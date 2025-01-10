from tkinter import *

def yoruba_app():
    window = Tk()
    window.title("Yoruba Dictionary")
    window.geometry("300x300")

    # Yoruba dictionary
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

    # insensitive search function
    def search(word):
        word_lower = word.lower()  # Converts the input word to lowercase
        for key, value in yoruba_dictionary.items():
            if key.lower() == word_lower:
                result.set(value)
                return
        result.set("No matching word")

    entry_text = StringVar()
    result = StringVar()

    title_label = Label(window, text="Yoruba Dictionary", font=("Arial", 16, "bold"))
    title_label.pack(pady=20)

    # Entry box for word input (Using Arial font)
    entry_box = Entry(window, textvariable=entry_text, font=("Arial", 14))
    entry_box.pack(pady=10)

    # display the result (Using Arial font)
    result_label = Label(window, textvariable=result, font=("Arial", 14))
    result_label.pack(pady=10)

    search_btn = Button(
        window,
        text="Search",
        font=("Arial", 14),
        command=lambda: search(entry_text.get())
    )
    search_btn.pack(pady=10)

    window.mainloop()

# Call the function to run the yoruba app
yoruba_app()
