import json

# Load rules from JSON
with open("rules.json", "r", encoding="utf-8") as f:
    RULES = json.load(f)

def find_response(user_text: str) -> str:
    text = user_text.lower()
    # iterate rule groups
    for intent, info in RULES.items():
        for patt in info.get("patterns", []):
            if patt in text:            # substring match
                # return a simple rotation/random choice (first for now)
                return info["responses"][0]
    # fallback
    return RULES["fallback"]["responses"][0]

def main():
    print("RuleBot — type 'bye' to exit.")
    while True:
        user = input("You: ").strip()
        if not user:
            continue
        resp = find_response(user)
        print("Bot:", resp)
        if any(word in user.lower() for word in RULES["bye"]["patterns"]):
            break

if __name__ == "__main__":
    main()
