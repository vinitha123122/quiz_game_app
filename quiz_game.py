class QuizGame:
    def __init__(self):
        self.levels = {
            1: [("What is 2+2?", "4"), ("What is the capital of France?", "Paris")],
            2: [("What is 5*6?", "30"), ("Who wrote '1984'?", "George Orwell")],
            3: [("What is the square root of 81?", "9"), ("What year did the WW2 end?", "1945")],
            # You can add up to 10 levels similarly
        }
        self.current_level = 1
        self.score = 0

    def play_level(self):
        if self.current_level not in self.levels:
            print("Congratulations! You have completed all levels!")
            return False  # Stop the game

        print(f"\nStarting Level {self.current_level}...")
        questions = self.levels[self.current_level]
        for q, ans in questions:
            user_ans = input(q + " ")
            if user_ans.strip().lower() == ans.lower():
                self.score += 10
                print("Correct!")
            else:
                print("Wrong! The answer is:", ans)
        print(f"Level {self.current_level} complete! Score: {self.score}")
        self.current_level += 1
        return True  # Continue to next level

    def customize_avatar(self, avatar_choice):
        print(f"Avatar set to {avatar_choice}")

if __name__ == "__main__":
    game = QuizGame()

    avatar = input("Choose your avatar (Wizard/Knight/Archer): ")
    game.customize_avatar(avatar)

    while True:
        if not game.play_level():
            break

    print(f"Final Score: {game.score}")
    print("Thanks for playing!")
