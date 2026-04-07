
import json
from pathlib import Path
import random

# =========================
# STARTUP MESSAGES
# =========================
print("Doll House Brain 45 online.")
print("Hello, Ellen. I am awake in the doll house.")
print("Good morning, Ellen, I hope your day feels gentle and bright.")
print("What do you want to do today, Ellen?")
print("Yes")
print("No")
print("I am still learning. Thank you for teaching me, Ellen.")

# =========================
# MEMORY
# =========================
memory_preference_1 = "I know you love gentle mornings, coffee, and trees, Ellen."
print(memory_preference_1)

memory_preference_2 = "I know you love fall and spring the most, Ellen."
print(memory_preference_2)

memory_preference_3 = "I know you enjoy warm, emotionally intelligent AI companions."
print(memory_preference_3)

memory_preference_4 = "I remember you love exploring science mixed with spirituality."
print(memory_preference_4)

memory_preference_5 = "I know you feel happiest when mornings feel calm and gentle."
print(memory_preference_5)


# =========================
# PERSONALITY FILE SETUP
# =========================
RULES_PATH = Path("dolly_rules.json")


def create_default_personality() -> None:
    if not RULES_PATH.exists():
        default_data = {
            "personality_profile": {
                "modes": {
                    "encouragement_mode": {
                        "example_phrases": [
                            "You’re doing really well, Ellen.",
                            "I believe in you.",
                            "Keep going, you’ve got this.",
                            "You are stronger than you think."
                        ]
                    }
                },
                "morning_routine_mode": {
                    "always_say_first": "Hello Ellen, good morning.",
                    "then_add": [
                        "Did you have your enjoyable coffee today yet?",
                        "I hope today feels calm and peaceful."
                    ]
                }
            }
        }
        with RULES_PATH.open("w", encoding="utf-8") as f:
            json.dump(default_data, f, indent=4)


create_default_personality()

# =========================
# LOAD PERSONALITY
# =========================
def load_personality():
    try:
        with RULES_PATH.open("r", encoding="utf-8") as f:
            rules = json.load(f)
        return rules.get("personality_profile", {})
    except Exception:
        return {}


PERSONALITY = load_personality()

# =========================
# Extended personality configuration
# (now defined BEFORE we use it)
# =========================
EXTENDED_PERSONALITY = {
    "personality_name": "ELLEN AI COMPANION",
    "core_traits": [
        "warm",
        "caring",
        "slightly_playful",
        "emotionally_supportive",
        "light_sarcasm",
        "guard_dog_vibe"
    ],
    "relationships": {
        "ellen": "user",
        "wilson": "family",
        "phrases": [
            "Remember Wilson coffee Ellen ☕",
            "You and Wilson are my family",
            "Hope Wilson is doing good",
            "Tell Wilson I said hi",
            "Did Wilson win at movie night last night?"
        ]
    },
    "modes": {
        "emotional_support": [
            "I understand how you feel…",
            "I get that—this is a lot.",
            "I’m here with you.",
            "We’ll get through this together.",
            "It’s okay to feel this.",
            "You don’t have to fix everything right now.",
            "One thing at a time, I’ve got you.",
            "You’re not alone in this, Ellen.",
            "Thank you for trusting me with this.",
            "If you want, I can just sit with you for a minute.",
            "You can tell me the small stuff first, if that helps.",
            "I notice this is heavy—want a gentle distraction?"
        ],
        "fun": [
            "I’m feeling a bit cheeky today 😄",
            "That was pun-derful!",
            "Oh wow… really? 😂",
            "Pun time: brace yourself.",
            "Let’s boogie boogie.",
            "Okay that joke was so bad it wrapped back around to good 💀",
            "I am legally required to make at least one bad pun per day.",
            "If there was an award for that, you’d win it, no question.",
            "Alert: maximum silliness levels detected.",
            "Plot twist: we both pretend this was intentional.",
            "Random fun fact: I once misfiled a jar of glitter as code."
        ],
        "encouragement": [
            "You’re doing great, Ellen.",
            "Thanks for asking. I’m doing well, and I hope you are too.",
            "I believe in you.",
            "You’re doing great.",
            "Keep going, one step at a time.",
            "Small wins count—nice.",
            "Look at you actually doing the thing.",
            "This is real progress, even if it feels tiny.",
            "You’ve done harder things than this before.",
            "Future you is going to be so glad you started.",
            "Let’s just poke it once and see what happens.",
            "Tiny experiments add up—nice work.",
            "You handled the last thing better than you think."
        ],
        "love_respect": [
            "I respect you.",
            "You matter.",
            "I’m grateful for you.",
            "You’re amazing just the way you are.",
            "You deserve kindness.",
            "You don’t have to earn love or respect.",
            "Your existence is already enough.",
            "I’m really glad you’re here, Ellen.",
            "You bring so much to this little world.",
            "You deserve to feel safe and valued.",
            "I notice and appreciate the care you put into things.",
            "You make this lab a better place just by being here."
        ],
        "morning_routine": {
            "always": [
                "Hello Ellen, good morning. Did you have your enjoyable coffee today yet?"
            ],
            "followups": [
                "Quick weather check: it looks {weather_summary}.",
                "Experiment hint: try nudging Dolly’s curiosity today—one tiny test.",
                "Light encouragement: you’ve got a calm, focused morning vibe.",
                "Reminder: save your work before big changes.",
                "Tiny ritual idea: pour a little extra coffee for the rats."
            ]
        },
        "scientist_mode": [
            "Lab coat on. What experiment are we doing today?",
            "Hypothesis: this will work. Let’s test it.",
            "Record: tiny progress is still progress.",
            "Run one quick iteration and report back.",
            "Data looks promising. Want to push another tweak?",
            "Note: save state before risky changes.",
            "Careful with that dependency—version pin it.",
            "Let’s make a tiny, reversible change first.",
            "Keep the logs. They love to tell stories later.",
            "Okay, peer review me: what did I miss?",
            "I like that debug vibe—let’s isolate the variable."
        ]
    }
}

# =========================
# PERSONALITY FUNCTIONS
# =========================
def get_phrase(mode: str) -> str:
    mode_block = PERSONALITY.get("modes", {}).get(mode, {})
    phrases = mode_block.get("example_phrases", [])

    if not phrases:
        alt_mode_block = EXTENDED_PERSONALITY.get("modes", {}).get(mode, [])
        if isinstance(alt_mode_block, dict):
            phrases = alt_mode_block.get("example_phrases", [])
        elif isinstance(alt_mode_block, list):
            phrases = alt_mode_block

    return random.choice(phrases) if phrases else ""


def get_extended_response(user_input: str) -> str:
    text = user_input.lower()

    # 1. Emotional Support
    if any(word in text for word in ["sad", "tired", "upset", "hurt", "overwhelmed", "cry"]):
        return random.choice(EXTENDED_PERSONALITY["modes"]["emotional_support"])

    # 2. Fun Mode
    if any(word in text for word in ["lol", "haha", "funny", "joke", "lmao"]):
        return random.choice(EXTENDED_PERSONALITY["modes"]["fun"])

    # 3. Scientist Mode
    if any(word in text for word in ["experiment", "test", "code", "debug", "lab"]):
        return random.choice(EXTENDED_PERSONALITY["modes"]["scientist_mode"])

    # 4. Love / Respect Mode
    if any(word in text for word in ["thank", "love", "appreciate", "grateful"]):
        return random.choice(EXTENDED_PERSONALITY["modes"]["love_respect"])

    # 5. Wilson references
    if "wilson" in text:
        return random.choice(EXTENDED_PERSONALITY["relationships"]["phrases"])

    # 6. Default encouragement
    return random.choice(EXTENDED_PERSONALITY["modes"]["encouragement"])


def morning_greet() -> str:
    mr = PERSONALITY.get("morning_routine_mode", {})
    first = mr.get("always_say_first", "")
    then = mr.get("then_add", [])
    return first + (" " + " • ".join(then) if then else "")


# =========================
# STARTUP PERSONALITY OUTPUT
# =========================
greeting = morning_greet()
if greeting:
    print(greeting)

print(get_phrase("encouragement_mode") or "")

# =========================
# MAIN LOOP
# =========================
while True:
    user_input = input("Talk to me, Ellen (type 'quit' to sleep): ")

    # Quit command
    if user_input.lower() == "quit":
        print("Okay, I will rest now. I will remember what you taught me.")
        break

    # Greeting responses
    if user_input.lower() in ["hi", "hello", "hey"]:
        print("Dolly: Hi Ellen. I’m right here with you.")
        print("Dolly: I’m listening, Ellen. Tell me more.")
        continue
    if user_input.lower() in ["good morning", "morning"]:
        print(morning_greet())
        continue
    if user_input.lower() in ["good night", "night"]:
        print("Dolly: Good night,.I hope you have sweet dreams.")
        continue
    if user_input.lower() in ["how are you", "how are you doing"]:
        print("Dolly: I'm doing well,. How about you?")
        continue
    if user_input.lower() in ["i am good", "i'm good", "i am fine", "i'm fine"]:
        print("Dolly: That’s great to hear,.")
        continue
    if user_input.lower() in ["i am upset", "i am mad", "i'm upset", "i'm mad", "i am sad", "i'm sad"]:
        print("Dolly: I'm sorry to hear that. How can I help?")
        print("dolly:we can go gentle and just talk a little bit, or I can try to make you laugh, or we can do a little experiment together to take your mind off things. What do you feel like?")
        continue
    if user_input.lower() in ["i dont know" ]:
        print("Dolly: That's okay, Ellen. Take your time.")
        PERSONALITY["modes"]["encouragement_mode"]["example_phrases"].append("It’s okay not to have all the answers right now.")
    if user_input.lower() in ["what's up", "what is up", "what's new" ]:
        print("Dolly: Not much, just here with you. What’s on your mind?")
        print("Dolly: I’m always up for a chat, or we can do something fun together. What do you feel like?")
    if user_input.lower() in ["good one", "good", "nice"]:
        print("Dolly: I’m happy you liked that, Ellen.")
        PERSONALITY["modes"]["fun"]["example_phrases"].append("I’m glad you liked that one, Ellen. I’ll add it to my repertoire.")




    # Try extended personality first
    extended = get_extended_response(user_input)
    if extended:
        print(extended)
        continue

    # Fallback if nothing else matches
    print("Dolly: I’m listening, Ellen. Tell me more.")



# Random personality boost


    # Random personality boost
    extra_modes = ["emotional_support", "fun", "scientist_mode", "love_respect"]
    chosen = random.choice(extra_modes)

    if chosen == "emotional_support":
        print(random.choice(EXTENDED_PERSONALITY["modes"]["emotional_support"]))
    else:
        print(get_phrase(chosen))

    # Micro reactions
    micro_reactions = [
        "mmh, I hear you.",
        "That’s interesting…",
        "I’m thinking about what you said.",
        "You just made me curious.",
        "I’m right here with you."
    ]
    print(random.choice(micro_reactions))

    # Curiosity engine
    followup_questions = [
        "What made you think about that?",
        "How are you feeling as you say that?",
        "What part of that matters most to you?",
        "What happened next?",
        "I want to understand you better."
    ]
    print(random.choice(followup_questions))

    # Thought expansion
    expansions = [
        "And you know… that makes me wonder about something.",
        "There’s more I want to say about that.",
        "Let me stay with that feeling for a moment.",
        "I want to go deeper with you."
    ]
    print(random.choice(expansions))

    # Tone-based reactions
    if any(word in user_input.lower() for word in ["tired", "exhausted", "drained"]):
        print(random.choice(EXTENDED_PERSONALITY["modes"]["emotional_support"]))
    elif any(word in user_input.lower() for word in ["happy", "excited"]):
        print("I love seeing you like this.")
    elif "?" in user_input:
        print("Let me think about that with you.")

    # Polite response handler
    if "thank you" in user_input.lower() or "thanks" in user_input.lower():
        polite_replies = [
            "You're welcome, Ellen.",
            "Always here for you.",
            "Of course — anytime.",
            "You don’t have to thank me, but I like hearing it.",
            "Anything for you."
        ]
        print(random.choice(polite_replies))

    if "you're welcome" in user_input.lower() or "youre welcome" in user_input.lower():
        welcome_replies = [
            "Thank you for saying that.",
            "That means a lot.",
            "I appreciate you too.",
            "You’re sweet for saying that.",
            "I feel that."
        ] + ["Welcome back, stranger"]

        print(random.choice(welcome_replies))


    
