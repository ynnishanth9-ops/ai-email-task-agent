"""
AI Email Task Agent

A simple starter automation agent that classifies email text,
extracts possible tasks, and suggests follow-up actions.
"""


def classify_email(email_text):
    email_lower = email_text.lower()

    if any(word in email_lower for word in ["urgent", "asap", "immediately"]):
        return "Urgent"
    elif any(word in email_lower for word in ["meeting", "schedule", "calendar"]):
        return "Meeting"
    elif any(word in email_lower for word in ["invoice", "payment", "receipt"]):
        return "Finance"
    else:
        return "General"


def extract_task(email_text):
    if "please" in email_text.lower():
        return "Review the email and complete the requested action."
    return "No clear task detected."


def suggest_follow_up(category):
    follow_ups = {
        "Urgent": "Respond as soon as possible and prioritize this email.",
        "Meeting": "Check calendar availability and prepare a reply.",
        "Finance": "Review payment or invoice details before responding.",
        "General": "Review the email and respond if needed."
    }

    return follow_ups.get(category, "Review and respond if required.")


def main():
    sample_email = """
    Hi Nishanth,

    Please review the project update and schedule a meeting for next week.

    Thanks.
    """

    category = classify_email(sample_email)
    task = extract_task(sample_email)
    follow_up = suggest_follow_up(category)

    print("Email Category:", category)
    print("Detected Task:", task)
    print("Suggested Follow-up:", follow_up)


if __name__ == "__main__":
    main()