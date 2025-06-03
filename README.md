# Number Guessing Desktop App

A simple and interactive number guessing game built with Python and Tkinter.

## Overview
This project is a desktop application that challenges users to guess a randomly generated number within a specified range. The app provides instant feedback on each guess, tracks the number of attempts, and offers a clean, user-friendly interface. It is ideal for beginners learning Python GUI development or anyone looking for a fun, simple game.

## Features
- **Graphical User Interface:** Built with Tkinter for a modern and intuitive experience.
- **Random Number Generation:** The game selects a random number within a configurable range.
- **Input Validation:** Ensures only valid numbers are accepted as guesses.
- **Feedback System:** Tells the user if their guess is too high, too low, or correct.
- **Attempts Counter:** Displays the number of guesses made.
- **Restart Option:** Allows the user to reset the game and play again.
- **Modular Code:** Game logic and GUI are separated for clarity and maintainability.

## How It Works
1. When the app starts, it randomly selects a number within a preset range (e.g., 1 to 100).
2. The user enters their guess in the input field and clicks the "Guess" button (or presses Enter).
3. The app checks the guess and provides feedback:
   - If the guess is too high or too low, the user is prompted to try again.
   - If the guess is correct, a congratulatory message is displayed and the game can be restarted.
4. The number of attempts is updated after each guess.
5. The user can click "Restart" at any time to start a new game with a new random number.

## Prerequisites
- **Python 3.x** (Download from [python.org](https://www.python.org/downloads/))
- **Tkinter** (Included with most Python installations)

## Installation & Running
1. **Clone or Download the Repository**
   - Download the ZIP or use Git to clone the project.
2. **Install Dependencies**
   - Tkinter is included by default. If you need additional packages, install them with:
     ```bash
     pip install -r requirements.txt
     ```
3. **Run the Application**
   - Open a terminal/command prompt in the project directory.
   - Run:
     ```bash
     python src/gui.py
     ```

## File Structure
```
number-guessing-desktop-app/
├── src/
│   ├── gui.py         # Main GUI application
│   ├── logic.py       # Game logic
│   └── main.py        # (Optional) Entry point
├── requirements.txt   # Python dependencies
├── README.md          # Project documentation
└── num_guess_d_app.py # (Unused/legacy)
```

## Customization
- You can change the guessing range by editing the `min_num` and `max_num` values in `logic.py`.
- The GUI appearance (colors, fonts, window size) can be customized in `gui.py`.

## Educational Value
This project demonstrates:
- Basic Python programming
- GUI development with Tkinter
- Modular code organization
- User input validation and feedback

## Screenshots
![Screenshot](screenshot.png)

## License
This project is for educational purposes.