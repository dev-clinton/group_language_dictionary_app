from tkinter import *

def spanish_dictionary_app():
    # Create the Spanish dictionary window
    window = Tk()
    window.title("Spanish Dictionary")
    window.geometry("350x300")  # Increased window size for better UI

    # Spanish dictionary
    spanish_dictionary = {
        "hola": "hello",
        "adios": "goodbye",
        "gracias": "thank you",
        "amor": "love",
        "familia": "family",
        "feliz": "happy",
        "navidad":"christmas",
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
        "abrazo":"hug",
        "sonrisa":"smile",
        "beso":"kiss",
        "corazon":"heart",
        "piton":"python",
    }

    # Autocomplete function
    def autocomplete(*args):
        typed_word = entry_text.get()

        # If the input is empty, show feedback and hide the suggestion listbox
        if typed_word == "":
            suggestion_listbox.place_forget()
            feedback_label.config(text = "Please enter a spanish word", fg = "green")
            return

        # Get all suggestions that start with the typed word (case-insensitive)
        suggestions = [
            word for word in spanish_dictionary.keys()
            if word.lower().startswith(typed_word.lower())
        ]

        # Update the listbox with matching suggestions
        suggestion_listbox.delete(0, END)  # Clear previous suggestions
        for suggestion in suggestions:
            suggestion_listbox.insert(END, suggestion)

        if not suggestions:  # Hide the listbox if no matches
            suggestion_listbox.place_forget()
            feedback_label.config(text = "No suggestions found", fg = "red")
        else:
            suggestion_listbox.place(x = entry_box.winfo_x(), y = entry_box.winfo_y() + 30)
            feedback_label.config(text = f"{len(suggestions)} suggestions found", fg = "blue")

    # Select word from the listbox
    def on_select(event):
        selected_word = suggestion_listbox.get(suggestion_listbox.curselection())
        entry_text.set(selected_word)
        search(selected_word)

    # Search function
    def search(word):
        if word.lower() in spanish_dictionary:
            result.set(spanish_dictionary[word.lower()])
        else:
            result.set("Not Found")

    # Clear function
    def clear():
        entry_text.set("")
        result.set("")
        suggestion_listbox.place_forget()
        feedback_label.config(text = "")

    # GUI elements
    entry_text = StringVar()
    result = StringVar()

    # Trace user input for autocomplete
    entry_text.trace("w", autocomplete)

    # Title Label
    title_label = Label(window, text = "Spanish Dictionary", font = ("Helvetica", 18, "bold"), fg = "red")
    title_label.pack(pady = 10)

    # Input field
    entry_box = Entry(window, textvariable = entry_text, font = ("Helvetica", 14))
    entry_box.pack(pady = 10)

    # Feedback label
    feedback_label = Label(window, text = "Please enter a spanish word", font = ("Helvetica", 10), fg = "gray")
    feedback_label.pack()

    # Suggestion listbox (hidden initially)
    suggestion_listbox = Listbox(window, width = 30, height = 6, selectmode = SINGLE, font = ("Helvetica", 12))
    suggestion_listbox.bind("<ButtonRelease-1>", on_select)
    suggestion_listbox.place_forget()

    # Result label
    result_label = Label(window, textvariable = result, font = ("helvetica", 14), fg = "blue")
    result_label.pack(pady = 10)

    # Buttons
    button_frame = Frame(window)
    button_frame.pack(pady = 10)

    search_btn = Button(
        button_frame,
        text = "Search",
        font = ("helvetica", 12),
        command = lambda: search(entry_text.get())
    )
    search_btn.grid(row = 0, column = 0, padx = 5)

    refresh_button = Button(
        button_frame,
        text = "Refresh",
        font = ("helvetica", 12),
        command = clear
    )
    refresh_button.grid(row = 0, column = 2, padx = 5)

    window.mainloop()

# Run the Spanish dictionary app
spanish_dictionary_app()