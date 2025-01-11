from tkinter import *

def igbo_dictionary_app():
    # Create the main window
    window = Toplevel()
    window.title("Igbo Dictionary")
    window.geometry("400x300")
    window.configure(bg="#f0f8ff")  # Light blue background color

    # Igbo Dictionary
    igbo_dict = {
        "iko": "Cup",
        "efele": "Plate",
        "nni": "Food",
        "mmiri": "Water",
        "elekere": "Time",
        "ngazi": "Spoon",
        "ute": "Mat",
        "akukwo": "Book",
        "ugwu": "Mountain",
        "akpa": "Bag",
        "akwa": "Cloth",
        "okuko": "Chicken",
        "agwagwa": "Lizard",
        "okpa": "Leg",
        "anya": "Eye",
        "isi": "Head",
        "nna": "Father",
        "nne": "Mother",
        "ekwenti": "Phone",
        "osikapa": "Rice",
    }

    # Title Label
    header_label = Label(window, text="Igbo Dictionary", font=("Arial", 18, "bold"), bg="#f0f8ff", fg="blue")
    header_label.pack(pady=10)

    # Input Entry
    entry_text = StringVar()
    entry_box = Entry(window, textvariable=entry_text, font=("Arial", 14), width=30, bg="white", fg="black")
    entry_box.pack(pady=10)

    # Result Label
    result = StringVar()
    result_label = Label(window, textvariable=result, font=("Arial", 14), bg="#f0f8ff", fg="green", wraplength=300)
    result_label.pack(pady=10)

    # Search Function
    def search():
        word = entry_text.get().strip().lower()  # Ensure case insensitivity
        if word in igbo_dict:
            result.set(f"Meaning: {igbo_dict[word]}")
        else:
            result.set("Word Not Found in Igbo Dictionary")

    # Search Button
    search_btn = Button(
        window,
        text="Search Word",
        font=("Arial", 12, "bold"),
        bg="#4CAF50",
        fg="white",
        command=search
    )
    search_btn.pack(pady=10)

    # Exit Button
    exit_btn = Button(
        window,
        text="Exit",
        font=("Arial", 12, "bold"),
        bg="#dc143c",
        fg="white",
        command=window.destroy
    )
    exit_btn.pack(pady=10)

    # Start the main loop
    window.mainloop()

# Ensure the script runs when executed directly
if __name__ == "__main__":
    igbo_dictionary_app()
