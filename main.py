from guardrail import check_prompt


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
            user_prompt=input("Enter your prompt: ")
            
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