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
