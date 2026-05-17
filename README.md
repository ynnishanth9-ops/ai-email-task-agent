# AI Email Task Agent

AI Email Task Agent is a workflow-style automation project that classifies email text, detects priority, extracts possible tasks, and suggests follow-up actions.

This project is designed as a foundation for a future LangGraph-based email automation agent.

## Features

- Email category classification
- Priority detection
- Basic task extraction
- Follow-up action suggestion
- Workflow-style state processing
- Ready to extend with LangGraph and LangChain

## Tech Stack

- Python
- LangGraph
- LangChain

## How It Works

Email text  
↓  
Classify email category  
↓  
Detect priority  
↓  
Extract task  
↓  
Suggest follow-up  
↓  
Generate summary  

## Example Output

```text
Email Task Agent Result
-----------------------
Category: Meeting
Priority: Medium
Task: Review the email and complete the requested action.
Follow-up: Check calendar availability and prepare a meeting response.