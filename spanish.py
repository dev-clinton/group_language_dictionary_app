from tkinter import * # tkinter is a gui function in python
# and * is used to import necessary tkinter alias like tk,button,label,listbox,e.t.c instead of typing them out

def spanish_dictionary_app():
    # Create the Spanish dictionary window
    # i changed tk to toplevel for it to be able to open a new window when called from main.py
    window = Toplevel()
    window.title("Spanish Dictionary")
    window.geometry("400x350")
    window.configure(bg="#f9f9f9")  # added Light background for better visibility

    # The Spanish dictionary
    spanish_dictionary = {
        "hola": "hello",
        "adios": "goodbye",
        "gracias": "thank you",
        "amor": "love",
        "familia": "family",
        "feliz": "happy",
        "navidad": "christmas",
        "libro": "book",
        "casa": "house",
        "escuela": "school",
        "maestro": "teacher",
        "agua": "water",
        "comida": "food",
        "amigo": "friend",
        "cielo": "sky",
        "mar": "sea",
        "rojo": "red",
        "verde": "green",
        "azul": "blue",
        "tiempo": "time",
        "dia": "day",
        "proyecto": "project",
        "abrazo": "hug",
        "sonrisa": "smile",
        "beso": "kiss",
        "corazon": "heart",
        "piton": "python",
    }

    #my Autocomplete function
    def autocomplete(*args):
        typed_word = entry_text.get().strip()

        # Show feedback if the input is empty
        if not typed_word:
            suggestion_listbox.place_forget()
            feedback_label.config(text="Please enter a Spanish word", fg="gray")
            return

        # Get suggestions
        suggestions = [
            word for word in spanish_dictionary.keys()
            if word.lower().startswith(typed_word.lower())
        ]

        # listbox with suggestions
        suggestion_listbox.delete(0, END)
        for suggestion in suggestions:
            suggestion_listbox.insert(END, suggestion)

        # Shows or hide the listbox based on suggestions
        if suggestions:
            suggestion_listbox.place(x=entry_box.winfo_x(), y=entry_box.winfo_y() + 30)
            feedback_label.config(text=f"{len(suggestions)} suggestions found", fg="blue")
        else:
            suggestion_listbox.place_forget()
            feedback_label.config(text="No suggestions found", fg="red")

    # Handle listbox selection
    def on_select(event):
        selected_word = suggestion_listbox.get(suggestion_listbox.curselection())
        entry_text.set(selected_word)
        search(selected_word)

    # Search function
    def search(word):
        if word.lower() in spanish_dictionary:
            result.set(f"Meaning: {spanish_dictionary[word.lower()]}")
            feedback_label.config(text="Word found!", fg="green")
        else:
            result.set("Not Found")
            feedback_label.config(text="Word not found", fg="red")

    # Clear input and results
    def clear():
        entry_text.set("")
        result.set("")
        suggestion_listbox.place_forget()
        feedback_label.config(text="Please enter a Spanish word", fg="gray")

    # Initialize variables
    entry_text = StringVar()
    result = StringVar()
    entry_text.trace("w", autocomplete)  # Track user input for autocomplete

    # Title label
    title_label = Label(window, text="Spanish Dictionary", font=("Helvetica", 18, "bold"), bg="#f9f9f9", fg="red")
    title_label.pack(pady=10)

    # Entry box
    entry_box = Entry(window, textvariable=entry_text, font=("Helvetica", 14))
    entry_box.pack(pady=10)

    # Feedback label
    feedback_label = Label(window, text="Please enter a Spanish word", font=("Helvetica", 10), bg="#f9f9f9", fg="gray")
    feedback_label.pack()

    # Suggestion listbox
    suggestion_listbox = Listbox(window, width=30, height=6, selectmode=SINGLE, font=("Helvetica", 12))
    suggestion_listbox.bind("<ButtonRelease-1>", on_select)
    suggestion_listbox.place_forget()

    # Result label
    result_label = Label(window, textvariable=result, font=("Helvetica", 14), bg="#f9f9f9", fg="blue")
    result_label.pack(pady=10)

    # Buttons
    button_frame = Frame(window, bg="#f9f9f9")
    button_frame.pack(pady=10)

    search_btn = Button(
        button_frame, text="Search", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=lambda: search(entry_text.get())
    )
    search_btn.grid(row=0, column=0, padx=5)

    refresh_btn = Button(
        button_frame, text="Refresh", font=("Helvetica", 12), bg="#DC143C", fg="white", command=clear
    )
    refresh_btn.grid(row=0, column=1, padx=5)

    # Run the app
    window.mainloop()

if __name__ == "__main__":
    spanish_dictionary_app()
