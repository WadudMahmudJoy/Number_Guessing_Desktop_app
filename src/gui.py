import tkinter as tk
from tkinter import messagebox
from logic import NumberGuessingGame
import winsound
import random
import os

class NumberGuessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("500x450")
        self.root.resizable(False, False)
        self.game = NumberGuessingGame()

        # Set background color only (no image, no error message)
        self.root.configure(bg="#232946")

        # Overlay for widgets
        self.overlay = tk.Frame(self.root, bg="#232946", bd=0)
        self.overlay.place(x=30, y=20, width=440, height=400)

        # Title
        self.title_label = tk.Label(self.overlay, text="🎲 Guess the Number! 🎲", font=("Comic Sans MS", 22, "bold"), bg="#232946", fg="#f9d923")
        self.title_label.pack(pady=(10, 8))

        # Info
        self.info_label = tk.Label(self.overlay, text=f"Guess a number between {self.game.min_num} and {self.game.max_num}", font=("Arial", 13), bg="#232946", fg="#eebbc3")
        self.info_label.pack(pady=2)

        # Entry
        self.entry = tk.Entry(self.overlay, font=("Arial", 16), justify="center", width=10, bg="#f7f7f7", fg="#232946", relief="solid", bd=2)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", lambda event: self.check_guess())

        # Guess Button
        self.guess_btn = tk.Button(self.overlay, text="Guess", font=("Arial", 13, "bold"), command=self.check_guess, bg="#21e6c1", fg="#232946", width=12, relief="raised", bd=3, activebackground="#278ea5")
        self.guess_btn.pack(pady=5)

        # Feedback
        self.feedback_label = tk.Label(self.overlay, text="", font=("Arial", 14, "bold"), bg="#232946", fg="#f6f6f6")
        self.feedback_label.pack(pady=10)

        # Attempts
        self.attempts_label = tk.Label(self.overlay, text="Attempts: 0", font=("Arial", 11), bg="#232946", fg="#eebbc3")
        self.attempts_label.pack(pady=2)

        # Hint Button
        self.hint_btn = tk.Button(self.overlay, text="Hint", font=("Arial", 11, "bold"), command=self.show_hint, bg="#f9d923", fg="#232946", width=8, relief="groove", bd=2, activebackground="#f7f7f7")
        self.hint_btn.pack(pady=5)

        # Reset Button
        self.reset_btn = tk.Button(self.overlay, text="Restart", font=("Arial", 11), command=self.reset_game, bg="#278ea5", fg="#f7f7f7", width=8, relief="groove", bd=2, activebackground="#21e6c1")
        self.reset_btn.pack(pady=5)

        # Hint label
        self.hint_label = tk.Label(self.overlay, text="", font=("Arial", 11, "italic"), bg="#232946", fg="#f9d923")
        self.hint_label.pack(pady=5)

        # Animation label (hidden by default)
        self.anim_label = tk.Label(self.overlay, text="🎉", font=("Arial", 40), bg="#232946", fg="#f9d923")
        self.anim_label.pack(pady=5)
        self.anim_label.place_forget()

    def play_sound(self, correct=False):
        if correct:
            winsound.MessageBeep(winsound.MB_ICONASTERISK)
        else:
            winsound.MessageBeep(winsound.MB_ICONHAND)

    def animate_correct(self):
        # Show animation label and flash it a few times
        def flash(count=0):
            if count >= 6:
                self.anim_label.place_forget()
                return
            if count % 2 == 0:
                self.anim_label.config(text="🎉", fg="#f9d923")
                self.anim_label.place(relx=0.5, rely=0.7, anchor="center")
            else:
                self.anim_label.place_forget()
            self.root.after(200, lambda: flash(count+1))
        flash()

    def check_guess(self):
        guess = self.entry.get()
        if not guess.isdigit():
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")
            self.play_sound(False)
            return
        guess = int(guess)
        result = self.game.guess(guess)
        self.attempts_label.config(text=f"Attempts: {self.game.attempts}")
        self.feedback_label.config(text=self.game.last_feedback)
        if result == "correct":
            self.play_sound(True)
            self.animate_correct()
            messagebox.showinfo("Congratulations!", self.game.last_feedback)
            self.guess_btn.config(state="disabled")
        else:
            self.play_sound(False)
        self.entry.delete(0, tk.END)

    def show_hint(self):
        # Give a hint: is the number even/odd or in a range
        target = self.game.target
        hint_type = random.choice(["parity", "range"])
        if hint_type == "parity":
            parity = "even" if target % 2 == 0 else "odd"
            self.hint_label.config(text=f"Hint: The number is {parity}.")
        else:
            # Give a range of +/- 10
            low = max(self.game.min_num, target - 10)
            high = min(self.game.max_num, target + 10)
            self.hint_label.config(text=f"Hint: The number is between {low} and {high}.")

    def reset_game(self):
        self.game.reset_game()
        self.feedback_label.config(text="")
        self.attempts_label.config(text="Attempts: 0")
        self.guess_btn.config(state="normal")
        self.entry.delete(0, tk.END)
        self.hint_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingApp(root)
    root.mainloop()