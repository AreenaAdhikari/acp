import random

class AIGuessingGame:
    def __init__(self):
        self.score = 0
        self.total_questions = 0
        self.places = [
            ("Eiffel Tower, Paris", False),
            ("Times Square, New York", False),
            ("Taj Mahal, India", False),
            ("Sydney Opera House", False),
            ("Great Wall of China", False),
            ("Burj Khalifa, Dubai", False),
            ("Statue of Liberty, USA", False),
            ("Colosseum, Rome", False),
            ("Machu Picchu, Peru", False),
            ("Pyramids of Giza, Egypt", False),
            ("Neon Gardens, Cyber City", True),
            ("Crystal Mountain Resort", True),
            ("Floating Islands of Pandora", True),
            ("Holographic Beach Club", True),
            ("Space Elevator Terminal", True),
            ("Underwater Bubble City", True),
            ("Cloud 9 Floating Hotel", True),
            ("Dragon's Tail Mountains", True),
            ("Mecha Robot Factory", True),
            ("Alien Art Museum", True)
        ]
        random.shuffle(self.places)
    
    def ask_question(self, place_name):
        print(f"\n{'='*50}")
        print(f"📍 Place: {place_name}")
        print(f"{'='*50}")
        while True:
            answer = input("Is this AI generated? (yes/no): ").lower().strip()
            if answer in ['yes', 'y']:
                return True
            elif answer in ['no', 'n']:
                return False
            else:
                print("Please answer with 'yes' or 'no'")
    
    def play_game(self):
        print("\n" + "="*50)
        print("WELCOME TO 'IS THIS AI OR NOT?' GAME!")
        print("="*50)
        print("I'll show you a place name, and you guess if it's")
        print("AI-generated or a real place on Google Maps!")
        print("-" * 50)
        input("Press Enter to start the game...")
        
        for place_name, is_ai in self.places[:5]:
            self.total_questions += 1
            user_guess = self.ask_question(place_name)
            if user_guess == is_ai:
                print("✅ CORRECT! Well done!")
                self.score += 1
            else:
                if is_ai:
                    print("INCORRECT! This place is AI-generated!")
                else:
                    print("INCORRECT! This is a real place on Google Maps!")
            print(f"Score: {self.score}/{self.total_questions}")
            if self.total_questions < 5:
                input("\nPress Enter for next question...")
        self.show_final_score()
    
    def show_final_score(self):
        print("\n" + "="*50)
        print("GAME OVER!")
        print("="*50)
        print(f"Final Score: {self.score}/{self.total_questions}")
        percentage = (self.score / self.total_questions) * 100
        if percentage == 100:
            print("🏆 PERFECT! You're an AI detection expert!")
        elif percentage >= 80:
            print("Great job! You really know your places!")
        elif percentage >= 60:
            print("Good effort! You're getting better!")
        elif percentage >= 40:
            print("Keep practicing! You'll improve!")
        else:
            print("AI tricked you this time! Want to play again?")
        print("="*50)
    
    def play_again(self):
        while True:
            again = input("\nDo you want to play again? (yes/no): ").lower().strip()
            if again in ['yes', 'y']:
                random.shuffle(self.places)
                self.score = 0
                self.total_questions = 0
                return True
            elif again in ['no', 'n']:
                print("\nThanks for playing! Goodbye!")
                return False
            else:
                print("Please answer with 'yes' or 'no'")

if __name__ == "__main__":
    game = AIGuessingGame()
    playing = True
    while playing:
        game.play_game()
        playing = game.play_again()