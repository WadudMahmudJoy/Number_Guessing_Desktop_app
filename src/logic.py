import random

class NumberGuessingGame:
    def __init__(self, min_num=1, max_num=100):
        self.min_num = min_num
        self.max_num = max_num
        self.reset_game()

    def reset_game(self):
        self.target = random.randint(self.min_num, self.max_num)
        self.attempts = 0
        self.last_feedback = ""

    def guess(self, number):
        self.attempts += 1
        diff = abs(number - self.target)
        if number == self.target:
            self.last_feedback = f"Correct! You guessed it in {self.attempts} tries."
            return "correct"
        elif number > self.target:
            if diff > 20:
                self.last_feedback = "Too high!"
                return "too high"
            else:
                self.last_feedback = "High!"
                return "high"
        else:
            if diff > 20:
                self.last_feedback = "Too low!"
                return "too low"
            else:
                self.last_feedback = "Low!"
                return "low"