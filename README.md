# Rock, Paper, Scissors - GUI Game

## Overview

![preview](https://github.com/user-attachments/assets/f275d6bf-9bd7-4863-b00f-d51ad8badbe8)

This is a simple Rock, Paper, Scissors game with a fun graphical user interface (GUI) built using Python's tkinter library. It includes animations and sound effects to make the classic game more interactive. You can choose between rock, paper, or scissors, and the computer will randomly select its move. The game will announce whether you won, lost, or tied!

## Why This Project?

I created this project out of a mix of boredom and inspiration from my students at **Code First Girls**, where I teach Python. Their enthusiasm motivated me to build a fun, fully functional application that demonstrates the power of Python and `tkinter`. Why not combine learning with a bit of fun?

## How It Works

The game is built with a clean and modular framework for easy understanding and maintenance. Here's an overview of the workflow:

![Game Workflow Diagram](https://github.com/hawra-nawi/Rock_Paper_Scissors/blob/main/Game%20Function%20Workflow/Image/workflow.png)

### Framework Overview:
1. **Game Setup:**
   - Initialize the GUI using `tkinter`, and set up the main window.
   - Load animations (GIFs) and sound effects to enhance user experience.

2. **Gameplay:**
   - The game presents a welcome screen followed by a choice screen where the user selects rock, paper, or scissors.
   - The computer randomly selects its move, and the result is determined based on traditional game rules.

3. **Results:**
   - The result screen displays the choices of both the player and the computer with animations and sound effects for winning, losing, or tying.
   - Users can choose to play again or exit.

For more detailed workflow documentation, [click here](https://github.com/hawra-nawi/Rock_Paper_Scissors/blob/main/Game%20Function%20Workflow/Rock%2C%20Paper%2C%20Scissors%20Game%20-%20Function%20Workflow.pdf).

### File Structure
- **[GIF](https://github.com/hawra-nawi/Rock_Paper_Scissors/tree/main/GIF)**: Contains the animated GIFs for rock, paper, and scissors.
- **[Sound_Effects](https://github.com/hawra-nawi/Rock_Paper_Scissors/tree/main/Sound_Effects)**: Contains the sound effects for win, lose, and tie outcomes.
- **[Main Python Script](https://github.com/hawra-nawi/Rock_Paper_Scissors/blob/main/rock_paper_scissors.py)**: The main game logic is within the Python script, structured to handle the game loop, animations, and result display.

### Code Structure:
The code is divided into well-documented functions, including:
- `show_welcome_screen()`: Displays the welcome screen.
- `show_choice_screen()`: Allows the user to select their choice (rock, paper, or scissors).
- `play_game(user_choice)`: Determines the computer’s choice, calculates the result, and triggers sound effects.
- `show_result_screen()`: Displays the result with animations for both player and computer choices.
- `load_and_resize_gif_frames()`: Handles GIF resizing for animations.
- `animate_gif()`: Animates the GIFs in a loop using tkinter's `after()` function.

## How to Run
1. Clone the repository and navigate to the project folder.
2. Ensure the required libraries are installed:
   - `tkinter`
   - `PIL` (Pillow for image processing)
   - `pygame` (for sound effects)
3. Run the main Python script:
   ```bash
   python rock_paper_scissors.py
   ```

## Open to Suggestions!
This was a fun project, and I'm open to hearing any ideas or suggestions on how to improve it! Feel free to reach out with your feedback or thoughts via LinkedIn (link).

Enjoy the game!
