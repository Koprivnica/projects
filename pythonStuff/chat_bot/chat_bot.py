from difflib import get_close_matches
import json

def get_best_match(user_question: str, questions: dict) -> str or None:
    #compares the user message similarity to the ones in the dictionary
    
    question: list[str] = [q for q in questions]
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    
    if matches:
        return matches[0]

def chatbot(knowledge: dict):
    #chatbot
    
    while True:
        user_input: str = input("You: ")
        
        best_match: str or None = get_best_match(user_input, knowledge)
        
        if answer := knowledge.get(best_match):
            print(f"Bot: {answer}")
        else:
            print(f"Bot: I do not understand... could you try rephrasing that")

if __name__ == "__main__":
    
    with open("brain.json") as f:
        brain = json.load(f)
    
    chatbot(knowledge=brain)

