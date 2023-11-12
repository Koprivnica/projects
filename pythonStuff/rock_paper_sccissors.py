import random
import sys

class RPS:
    def __init__(self):
        
        self.moves: list[str] = ["rock", "paper", "sccissors"]
        self.user_score: int = 0
        self.ai_score: int = 0
    
    def play_game(self):

        user_move: str = input("Rock, Paper or Sccissors? >> ").lower()
        
        if user_move == "exit":
            print("THNX for playing")
            sys.exit()
        
        if user_move not in self.moves:
            print("Invalid move...")
            return self.play_game()
        
        ai_move: str = random.choice(self.moves)
        
        self.display_moves(user_move, ai_move)
        self.check_move(user_move, ai_move)
        
    def display_moves(self, user_move: str, ai_move: str):
        print("-----")
        print(f"You: {user_move.upper()}")
        print(f"AI: {ai_move.upper()}")
        print("-----")
    
    def check_move(self, user_move: str, ai_move: str):
        if user_move == ai_move:
            print("It is a tie")
            print(f"User {self.user_score} - {self.ai_score} AI")
        elif user_move == "rock" and ai_move == "sccissors":
            print("You win!")
            self.user_score += 1
            print(f"User {self.user_score} - {self.ai_score} AI")
        elif user_move == "sccissors" and ai_move == "paper":
            print("You win!")
            self.user_score += 1
            print(f"User {self.user_score} - {self.ai_score} AI")
        elif user_move == "paper" and ai_move == "rock":
            print("You win!")
            self.user_score += 1
            print(f"User {self.user_score} - {self.ai_score} AI")
        else:
            print("AI wins!")
            self.ai_score += 1
            print(f"User {self.user_score} - {self.ai_score} AI")
            
if __name__ == "__main__":
    rps = RPS()
    
    while True:
        rps.play_game()        