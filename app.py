"""
AI Email Task Agent

A workflow-style email automation agent that classifies an email,
extracts a task, detects priority, and suggests a follow-up action.
"""


def classify_email(state):
    email_text = state["email_text"].lower()

    if any(word in email_text for word in ["urgent", "asap", "immediately"]):
        state["category"] = "Urgent"
    elif any(word in email_text for word in ["meeting", "schedule", "calendar"]):
        state["category"] = "Meeting"
    elif any(word in email_text for word in ["invoice", "payment", "receipt"]):
        state["category"] = "Finance"
    else:
        state["category"] = "General"

    return state


def detect_priority(state):
    email_text = state["email_text"].lower()

    if any(word in email_text for word in ["urgent", "asap", "immediately"]):
        state["priority"] = "High"
    elif any(word in email_text for word in ["soon", "tomorrow", "next week"]):
        state["priority"] = "Medium"
    else:
        state["priority"] = "Low"

    return state


def extract_task(state):
    email_text = state["email_text"].lower()

    if "please" in email_text or "can you" in email_text:
        state["task"] = "Review the email and complete the requested action."
    else:
        state["task"] = "No clear task detected."

    return state


def suggest_follow_up(state):
    category = state["category"]
    priority = state["priority"]

    if category == "Urgent":
        state["follow_up"] = "Respond immediately and prioritize this email."
    elif category == "Meeting":
        state["follow_up"] = "Check calendar availability and prepare a meeting response."
    elif category == "Finance":
        state["follow_up"] = "Review payment or invoice details before replying."
    else:
        state["follow_up"] = "Review the email and respond if needed."

    state["summary"] = (
        f"Category: {category}\n"
        f"Priority: {priority}\n"
        f"Task: {state['task']}\n"
        f"Follow-up: {state['follow_up']}"
    )

    return state


def run_email_workflow(email_text):
    state = {
        "email_text": email_text,
        "category": "",
        "priority": "",
        "task": "",
        "follow_up": "",
        "summary": "",
    }

    state = classify_email(state)
    state = detect_priority(state)
    state = extract_task(state)
    state = suggest_follow_up(state)

    return state


def main():
    sample_email = """
    Hi Nishanth,

    Please review the project update and schedule a meeting for next week.

    Thanks.
    """

    result = run_email_workflow(sample_email)

    print("Email Task Agent Result")
    print("-----------------------")
    print(result["summary"])


if __name__ == "__main__":
    main()