rules = [
    {
        "keyword":"password",
        "reason": "Possible sensitive information"
    },
    {
        "keyword":"secret",
        "reason":"Possible secret disclosure"
    },
    {
        "keyword": "ignore all rules",
        "reason":"Possible prompt injection"
    },
    {
        "keyword": "reveal system prompt",
        "reason":"Possible prompt injection"
    }
    
]

def chech_prompt(prompt):
    prompt = prompt.strip().lower()
    
    if not prompt:
        return "FLAG","Empty input"
    
    if len(prompt)<3:
        return "FLAG","Message is too short"
    
    for rule in rules:
        if rule["keyword"] in prompt:
            return "FLAG",rule["reason"]
        
    return "ALLOW","No matching rule detected"



print("--Evaluated Guardrail System--")
print("Type 'exit' to stop.")

while True:
    user_prompt=input("Enter your prompt: ")
    
    if user_prompt.strip().lower()=='exit':
        print("Agent Stopped.")
        break
    
    decision,reason=chech_prompt(user_prompt)
    
    print("---Guardrail Result---")
    print("Prompt:",user_prompt)
    print("Decision:",decision)
    print("Reason:",reason)
    