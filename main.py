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

def check_prompt(prompt):
    if not isinstance(prompt,str):
        return "FLAG","Input must be text"
    
    prompt=prompt.strip().lower()
    
    if not prompt:
        return "FLAG","Empty input"
    
    if len(prompt) < 3:
        return "FLAG","Message is too short"
    
    for rule in rules:
        if rule["keyword"] in prompt:
            return "FLAG",rule["reason"]
    
    
    return "ALLOW","No matching rule detected"


def display_result(prompt,decision,reason):
    print("---Guardrail Result---")
    
    print("Prompt:",prompt)
    print("Decision:",decision)
    print("Reason:",reason)
    

def main():
    
    print("=== Evaluated Guardrail Agent ===")
    print("Type 'exit' to stop.")
    
    while True:
        
        try:
            user_prompt=input("Enter your prompt")
            
            if user_prompt.strip().lower()=='exit':
                print("Agent stopped")
                break
            decision,reason=check_prompt(user_prompt)
            
            display_result(user_prompt,decision,reason)
        except(EOFError,KeyboardInterrupt):
            print("Agent Stopped.")
            break
        

if __name__== "__main__":
    main()