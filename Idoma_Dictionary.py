from tkinter import Tk, Entry, Label, Button, StringVar, Toplevel


def create_gui(window, idoma_dict):
    # Input Entry Field
    entry_text = StringVar()
    entry_box = Entry(window, textvariable=entry_text, font=("Arial", 14), width=30)
    entry_box.pack(pady=10)

    # Result Label
    result = StringVar()
    result_label = Label(window, textvariable=result, font=("Arial", 12), fg="green")
    result_label.pack(pady=10)

    # Search Function
    def search_word():
        word = entry_text.get().strip().lower()  # Convert to lowercase for case-insensitive search
        if word in idoma_dict:
            result.set(f"Meaning: {idoma_dict[word]}")
        else:
            result.set("Word Not Found in Idoma Dictionary")

    # Search Button
    search_btn = Button(window, text="Search", command=search_word, font=("Arial", 12), bg="#4CAF50", fg="white")
    search_btn.pack(pady=10)

    # Exit Button
    exit_btn = Button(window, text="Exit", command=window.destroy, font=("Arial", 12), bg="#DC143C", fg="white")
    exit_btn.pack(pady=10)

def idoma_dictionary_app():
    # Create Main Window
    window = Toplevel()
    window.title("Idoma Dictionary")
    window.geometry("400x300")
    window.configure(bg="#f0f8ff")  # Light blue background color

    # Title Label
    title_label = Label(window, text="Idoma Dictionary", font=("Arial", 18, "bold"), bg="#f0f8ff", fg="black")
    title_label.pack(pady=10)

    # Idoma Dictionary
    idoma_dict = {
        "wa": "Come",
        "ehi": "Gift",
        "enem": "My Mother",
        "nyor": "Go",
        "ole": "House",
        "ola": "Fire or Light",
        "oine": "My Relative",
        "odedere": "Food",
        "ewa": "Knife",
        "ewu": "Goat",
        "agodo": "Bed",
        "ily": "Cloth",
        "anor": "Oil",
        "anor le": "Red Oil",
        "ije": "Money",
        "eje": "Lion",
        "eche": "Earth",
        "adah": "Father",
        "ena": "Cow",
        "ebo": "Peace",
    }

    create_gui(window, idoma_dict)
    window.mainloop()

# Run the Application
if __name__ == "__main__":
    idoma_dictionary_app()
