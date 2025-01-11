from tkinter import Tk, Entry, Label, Button, StringVar, Toplevel


def yoruba_app():
    # Create the main application window
    window = Toplevel()
    window.title("Yoruba Dictionary")
    window.geometry("400x300")
    window.configure(bg="#f7f7f7")  # Light gray background

    # Yoruba dictionary data
    yoruba_dictionary = {
        "Ase": "Amen",
        "Ope": "Peace",
        "Ayo": "Joy",
        "Oshe": "Thanks",
        "Abi": "Is it?",
        "Oro": "Voice",
        "Lo": "Go",
        "Wa": "Come",
        "Ka": "Stay",
        "Ore": "Friend",
        "Baba": "Father",
        "Iya": "Mother",
        "Aburo": "Younger sibling",
        "Egbon": "Older sibling",
        "Ojo": "Day",
        "Aiku": "Night",
        "Ona": "Road",
        "Ile": "House",
        "Oko": "Farm",
        "Eja": "Fish"
    }

    # Search function with case-insensitivity
    def search_word():
        word = entry_text.get().strip().lower()  # Normalize user input
        if word in (key.lower() for key in yoruba_dictionary.keys()):  # Check if input matches any key
            result.set(f"Meaning: {yoruba_dictionary[word.capitalize()]}")
        else:
            result.set("Word Not Found in Yoruba Dictionary")

    # Title label
    title_label = Label(window, text="Yoruba Dictionary", font=("Arial", 18, "bold"), bg="#f7f7f7", fg="brown")
    title_label.pack(pady=10)

    # Entry box for user input
    entry_text = StringVar()
    entry_box = Entry(window, textvariable=entry_text, font=("Arial", 14), width=30)
    entry_box.pack(pady=10)

    # Label for displaying search results
    result = StringVar()
    result_label = Label(window, textvariable=result, font=("Arial", 14), bg="#f7f7f7", fg="green")
    result_label.pack(pady=10)

    # Search button
    search_btn = Button(window, text="Search", command=search_word, font=("Arial", 14), bg="#4CAF50", fg="white")
    search_btn.pack(pady=10)

    # Exit button
    exit_btn = Button(window, text="Exit", command=window.destroy, font=("Arial", 14), bg="#DC143C", fg="white")
    exit_btn.pack(pady=10)

    # Run the application loop
    window.mainloop()

# Run the Yoruba dictionary app
if __name__ == "__main__":
    yoruba_app()
