# Impact Statement

## The Problem This Solves

When a refugee family arrives in New York City, they are often exhausted, traumatized, 
and disoriented. They may speak little or no English. They don't know who to call, 
where to go, or what they're entitled to. The organizations that exist to help them 
are real and accessible — but only if you know they exist.

IRC caseworkers do extraordinary work connecting newly arrived people to these resources. 
But caseworkers are human. They work limited hours. They carry heavy caseloads. 
And the people they serve often have urgent questions at 10pm on a Tuesday, 
or on a weekend, or in the middle of a crisis that can't wait until Monday morning.

**This chatbot is not a replacement for a caseworker. It is a bridge — available 24 hours 
a day, 7 days a week, to anyone with a phone.**

---

## Who This Is For

- A newly arrived refugee who doesn't know what ESL classes exist in their neighborhood
- An immigrant mother trying to find a food pantry that won't turn her away without documentation
- A survivor of violence who needs mental health support but doesn't know where to start
- A caseworker who wants to give a client a simple tool to explore resources on their own

---

## Why AI Is the Right Tool Here

Traditional resource directories — websites, printed pamphlets, spreadsheets — require 
the user to already know what they're looking for. They require literacy in English. 
They require the confidence to navigate a government website.

A conversational AI chatbot removes those barriers. A person can type (or eventually speak) 
in plain language:

> *"I need food for my children tonight"*  
> *"I don't have papers — can I still get help?"*  
> *"I am scared and I don't know what to do"*

And receive a warm, specific, human-feeling response — with a real address and a real 
phone number — immediately.

---

## What Makes This Different From a Google Search

1. **It understands context.** If someone asks "what about for my kids?" the chatbot 
   knows they're referring to the organization mentioned in the previous message.

2. **It removes the documentation barrier.** The chatbot is explicitly instructed to 
   remind users that NYC services are available regardless of immigration status — 
   something a Google search won't proactively tell you.

3. **It is trauma-informed by design.** The tone is warm and patient. It never judges. 
   It never asks for personal information. It always reminds users they are not alone.

4. **It handles crisis.** If someone expresses fear or danger, the chatbot immediately 
   provides crisis resources — before anything else.

---

## Personal Motivation

I built this project as the daughter of a first-generation immigrant. My mother came 
to this country and had to navigate systems she didn't understand, in a language she 
was still learning, without a guide.

I know she is not alone in that experience. Millions of people arrive in this country 
every year facing exactly what she faced. The International Rescue Committee exists 
to help them — and I built this tool to extend that help further.

This project is dedicated to every person who has ever arrived somewhere new with 
nothing but hope, and had to figure out the rest alone.

---

## Limitations & Future Work

This tool is a starting point, not a finished product. Known limitations:

- **English only (for now):** A future version should support Spanish, Arabic, French, 
  Haitian Creole, and other languages commonly spoken by NYC's refugee population.
- **NYC only (for now):** The resource database covers New York City. IRC operates in 
  29 other US cities — each would need their own resource database.
- **Resources change:** Phone numbers, addresses, and program availability change. 
  This database requires regular human verification to stay accurate.
- **Not a crisis line:** For immediate danger, users should always call 911. 
  This tool is not a substitute for emergency services.

Future versions could include voice input (for users with low literacy), 
multilingual support via Claude's translation capabilities, and integration 
with live resource availability APIs.

---

*Built with Anthropic's Claude API. Inspired by the mission of the International Rescue Committee.*
