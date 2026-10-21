
# evaluated guardrail agent

A Python-based project that checks user prompts against
basic rules to flag potentially sensitive information
and simple prompt injection attempts.

## features

- Keyword-based prompt checking
- Detection of empty and very short inputs
- Separate guardrail logic and application interface
- Clear ALLOW and FLAG decisions

## current technologies

- Python
- Git and GitHub

## How to Run

1. Install Python 3.
2. Open a terminal in the project directory.
3. Run:

   python main.py

## current limitations

This project uses basic keyword matching. It is a learning
prototype and does not provide comprehensive security
against prompt injection or sensitive information exposure.
