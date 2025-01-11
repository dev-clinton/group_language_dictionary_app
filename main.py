"""This is the group main.py code for all dictionary and our primary colours were
red and green (for the exit and search buttons) and purple for the main G.U.I"""

from tkinter import *

from spanish import spanish_dictionary_app  # Import Spanish dictionary
from Igbo_dictionary import igbo_dictionary_app  # Import igbo dictionary
from Idoma_Dictionary import idoma_dictionary_app # Import idoma dictionary
from yoruba import yoruba_app  # Import Yoruba dictionary
from japanese import japanese_app  # Import Japanese dictionary


def main():
    # Create the main window
    window = Tk()
    window.title("Multilingual Dictionary")
    window.geometry("600x550")
    window.config(bg="#f5f5f5")  # Light background color

    # Center the window on the screen
    window.eval('tk::PlaceWindow . center')

    # Add a title label
    title_label = Label(window, text="Multilingual Dictionary", font=("Arial", 25, "bold"), bg="#f5f5f5", fg= "black")
    title_label.pack(pady=20)

    # Add a subtitle
    subtitle_label = Label(window, text="Select a dictionary to Explore!", font=("Arial", 14), bg="#f5f5f5", fg="black")
    subtitle_label.pack(pady=10)

    # Feedback label for user guidance
    feedback_label = Label(window, text="", font=("Arial", 12), bg="#f5f5f5", fg="red")
    feedback_label.pack(pady=10)

    # Function to handle opening a dictionary
    def open_dictionary(dictionary_app, name):
        try:
            feedback_label.config(text=f"Opening {name} Dictionary...")
            window.withdraw()  # Hide the main window
            dictionary_app()  # Open the chosen dictionary
            window.deiconify()  # Show the main window again
        except Exception as e:
            feedback_label.config(text=f"Error: {e}")

    # Buttons for dictionaries
    Button(window, text="Spanish Dictionary", font=("Arial", 14), bg="#4b0082", fg="white", width=25,
           command=lambda: open_dictionary(spanish_dictionary_app, "Spanish")).pack(pady=10)

    Button(window, text="Igbo Dictionary", font=("Arial", 14), bg="#4b0082", fg="white", width=25,
           command=lambda: open_dictionary(igbo_dictionary_app, "Igbo")).pack(pady=10)

    Button(window, text="Yoruba Dictionary", font=("Arial", 14), bg="#4b0082", fg="white", width=25,
           command=lambda: open_dictionary(yoruba_app, "Yoruba")).pack(pady=10)

    Button(window, text="Idoma Dictionary", font=("Arial", 14), bg="#4b0082", fg="white", width=25,
           command=lambda: open_dictionary(idoma_dictionary_app, "Idoma")).pack(pady=10)

    Button(window, text="Japanese Dictionary", font=("Arial", 14), bg="#4b0082", fg="white", width=25,
           command=lambda: open_dictionary(japanese_app, "Japanese")).pack(pady=10)

    # Add an exit button
    Button(window, text="Exit", font=("Arial", 14), bg="#dc143c", fg="white", width=25, command=window.destroy).pack(pady=20)

    # Start the main loop
    window.mainloop()


if __name__ == "__main__":
    main()
