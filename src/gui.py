import tkinter as tk
from tkinter import messagebox
from logic import NumberGuessingGame

class NumberGuessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f4f8")

        self.game = NumberGuessingGame()

        self.title_label = tk.Label(root, text="Guess the Number!", font=("Arial", 18, "bold"), bg="#f0f4f8", fg="#333")
        self.title_label.pack(pady=10)

        self.info_label = tk.Label(root, text=f"Guess a number between {self.game.min_num} and {self.game.max_num}", font=("Arial", 12), bg="#f0f4f8")
        self.info_label.pack(pady=5)

        self.entry = tk.Entry(root, font=("Arial", 14), justify="center")
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", lambda event: self.check_guess())

        self.guess_btn = tk.Button(root, text="Guess", font=("Arial", 12), command=self.check_guess, bg="#4caf50", fg="white", width=10)
        self.guess_btn.pack(pady=5)

        self.feedback_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f0f4f8")
        self.feedback_label.pack(pady=10)

        self.attempts_label = tk.Label(root, text="Attempts: 0", font=("Arial", 10), bg="#f0f4f8")
        self.attempts_label.pack(pady=5)

        self.reset_btn = tk.Button(root, text="Restart", font=("Arial", 10), command=self.reset_game, bg="#2196f3", fg="white", width=8)
        self.reset_btn.pack(pady=5)

    def check_guess(self):
        guess = self.entry.get()
        if not guess.isdigit():
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")
            return
        guess = int(guess)
        result = self.game.guess(guess)
        self.attempts_label.config(text=f"Attempts: {self.game.attempts}")
        self.feedback_label.config(text=self.game.last_feedback)
        if result == "correct":
            messagebox.showinfo("Congratulations!", self.game.last_feedback)
            self.guess_btn.config(state="disabled")
        self.entry.delete(0, tk.END)

    def reset_game(self):
        self.game.reset_game()
        self.feedback_label.config(text="")
        self.attempts_label.config(text="Attempts: 0")
        self.guess_btn.config(state="normal")
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingApp(root)
    root.mainloop()