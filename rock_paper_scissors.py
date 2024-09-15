### Rock, Paper, Scissors ###

# The aim of this script is to create Rock, Paper, Scissors game through GUI (Graphic User Interface)

## 1. Importing the Libraries
# tkinter: Provides the GUI components
import tkinter as tk
# random: To generate random choices.
import random
# pygame: Used for handling sound effects.
import pygame
# PIL (Pillow): For image processing (e.g., resizing).
from PIL import Image, ImageTk

## 2. Initialize pygame for sound effects
pygame.mixer.init()

# Load Sound Effects
win_sound = pygame.mixer.Sound("Sound_Effects/winner.mpeg.wav")
lose_sound = pygame.mixer.Sound("Sound_Effects/lose.mpeg.wav")
tie_sound = pygame.mixer.Sound("Sound_Effects/tie_1.wav")

## 3. Set up Main Window
# Creates the main window.
root = tk.Tk()
# Sets the window size to 600x400 pixels (width x height).
root.geometry("600x400")
# Background colour
root.configure(bg="dark slate blue")

## 4. Load and Resize GIF Frames for Animation
# This function's purpose is to load a GIF file, resize each frame to a specified width and height, and return a list of the resized frames.
def load_and_resize_gif_frames(image_path, width, height):
    # Open the GIF file using the PIL library
    # A GIF can contain multiple frames, and this command allows us to access and manipulate each frame individually.
    gif = Image.open(image_path)
    # Initialize an empty list to store each frame of the GIF
    frames = []
    try:
        # Start an infinite loop to process each frame of the GIF, since GIFs can have multiple frames, we need to process each one.
        while True:
            # resizes the current frame to the specified dimensions
            # `Image.ANTIALIAS` ensures that the resized image maintains good quality by smoothing out edges, which is especially useful when scaling images down.
            resized_frame = gif.copy().resize((width, height), Image.ANTIALIAS)  # Resize frame
            # After resizing the frame, we convert it into a format that tkinter can use to display the image (ImageTk.PhotoImage())
            # This converted frame is appended to the frames list
            frames.append(ImageTk.PhotoImage(resized_frame))
            # The seek() method moves to the next frame in the GIF.
            # The argument len(frames) tells the program to move to the frame number that corresponds to how many frames have already been processed.
            # For example, when the first frame has been processed (len(frames) == 1), it seeks to the second frame, and so on.
            gif.seek(len(frames))  # Go to the next frame
    # This handles the end of the GIF file. When the seek() function tries to move beyond the last frame, it raises an EOFError (end of file error).
    # The except block catches this error, effectively stopping the loop once all frames have been processed.
    except EOFError:
        pass  # End of GIF
    # After all frames have been processed, we return the frames list containing the resized images.
    return frames


## 5. Animate GIFs in Labels
# The animate_gif function is responsible for creating the animation effect by cycling through the frames of the GIF at a set interval.
# It takes a label widget (where the animation will be displayed), a list of gif_frames, and a delay to control the speed of the animation.
def animate_gif(label, gif_frames, delay):
    # This defines an inner function update_gif that takes an index parameter.
    # The index refers to which frame in the gif_frames list we want to display.
    def update_gif(index):
        # This command retrieves the current frame from the gif_frames list using the index.
        # The index determines which frame to display next.
        frame = gif_frames[index]
        # This updates the label's displayed image to the current frame.
        # The label is the widget where the GIF animation is shown.
        label.config(image=frame)
        # This command ensures that the frame is referenced in the widget to prevent Python's garbage collector from deleting the frame image.
        # Without this line, the animation may fail or display blank frames because the frames could be removed from memory after display.
        label.image = frame

        # Schedule the next frame update
        # This updates the index to move to the next frame.
        # The % len(gif_frames) ensures that the index loops back to the start (index 0) when it reaches the end of the list, creating an infinite loop of frames.
        index = (index + 1) % len(gif_frames)
        # The `root.after()` function is used to schedule when the update_gif() function should run next.
        # The `delay` is the number of milliseconds to wait before calling the function again (e.g., 100 milliseconds).
        # This creates the animation effect by repeatedly changing the displayed frame at regular intervals.
        root.after(delay, update_gif, index)

    # This initiates the animation by calling update_gif() with the first frame (index 0).
    # From there, the function will keep calling itself (via root.after()) to update the frames.
    update_gif(0)  # Start the animation


## 6. Welcome screen
# show_welcome_screen(): Clears previous widgets and displays a welcome label and a "Next" button.
# welcome_label: Shows the text "WELCOME!" with a font size of 24, white text on a light blue background.
# next_button: Button that changes colour when hovered over and leads to the choice screen.
def show_welcome_screen():
    # root.winfo_children() retrieves a list of all widgets currently in the 'root' window.
    for widget in root.winfo_children():
        # widget.destroy() removes each widget from the window.
        # This ensures that the welcome screen starts fresh without any previous widgets.
        widget.destroy()

    # Creating a "Welcome to..." Label title
    welcome_label = tk.Label(root, text="Welcome to...", font=("Helvetica", 30), bg="dark slate blue", fg="white")
    # Places the label in the window and adds vertical padding of 20 pixels above and below the label.
    welcome_label.pack(pady=20)

    # Create and Configure Next Button
    next_button = tk.Button(root, text="Next", bg="white", fg="black", command=show_choice_screen)
    next_button.pack(pady=10)


## 7. Choice Screen
def show_choice_screen():
    # Again, clears previous widgets and displays the choice screen.
    for widget in root.winfo_children():
        widget.destroy()

    # Creating label title "Rock, Paper, Scissors!"
    title_label = tk.Label(root, text="Rock, Paper, Scissors!", font=("Helvetica", 30), bg="dark slate blue", fg="white")
    title_label.pack(pady=10)

    # Adding the next text "Choose your weapon:"
    pick_label = tk.Label(root, text="Choose your weapon:", font=("Helvetica", 18), bg="dark slate blue", fg="white")
    pick_label.pack(pady=5)

    # A Frame widget is created to contain the buttons (to display the gifs).
    # The frame is packed with vertical padding of 20 pixels to separate it from other elements.
    button_frame = tk.Frame(root, bg="dark slate blue")
    button_frame.pack(pady=20)

    # Load GIF frames for animation (resized to 100x100)
    rock_gif_frames = load_and_resize_gif_frames("GIF/rock.gif", 100, 100)
    paper_gif_frames = load_and_resize_gif_frames("GIF/paper.gif", 100, 100)
    scissors_gif_frames = load_and_resize_gif_frames("GIF/scissors.gif", 100, 100)

    # Create and animate Rock button (that is added to the button_frame)
    rock_label = tk.Label(button_frame, bg="dark slate blue")
    rock_label.pack(side="left", padx=20)
    animate_gif(rock_label, rock_gif_frames, 100)  # Animate at 100ms delay

    # Create and animate Paper button (that is added to the button_frame)
    paper_label = tk.Label(button_frame, bg="dark slate blue")
    # The button is packed into the button_frame with horizontal padding of 20 pixels.
    paper_label.pack(side="left", padx=10)
    # Animate at 100ms delay
    animate_gif(paper_label, paper_gif_frames, 100)

    # Create and animate Scissors button (that is added to the button_frame)
    scissors_label = tk.Label(button_frame, bg="dark slate blue")
    scissors_label.pack(side="left", padx=10)
    animate_gif(scissors_label, scissors_gif_frames, 100)

    # Buttons for user input (Rock, Paper, Scissors) - user will have select either rock, paper, scissors button
    button_frame = tk.Frame(root, bg="dark slate blue")
    button_frame.pack(pady=20)

    # When this button is clicked, it calls the play_game("rock")
    rock_button = tk.Button(button_frame, text="Rock", command=lambda: play_game("rock"))
    rock_button.pack(side="left", padx=20)

    # When this button is clicked, it calls the play_game("paper")
    paper_button = tk.Button(button_frame, text="Paper", command=lambda: play_game("paper"))
    paper_button.pack(side="left", padx=20)

    # When this button is clicked, it calls the play_game("scissors")
    scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play_game("scissors"))
    scissors_button.pack(side="left", padx=20)

## 8. Game Logic
# The aim to determine the computer's choice, checks the results, plays the corresponding sound, and shows the resul screen
# With play_game() takes the user's choice
def play_game(user_choice):
    # choices for both user and computer
    choices = ["rock", "paper", "scissors"]
    # the computer will pick a random choice of rock, paper, scissors (whereas the user can choose)
    computer_choice = random.choice(choices)

    #  The function `determine_winner()` is called with user_choice and computer_choice as arguments to determine the result of the game (win, lose, or tie).
    result = determine_winner(user_choice, computer_choice)

    # Play sound effects based on the result
    if result == "win":
        win_sound.play()
    elif result == "lose":
        lose_sound.play()
    else:
        tie_sound.play()

    # Show the result screen with the outcome and choices
    show_result_screen(result, user_choice, computer_choice)


## 9. Result Logic
# The aim is to determines the result based on the user's and computer's choices.
# determine_winner passing argument value are (user_choice, computer_choice) in the form of (user, computer)
def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
            (user == "paper" and computer == "rock") or \
            (user == "scissors" and computer == "paper"):
        return "win"
    else:
        return "lose"


## 10. Result Screen with properly aligned gifs, VS label, and buttons
# This function displays the result screen, showing the user's choice, computer's choice, and the result
def show_result_screen(result, user_choice, computer_choice):
    # Again, clears previous widgets and displays the result of the game.
    for widget in root.winfo_children():
        widget.destroy()

    # Create a Label, determine the result message based on the game outcome
    result_text = "You Win!" if result == "win" else "You Lose!" if result == "lose" else "It's a Tie!"
    result_label = tk.Label(root, text=result_text, font=("Helvetica", 30), bg="dark slate blue", fg="white")
    result_label.pack(pady=20)

    # Create a frame to hold the result images and "VS" label
    result_frame = tk.Frame(root, bg="dark slate blue")
    result_frame.pack(pady=30)

    # Load and resize the GIFs for both user's and computer's choices to 100x100
    user_gif_frames = load_and_resize_gif_frames(f"GIF/{user_choice}.gif", 100, 100)
    computer_gif_frames = load_and_resize_gif_frames(f"GIF/{computer_choice}.gif", 100, 100)

    # Display user's choice with animation
    user_label = tk.Label(result_frame, bg="dark slate blue")
    user_label.pack(side="left", padx=30)
    animate_gif(user_label, user_gif_frames, 100)

    # Display "VS" label between user and computer choices
    vs_label = tk.Label(result_frame, text="VS", font=("Helvetica", 18, "bold"), bg="dark slate blue", fg="white")
    vs_label.pack(side="left", padx=20)

    # Display computer's choice with animation
    computer_label = tk.Label(result_frame, bg="dark slate blue")
    computer_label.pack(side="left", padx=30)
    animate_gif(computer_label, computer_gif_frames, 100)

    # Create a frame for the buttons below the result
    button_frame = tk.Frame(root, bg="dark slate blue")
    button_frame.pack(pady=20)

    # Create and place the "Play Again" button
    play_again_button = tk.Button(button_frame, text="Play Again", font=("Helvetica", 18), command=show_choice_screen, bg="white", fg="black")
    play_again_button.pack(side="left", padx=10)

    # Create and place the "Exit" button
    exit_button = tk.Button(button_frame, text="Exit", font=("Helvetica", 18), command=root.quit, bg="white",fg="black")
    exit_button.pack(side="left", padx=10)


# Start the game
show_welcome_screen()
root.mainloop()
