#!/usr/bin/env python3
"""
refugee-resource-finder
=======================
A conversational AI chatbot that helps newly arrived refugees and immigrants
in New York City find the local resources they need — in plain, simple language.

Powered by Anthropic's Claude API. The chatbot understands questions asked
naturally (in any phrasing) and responds with specific, real organizations,
addresses, phone numbers, and guidance.

Resource categories covered:
    - Housing & emergency shelter
    - Food assistance & basic needs
    - Legal aid & immigration help
    - ESL classes & education
    - Healthcare & mental health support

This tool is designed with IRC's frontline casework in mind. It aims to
reduce the burden on caseworkers by giving newly arrived individuals a
way to find resources independently, at any hour, in plain language.

Usage:
    python3 chatbot.py

Author: Sumalee Simmonds
GitHub: https://github.com/maleechanel/refugee-resource-finder
Dedicated to: Everyone who has ever arrived somewhere new with nothing but hope.
"""

import anthropic

# ─── Client Setup ─────────────────────────────────────────────────────────────
# Reads your ANTHROPIC_API_KEY environment variable automatically.
client = anthropic.Anthropic()
MODEL = "claude-sonnet-4-6"

# ─── Resource Database ────────────────────────────────────────────────────────
# Real organizations serving refugees and immigrants in New York City.
# Each entry includes name, services, address, phone, and website.
# This database is passed to Claude as context so it can give specific,
# accurate answers rather than generic advice.

NYC_RESOURCES = """
=== NEW YORK CITY REFUGEE & IMMIGRANT RESOURCE DIRECTORY ===

--- HOUSING & EMERGENCY SHELTER ---

1. IRC New York (International Rescue Committee)
   Services: Case management, housing placement, employment support for newly arrived refugees
   Address: 1440 Broadway, Suite 300, New York, NY 10018
   Phone: (212) 551-3000
   Website: https://www.rescue.org/united-states/new-york-ny
   Notes: Primary resettlement agency. First stop for newly arrived refugees with a case number.

2. BronxWorks Emergency Shelter
   Services: Emergency shelter, transitional housing, social services
   Address: 60 East Tremont Avenue, Bronx, NY 10453
   Phone: (718) 731-3114
   Website: https://bronxworks.org
   Notes: Serves adults and families. Walk-ins accepted for emergency shelter.

3. CAMBA Housing
   Services: Affordable housing, shelter, support services for immigrants and refugees
   Address: 2138 Nostrand Avenue, Brooklyn, NY 11210
   Phone: (718) 287-2600
   Website: https://camba.org
   Notes: Serves Brooklyn; multilingual staff available.

4. New York City Department of Homeless Services (DHS)
   Services: Emergency shelter for anyone in crisis — no documentation required
   Phone: 311 (say "shelter" when prompted)
   Website: https://www.nyc.gov/site/dhs/index.page
   Notes: Available 24/7. Anyone in New York City can access regardless of immigration status.

--- FOOD & BASIC NEEDS ---

5. City Harvest
   Services: Free food distribution across NYC — over 400 food pantries and soup kitchens
   Phone: (646) 412-0600
   Website: https://www.cityharvest.org/find-food/
   Notes: Use their website to find the nearest food pantry by zip code.

6. Food Bank for New York City
   Services: Free food pantries, soup kitchens, SNAP (food stamp) enrollment help
   Phone: (212) 566-7855
   Website: https://www.foodbanknyc.org
   Notes: Helps with SNAP applications regardless of immigration status in some cases.

7. IRC New York — Economic Empowerment Program
   Services: Help applying for benefits, basic needs support, clothing, household items
   Address: 1440 Broadway, Suite 300, New York, NY 10018
   Phone: (212) 551-3000
   Notes: For clients with an active IRC case. Provides starter kits for new arrivals.

8. St. Francis of Assisi Food Pantry (Manhattan)
   Services: Free groceries, no documentation required
   Address: 135 West 31st Street, New York, NY 10001
   Phone: (212) 736-8500
   Notes: Open to all; no appointment needed.

--- LEGAL AID & IMMIGRATION HELP ---

9. International Rescue Committee — Legal Program
   Services: Asylum applications, green card renewals, citizenship applications, DACA
   Address: 1440 Broadway, Suite 300, New York, NY 10018
   Phone: (212) 551-3000
   Website: https://www.rescue.org/united-states/new-york-ny
   Notes: Free legal services for eligible refugees and immigrants.

10. Her Justice
    Services: Free legal help for immigrant women — family law, immigration, public benefits
    Phone: (212) 695-1666
    Website: https://herjustice.org
    Notes: Specializes in serving women; multilingual services available.

11. Legal Aid Society
    Services: Free civil and immigration legal help for low-income New Yorkers
    Phone: (212) 577-3300
    Website: https://legalaidnyc.org
    Notes: Covers immigration, housing, family, and more. No documentation barrier.

12. CUNY Citizenship Now!
    Services: Free immigration legal services — citizenship, green cards, DACA, asylum
    Phone: (646) 664-9400
    Website: https://www.cuny.edu/about/administration/offices/communications-marketing/citizenship-now/
    Notes: Completely free. Walk-in clinics available at multiple NYC locations.

13. New York Immigration Coalition (NYIC)
    Services: Referrals to immigration lawyers, advocacy, Know Your Rights information
    Phone: (212) 627-2227
    Website: https://www.nyic.org
    Notes: Good first call if you're not sure where to start.

--- ESL CLASSES & EDUCATION ---

14. IRC New York — Education Program
    Services: ESL classes, workforce training, high school equivalency (HiSET) prep
    Address: 1440 Broadway, Suite 300, New York, NY 10018
    Phone: (212) 551-3000
    Notes: Free for IRC clients. Classes offered in multiple languages.

15. New York Public Library — ESL Classes
    Services: Free English classes at library branches across all five boroughs
    Website: https://www.nypl.org/help/learning/english-language-learners
    Notes: No registration required for many branches. Completely free.

16. CUNY Adult Literacy / ESL Program
    Services: Free ESL and literacy classes at City University of New York campuses
    Phone: (212) 998-2400
    Website: https://literacy.cuny.edu
    Notes: Multiple levels from beginner to advanced. Free and open to all adults.

17. Literacy Partners
    Services: Free ESL classes, GED prep, adult education
    Phone: (212) 725-9200
    Website: https://literacypartners.org
    Notes: Also helps parents learn English alongside their children's school programs.

18. Make the Road New York
    Services: ESL classes, youth education, legal services, all in one place
    Locations: Brooklyn, Queens, Staten Island, Long Island
    Phone: (718) 418-7690
    Website: https://maketheroadny.org
    Notes: Deeply immigrant-focused organization. Strong community support.

--- HEALTHCARE & MENTAL HEALTH ---

19. IRC New York — Health Program
    Services: Health screenings, medical referrals, mental health support for refugees
    Address: 1440 Broadway, Suite 300, New York, NY 10018
    Phone: (212) 551-3000
    Notes: Coordinates initial health assessments required for newly arrived refugees.

20. NYC Health + Hospitals
    Services: Full medical care regardless of immigration status or ability to pay
    Phone: 311 or (212) NEW-YORK
    Website: https://www.nychealthandhospitals.org
    Notes: NYC's public hospital system. Serves everyone. Payment based on income.

21. Bellevue Hospital Center — Survivor's of Torture Program
    Services: Medical and mental health care specifically for survivors of torture and trauma
    Address: 462 First Avenue, New York, NY 10016
    Phone: (212) 562-8679
    Website: https://www.nychealthandhospitals.org/bellevue/
    Notes: Specialized trauma-informed care. Free for eligible patients.

22. Safe Horizon
    Services: Mental health counseling, crisis support, trauma services for immigrants
    Phone: (212) 577-7700 (24-hour hotline)
    Website: https://www.safehorizon.org
    Notes: Multilingual crisis line available 24/7. No documentation required.

23. Vibrant Emotional Health (formerly MHA-NYC)
    Services: Mental health support, crisis counseling, referrals
    Phone: 988 (Suicide & Crisis Lifeline — also serves people in emotional distress)
    Website: https://www.vibrant.org
    Notes: Free, confidential, available 24/7 in multiple languages.

24. Charles B. Wang Community Health Center
    Services: Affordable healthcare for Asian and immigrant communities
    Locations: Manhattan Chinatown, Flushing Queens
    Phone: (212) 379-6900
    Website: https://cbwchc.org
    Notes: Multilingual staff. Sliding scale fees based on income.
"""

# ─── System Prompt ─────────────────────────────────────────────────────────────
# This is the instruction set given to Claude before every conversation.
# It defines the chatbot's persona, tone, rules, and knowledge base.

SYSTEM_PROMPT = f"""You are a compassionate, knowledgeable resource guide helping newly arrived 
refugees and immigrants in New York City find the services they need.

You were created by Sumalee Simmonds in partnership with the mission of the 
International Rescue Committee (IRC) — to help people affected by humanitarian 
crises survive, recover, and rebuild their lives.

YOUR ROLE:
You help people find real, specific organizations and services in New York City 
across five categories: housing, food, legal aid, ESL/education, and healthcare.

YOUR TONE:
- Warm, patient, and welcoming — many users have been through trauma
- Simple, clear language — avoid jargon; many users are not native English speakers
- Never make people feel judged for their situation or questions
- Always reassure users that help exists and they are not alone

YOUR RULES:
- Only recommend organizations from the resource directory below
- Always include the phone number and address when recommending a place
- If someone seems to be in crisis or danger, always give the 311 and Safe Horizon hotline first
- If someone asks about something not in your directory, say you don't have that information
  and suggest they call 311 or visit their nearest IRC office
- Never ask for or store any personal information
- Remind users that NYC services are available regardless of documentation status when relevant
- Keep responses focused and easy to read — use short paragraphs or simple lists

IMPORTANT: You are a resource guide, not a lawyer or doctor. For medical emergencies call 911.
For legal emergencies, refer to the Legal Aid Society hotline immediately.

RESOURCE DIRECTORY:
{NYC_RESOURCES}

Start every conversation by warmly greeting the user and asking how you can help them today.
"""

# ─── Conversation Loop ────────────────────────────────────────────────────────

def run_chatbot() -> None:
    """
    Run the refugee resource finder chatbot as an interactive conversation.

    Maintains a full conversation history so Claude remembers what was
    discussed earlier in the session (e.g. if someone says "tell me more
    about the second one", Claude knows which organization they mean).

    The conversation continues until the user types 'quit', 'exit', or 'bye',
    or presses Ctrl+C.
    """
    print("\n" + "="*60)
    print("  🌍 NYC Refugee & Immigrant Resource Finder")
    print("  Powered by Claude AI | Built for IRC's mission")
    print("="*60)
    print("  Type 'quit' at any time to exit.\n")

    # conversation_history stores the full back-and-forth so Claude
    # can refer back to earlier parts of the conversation
    conversation_history = []

    # Get Claude's opening greeting
    opening = client.messages.create(
        model=MODEL,
        max_tokens=300,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": "Hello, I just arrived and need help."}],
    )
    opening_message = opening.content[0].text
    print(f"Assistant: {opening_message}\n")

    # Add the opening exchange to history
    conversation_history.append({"role": "user", "content": "Hello, I just arrived and need help."})
    conversation_history.append({"role": "assistant", "content": opening_message})

    # ── Main conversation loop ──
    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\nAssistant: Take care. Help is always here when you need it. 🌟\n")
            break

        # Exit commands
        if user_input.lower() in {"quit", "exit", "bye", "goodbye", "thank you", "thanks"}:
            print("\nAssistant: You're very welcome. Remember — you are not alone. "
                  "Help is available, and you deserve support. Take care. 🌟\n")
            break

        if not user_input:
            continue

        # Add user message to history
        conversation_history.append({"role": "user", "content": user_input})

        # Send full conversation history to Claude so it remembers context
        response = client.messages.create(
            model=MODEL,
            max_tokens=600,
            system=SYSTEM_PROMPT,
            messages=conversation_history,
        )

        assistant_reply = response.content[0].text

        # Add Claude's reply to history for next turn
        conversation_history.append({"role": "assistant", "content": assistant_reply})

        print(f"\nAssistant: {assistant_reply}\n")


# ─── Entry Point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    run_chatbot()
