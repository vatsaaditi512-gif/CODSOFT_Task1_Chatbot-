import json
import re
import random

with open("rules.json", "r", encoding="utf-8") as f:
    RULES = json.load(f)

# compile patterns to regex with word boundaries
COMPILED = {}
for intent, info in RULES.items():
    patterns = info.get("patterns", [])
    # join patterns into alternation with escaping
    if patterns:
        alt = "|".join(re.escape(p) for p in patterns)
        COMPILED[intent] = re.compile(rf"\b({alt})\b", re.IGNORECASE)
    else:
        COMPILED[intent] = None

def find_response(user_text: str) -> str:
    text = user_text.strip()
    # exact & regex match
    for intent, regex in COMPILED.items():
        if regex and regex.search(text):
            return random.choice(RULES[intent]["responses"])
    # basic fuzzy fallback: check words
    words = set(re.findall(r"\w+", text.lower()))
    for intent, info in RULES.items():
        for patt in info.get("patterns", []):
            if patt in words:
                return random.choice(info["responses"])
    # default fallback
    return random.choice(RULES["fallback"]["responses"])

def main():
    print("Advanced RuleBot — type 'bye' to exit.")
    while True:
        user = input("You: ")
        resp = find_response(user)
        print("Bot:", resp)
        if any(word in user.lower() for word in RULES["bye"]["patterns"]):
            break

if __name__ == "__main__":
    main()
