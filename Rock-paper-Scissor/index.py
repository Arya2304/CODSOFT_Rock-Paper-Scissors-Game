import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
        (user_choice == "Scissors" and computer_choice == "Paper") or \
        (user_choice == "Paper" and computer_choice == "Rock"):
        return "User"
    else:
        return "Computer"

# Function to handle user choice
def user_choice(choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(choice, computer_choice)
    
    if result == "User":
        user_score.set(user_score.get() + 1)
        messagebox.showinfo("Result", f"You chose {choice}, Computer chose {computer_choice}. You win! 😊")
    elif result == "Computer":
        computer_score.set(computer_score.get() + 1)
        messagebox.showinfo("Result", f"You chose {choice}, Computer chose {computer_choice}. You lose! 😢")
    else:
        messagebox.showinfo("Result", f"You chose {choice}, Computer chose {computer_choice}. It's a tie! 😐")
    
    play_again = messagebox.askyesno("Play Again", "Do you want to play another round?")
    if not play_again:
        root.destroy()

# Function to create the main window
def create_main_window():
    global root, user_score, computer_score
    
    root = ctk.CTk()
    root.title("Rock-Paper-Scissors Game")
    root.geometry("500x300")

    ctk.CTkLabel(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 16)).pack(pady=20)

    user_score = ctk.IntVar(value=0)
    computer_score = ctk.IntVar(value=0)
    
    frame = ctk.CTkFrame(root)
    frame.pack(pady=10)
    
    rock_button = ctk.CTkButton(frame, text="Rock ✊", command=lambda: user_choice("Rock"))
    rock_button.grid(row=0, column=0, padx=10)
    
    paper_button = ctk.CTkButton(frame, text="Paper ✋", command=lambda: user_choice("Paper"))
    paper_button.grid(row=0, column=1, padx=10)
    
    scissors_button = ctk.CTkButton(frame, text="Scissors ✌️", command=lambda: user_choice("Scissors"))
    scissors_button.grid(row=0, column=2, padx=10)
    
    score_frame = ctk.CTkFrame(root)
    score_frame.pack(pady=20)
    
    ctk.CTkLabel(score_frame, text="User Score:").grid(row=0, column=0, padx=10)
    ctk.CTkLabel(score_frame, textvariable=user_score).grid(row=0, column=1, padx=10)
    
    ctk.CTkLabel(score_frame, text="Computer Score:").grid(row=0, column=2, padx=10)
    ctk.CTkLabel(score_frame, textvariable=computer_score).grid(row=0, column=3, padx=10)
    
    root.mainloop()

# Run the main window
create_main_window()
