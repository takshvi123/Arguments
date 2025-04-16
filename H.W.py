from tkinter import Tk, Button, Label, Entry, messagebox
from tkinter.ttk import Progressbar
import time
from playsound import playsound  # Install using: pip install playsound

# Countdown function for shutdown with dynamic interactivity
def countdown(seconds):
    countdown_window = Tk()
    countdown_window.title("Countdown Timer ⏳")
    countdown_window.geometry("400x200")
    countdown_window.configure(bg="#FFE4B5")

    Label(
        countdown_window,
        text="System shutdown is about to begin...",
        font=("Helvetica", 14, "bold"),
        bg="#FFE4B5",
        fg="darkred"
    ).pack(pady=20)

    progress = Progressbar(countdown_window, orient="horizontal", length=300, mode="determinate")
    progress.pack(pady=20)
    progress["maximum"] = seconds

    for i in range(seconds):
        progress["value"] = i + 1
        countdown_window.update()
        time.sleep(1)

    Label(
        countdown_window,
        text="Goodbye! Shutting down now... 👋",
        font=("Helvetica", 14, "bold"),
        bg="#FFE4B5",
        fg="darkblue"
    ).pack(pady=20)

    # Trigger final message with a sound effect
    countdown_window.after(1000, lambda: playsound("shutdown_sound.mp3"))
    countdown_window.after(3000, countdown_window.destroy)
    countdown_window.mainloop()

# Function to simulate shutdown
def shutdown():
    shutdown_window = Tk()
    shutdown_window.title("Shutdown Confirmation 🔒")
    shutdown_window.geometry("600x400")
    shutdown_window.configure(bg="#FFDDC1")

    Label(
        shutdown_window,
        text="🚨 Are you sure you want to shut down? 🚨",
        font=("Arial", 24, "bold"),
        bg="#FFDDC1",
        fg="red"
    ).pack(pady=50)

    def confirm_shutdown():
        Label(
            shutdown_window,
            text="🔌 Initiating shutdown process...",
            font=("Arial", 18),
            bg="#FFDDC1",
            fg="green"
        ).pack(pady=20)

        playsound("shutdown_sound.mp3")  # Ensure you have the file in your directory
        shutdown_window.destroy()
        countdown(10)

    def cancel_shutdown():
        Label(
            shutdown_window,
            text="✅ Shutdown canceled! Returning to main menu...",
            font=("Arial", 18),
            bg="#FFDDC1",
            fg="blue"
        ).pack(pady=20)

        playsound("cancel_sound.mp3")  # Ensure you have the file in your directory
        shutdown_window.after(2000, shutdown_window.destroy)

    Button(
        shutdown_window,
        text="✔ Confirm Shutdown",
        font=("Arial", 18, "bold"),
        bg="red",
        fg="white",
        command=confirm_shutdown
    ).pack(pady=30)

    Button(
        shutdown_window,
        text="❌ Cancel Shutdown",
        font=("Arial", 18, "bold"),
        bg="green",
        fg="white",
        command=cancel_shutdown
    ).pack(pady=30)

    shutdown_window.mainloop()

# Function for feedback
def feedback():
    feedback_window = Tk()
    feedback_window.title("Feedback 🌟")
    feedback_window.geometry("600x400")
    feedback_window.configure(bg="#D5F3FE")

    Label(
        feedback_window,
        text="We value your feedback! 🌟",
        font=("Helvetica", 24, "bold"),
        bg="#D5F3FE",
        fg="purple"
    ).pack(pady=50)

    feedback_entry = Entry(feedback_window, width=50)
    feedback_entry.pack(pady=20)

    def submit_feedback():
        user_feedback = feedback_entry.get().strip()
        if not user_feedback:
            messagebox.showerror("Error", "Feedback cannot be empty!")
            return
        Label(
            feedback_window,
            text=f"Thank you for your feedback: '{user_feedback}' 💖",
            font=("Helvetica", 18),
            bg="#D5F3FE",
            fg="blue"
        ).pack(pady=30)

    Button(
        feedback_window,
        text="Submit Feedback",
        font=("Arial", 18, "bold"),
        bg="orange",
        fg="white",
        command=submit_feedback
    ).pack(pady=20)

    feedback_window.mainloop()

# Main application menu
def main_menu():
    app = Tk()
    app.title("System Shutdown Simulator 🚀")
    app.geometry("800x600")
    app.configure(bg="#D5F3FE")

    Label(
        app,
        text="✨ Welcome to the System Shutdown Simulator ✨",
        font=("Helvetica", 32, "bold"),
        bg="#D5F3FE",
        fg="darkblue"
    ).pack(pady=50)

    Label(
        app,
        text="Select an option below to proceed:",
        font=("Helvetica", 18),
        bg="#D5F3FE"
    ).pack(pady=20)

    Button(
        app,
        text="🔴 Shutdown",
        font=("Arial", 24, "bold"),
        bg="red",
        fg="white",
        command=shutdown
    ).pack(pady=30)

    Button(
        app,
        text="💬 Feedback",
        font=("Arial", 24, "bold"),
        bg="blue",
        fg="white",
        command=feedback
    ).pack(pady=20)

    Button(
        app,
        text="❌ Exit",
        font=("Arial", 24, "bold"),
        bg="black",
        fg="white",
        command=app.quit
    ).pack(pady=30)

    app.mainloop()

# Run the main menu
main_menu()