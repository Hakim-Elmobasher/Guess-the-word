import random
import tkinter as tk
from tkinter import messagebox

# Function to handle guessing
def check_guess():
    global attempts
    guess = guess_entry.get().lower()  # Get the user input from the entry box
    guess_entry.delete(0, tk.END)  # Clear the input field

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guess_word[i] = guess
        word_label.config(text=' '.join(guess_word))
        if '_' not in guess_word:
            messagebox.showinfo('Congratulations!', f'You guessed the word: {word}')
            root.quit()
    else:
        attempts -= 1
        attempts_label.config(text=f'Attempts left: {attempts}')
        draw_hangman()  # Update the hangman figure

        if attempts > 0:
            shake_hangman()  # Shake the hangman after a wrong guess
        if attempts == 0:
            animate_hangman_death()  # Hangman "dies" after final wrong guess
            messagebox.showinfo('Game Over', f'You\'ve been hanged! The word was: {word}')
            root.quit()

# Function to draw the hangman parts progressively
def draw_hangman():
    if attempts == 5:
        canvas.create_line(100, 250, 100, 50)  # Vertical pole
    elif attempts == 4:
        canvas.create_line(100, 50, 200, 50)  # Top horizontal pole
    elif attempts == 3:
        canvas.create_line(200, 50, 200, 80)  # Rope
    elif attempts == 2:
        canvas.create_oval(180, 80, 220, 120, tag="head")  # Head
    elif attempts == 1:
        canvas.create_line(200, 120, 200, 180, tag="body")  # Body
    elif attempts == 0:
        canvas.create_line(200, 130, 180, 160, tag="left_arm")  # Left arm
        canvas.create_line(200, 130, 220, 160, tag="right_arm")  # Right arm
        canvas.create_line(200, 180, 180, 210, tag="left_leg")  # Left leg
        canvas.create_line(200, 180, 220, 210, tag="right_leg")  # Right leg

# Function to animate the hangman shaking after a wrong guess
def shake_hangman():
    def shake():
        canvas.move("head", -5, 0)
        root.after(100, lambda: canvas.move("head", 10, 0))
        root.after(200, lambda: canvas.move("head", -5, 0))

    shake()

# Function to animate hangman's "death" when the player loses
def animate_hangman_death():
    def struggle():
        canvas.move("body", 0, -5)
        root.after(100, lambda: canvas.move("body", 0, 5))
        canvas.create_line(180, 100, 220, 100, fill="red")  # Cross eyes
        canvas.create_line(180, 100, 220, 120, fill="red")  # Cross eyes

    struggle()

# Function to animate blinking eyes
def blink_eyes():
    # Create eyes
    eye_left = canvas.create_oval(190, 90, 195, 95, fill="black", tag="eye_left")
    eye_right = canvas.create_oval(205, 90, 210, 95, fill="black", tag="eye_right")

    def blink():
        # Close the eyes
        canvas.itemconfig(eye_left, state='hidden')
        canvas.itemconfig(eye_right, state='hidden')
        root.after(200, open_eyes)  # After 200ms, open eyes again

    def open_eyes():
        # Open the eyes
        canvas.itemconfig(eye_left, state='normal')
        canvas.itemconfig(eye_right, state='normal')

    # Randomly blink every few seconds
    root.after(random.randint(2000, 5000), blink)

# Initialize the game variables
word_bank = ['Ponder', 'Zephyr', 'Cascade', 'Prism', 'Orbit', 'Velvet', 'rizz', 'ohio', 'sigma', 'tiktok', 'skibidi'] 
word = random.choice(word_bank).lower()
guess_word = ['_'] * len(word)
attempts = 6  # Number of incorrect guesses before losing

# Setup Tkinter window
root = tk.Tk()
root.title("Interactive Animated Hangman")

# Create and place widgets
word_label = tk.Label(root, text=' '.join(guess_word), font=('Helvetica', 20))
word_label.pack(pady=10)

attempts_label = tk.Label(root, text=f'Attempts left: {attempts}', font=('Helvetica', 16))
attempts_label.pack(pady=10)

guess_entry = tk.Entry(root, font=('Helvetica', 16), width=5)
guess_entry.pack(pady=10)

submit_button = tk.Button(root, text="Submit", font=('Helvetica', 16), command=check_guess)
submit_button.pack(pady=10)

# Create a canvas to draw the hangman
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

# Start eye blinking animation
blink_eyes()

# Run the application
root.mainloop()
