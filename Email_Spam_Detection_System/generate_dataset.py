"""
generate_dataset.py
--------------------
Generates a synthetic but realistic labeled dataset of SPAM and HAM (not spam)
messages, similar in style/structure to the well-known SMS Spam Collection
dataset. This lets the project run fully offline while still producing a
reasonably large, varied training set (1000+ labeled messages).

Output: dataset.csv  (columns: label, message)   label -> spam / ham
"""

import csv
import random

random.seed(42)

# ---------------------------------------------------------------------------
# Building blocks for SPAM messages
# ---------------------------------------------------------------------------
spam_openers = [
    "WINNER!!", "CONGRATULATIONS", "URGENT", "FREE ENTRY", "ALERT",
    "Final Notice", "Limited Time Offer", "Dear Customer", "Hey there",
    "Attention", "IMPORTANT", "You have been selected", "Breaking News",
]

spam_bodies = [
    "You have won a ${amount} cash prize! Claim now by clicking the link below.",
    "Your mobile number has been selected to receive a free {item}. Reply YES to claim.",
    "Click here to claim your free {item} before the offer expires today!",
    "You have an unclaimed prize of ${amount}. Verify your account to receive it.",
    "Get a loan of ${amount} approved instantly, no credit check required!",
    "Your account will be suspended unless you verify your details immediately: {link}",
    "Congratulations! You've been chosen for a free {item} worth ${amount}.",
    "URGENT: Your bank account has unusual activity. Login now to secure it: {link}",
    "Earn ${amount} per day working from home! No experience needed, sign up now.",
    "Text WIN to 80086 to enter our weekly draw and win a brand new {item}!",
    "Your subscription payment of ${amount} has failed. Update your card here: {link}",
    "Hot singles in your area want to chat with you now! Click {link}",
    "You are pre-approved for a ${amount} credit card. Apply now, no fees!",
    "FREE {item} just for you! Limited stock, claim before midnight.",
    "This is your final reminder to claim your ${amount} refund. Act now: {link}",
    "Exclusive deal: Buy one {item} and get another absolutely free! Offer ends soon.",
    "Your parcel could not be delivered. Pay a small fee to reschedule: {link}",
    "Verify your identity now to avoid permanent account suspension: {link}",
    "You've been chosen to test our new {item} for free, just pay shipping.",
    "Claim your government grant of ${amount} today, no repayment needed!",
    "Act fast! Only 3 {item}s left at 90% discount, order now.",
    "You have 1 new voicemail regarding your ${amount} settlement claim. Call now.",
    "Double your investment in {item} stocks this week only, guaranteed returns!",
    "Your Netflix account is on hold. Update billing info immediately: {link}",
    "Win a brand new {item} by simply sharing this message with 10 friends!",
]

spam_items = ["iPhone", "laptop", "smartwatch", "vacation package", "gift card",
              "TV", "cruise trip", "PlayStation", "tablet", "coupon book"]
spam_links = ["bit.ly/claim-now", "secure-verify-account.com", "win-big-prizes.net",
              "your-refund-portal.com", "click-to-claim.co"]

def make_spam():
    opener = random.choice(spam_openers)
    body = random.choice(spam_bodies).format(
        amount=random.choice([500, 1000, 2500, 5000, 10000, 250, 750]),
        item=random.choice(spam_items),
        link=random.choice(spam_links),
    )
    return f"{opener}: {body}"


# ---------------------------------------------------------------------------
# Building blocks for HAM (normal) messages
# ---------------------------------------------------------------------------
ham_templates = [
    "Hey, are we still meeting for {event} tomorrow at {time}?",
    "Can you send me the {doc} before {time}? Thanks!",
    "I'll be home by {time}, do you need me to pick up anything?",
    "Thanks for the help with {topic} today, really appreciate it.",
    "Don't forget we have {event} scheduled for {time}.",
    "Just landed, will call you once I reach {place}.",
    "Can we reschedule our {event} to next week?",
    "Happy birthday! Hope you have a wonderful day.",
    "The meeting about {topic} has been moved to {time}.",
    "Let me know if you're free for {event} this weekend.",
    "I finished the {doc}, sending it over shortly.",
    "Mom said dinner is ready, come home soon.",
    "Great job on the {topic} presentation today!",
    "Are you coming to {place} this evening?",
    "Please review the {doc} and let me know your thoughts.",
    "I'm running a bit late, will reach {place} in 10 minutes.",
    "Thanks for the birthday wishes, means a lot!",
    "Let's catch up over coffee sometime next week.",
    "Reminder: your appointment is scheduled for {time}.",
    "Can you help me understand this {topic} assignment?",
    "The project deadline for {topic} has been extended to next Friday.",
    "I really enjoyed the movie we watched last night.",
    "Please find attached the {doc} you requested.",
    "See you at {place} at {time}, don't be late!",
    "How was your trip to {place}? Hope it went well.",
    "I'll send you the {doc} once I finish reviewing it.",
    "Can you pick me up from {place} after work?",
    "Let's plan the {event} for next month.",
    "Thank you for attending the {topic} session today.",
    "I'm still working on the {doc}, will share it soon.",
]

ham_events = ["lunch", "the meeting", "dinner", "the movie", "our call",
              "the workshop", "the interview", "class", "the party", "our trip"]
ham_docs = ["report", "presentation", "invoice", "assignment", "notes",
            "spreadsheet", "proposal", "resume", "contract", "summary"]
ham_topics = ["the project", "machine learning", "the budget", "marketing",
              "the app design", "history", "the client call", "python", "data science"]
ham_places = ["the office", "college", "home", "the airport", "the mall",
              "the gym", "the station", "downtown", "the library"]
ham_times = ["5 PM", "10 AM", "tomorrow morning", "tonight", "3:30 PM",
             "next Monday", "this weekend", "noon", "8 PM"]

def make_ham():
    template = random.choice(ham_templates)
    return template.format(
        event=random.choice(ham_events),
        doc=random.choice(ham_docs),
        topic=random.choice(ham_topics),
        place=random.choice(ham_places),
        time=random.choice(ham_times),
    )


# ---------------------------------------------------------------------------
# Generate dataset
# ---------------------------------------------------------------------------
def generate(n_spam=500, n_ham=500):
    seen = set()
    rows = []

    spam_count = 0
    attempts = 0
    while spam_count < n_spam and attempts < n_spam * 20:
        attempts += 1
        msg = make_spam()
        if msg not in seen:
            seen.add(msg)
            rows.append(("spam", msg))
            spam_count += 1

    ham_count = 0
    attempts = 0
    while ham_count < n_ham and attempts < n_ham * 20:
        attempts += 1
        msg = make_ham()
        if msg not in seen:
            seen.add(msg)
            rows.append(("ham", msg))
            ham_count += 1

    random.shuffle(rows)
    return rows


if __name__ == "__main__":
    data = generate()
    with open("dataset.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["label", "message"])
        writer.writerows(data)
    print(f"Generated {len(data)} messages -> dataset.csv")
