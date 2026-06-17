# NYC Refugee and Immigrant Resource Finder

A conversational AI chatbot that helps newly arrived refugees and immigrants
in New York City find the resources they need in plain, simple language,
available 24 hours a day.

Built in alignment with the mission of the International Rescue Committee (IRC).
https://www.rescue.org/

Read the full impact statement: IMPACT.md

---

## What it does

You type a question in plain language:

  "I just arrived and I need food for my children tonight"
  "I don't have papers — can I still get help?"
  "I need a lawyer for my asylum case"
  "Where can I learn English for free?"

The chatbot responds with specific real organizations, addresses,
phone numbers, and warm guidance — immediately.

---

## Resource categories covered

- Housing and emergency shelter
- Food assistance and basic needs
- Legal aid and immigration help
- ESL classes and education
- Healthcare and mental health support

All resources are real organizations serving New York City.
All services are available regardless of immigration status.

---

## How it works

The chatbot is powered by Anthropic's Claude API with a curated database
of 24 real NYC organizations embedded in the system prompt.

Claude maintains full conversation history so it understands context across
multiple messages — if someone says "tell me more about the second one,"
it knows exactly which organization they mean.

The system prompt instructs Claude to:
- Use warm, patient, simple language
- Never ask for personal information
- Always surface crisis resources first if someone is in danger
- Remind users that services are available regardless of documentation status

---

## Setup

Requirements: Python 3.9 or higher, an Anthropic API key

  git clone https://github.com/sumaleesimmonds/refugee-resource-finder.git
  cd refugee-resource-finder
  pip3 install anthropic
  export ANTHROPIC_API_KEY="sk-ant-your-key-here"
  python3 chatbot.py

---

## Sample conversation

  Assistant: Hello and welcome. I am here to help you find support
  in New York City. You are not alone. What do you need help with today?

  You: I need food for my family tonight

  Assistant: Of course — here are places you can go today for free food,
  no documentation required:

  St. Francis of Assisi Food Pantry (Manhattan)
  135 West 31st Street, New York, NY 10001
  Phone: (212) 736-8500
  Open to everyone. No appointment needed.

  City Harvest Food Pantry Network
  Phone: (646) 412-0600
  Website: cityharvest.org/find-food
  Use their website to find the nearest pantry by zip code.

  Would you like help finding anything else — shelter, legal help,
  English classes, or healthcare?

---

## Why this matters

Traditional resource directories require the user to already know what
they are looking for, to read English fluently, and to have the confidence
to navigate a government website.

A conversational AI removes those barriers. Someone in crisis can type
in plain language and receive a warm, specific, human-feeling response
with a real address and phone number — immediately, at any hour.

Read the full impact statement in IMPACT.md.

---

## Limitations and future work

- English only (for now) — future versions should support Spanish, Arabic,
  French, Haitian Creole, and other languages common in NYC refugee communities
- NYC only (for now) — IRC operates in 29 US cities, each needing its own database
- Resources change — phone numbers and program availability require regular verification
- Not a crisis line — for immediate danger, always call 911

---

## Personal dedication

I built this as the daughter of a first-generation immigrant. My mother
navigated systems she did not understand, in a language she was learning,
without a guide. This tool is dedicated to everyone who has arrived
somewhere new with nothing but hope.

---

## License

MIT — free to use, adapt, and build upon for humanitarian purposes.
