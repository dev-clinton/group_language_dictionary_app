from tkinter import *

def japanese_app():
    # Create the main window
    window = Toplevel()
    window.title("Japanese Dictionary")
    window.geometry("350x300")
    window.config(bg="#f0f8ff")  # Light blue background

    # Japanese dictionary
    japanese_dictionary = {
        "kawa": "River",
        "yama": "Mountain",
        "gomen": "Sorry",
        "neko": "Cat",
        "inu": "Dog",
        "hana": "Flower",
        "kami": "Paper",
        "mizu": "Water",
        "kaze": "Wind",
        "hi": "Sun",
        "yuki": "Snow",
        "ame": "Rain",
        "umi": "Sea",
        "sora": "Sky",
        "ki": "Tree",
        "tori": "Bird",
        "uma": "Horse",
        "natsu": "Summer",
        "fuyu": "Winter",
        "haru": "Spring"
    }

    # The dictionary search function
    def search(word):
        word = word.lower()  # Ensure case insensitivity
        if word in japanese_dictionary:
            result.set(f"Meaning: {japanese_dictionary[word]}")
        else:
            result.set("Word Not Found in Japanese Dictionary")

    # StringVars for input and result
    entry_text = StringVar()
    result = StringVar()

    # Title Label
    title_label = Label(
        window,
        text="Japanese Dictionary",
        font=("Arial", 18, "bold"),
        bg="#f0f8ff",
        fg="black"
    )
    title_label.pack(pady=10)

    # Entry Box
    entry_box = Entry(
        window,
        textvariable=entry_text,
        font=("Arial", 14),
        bg="white",
        fg="black",
        width=30
    )
    entry_box.pack(pady=10)

    # Search Button
    search_btn = Button(
        window,
        text="Search Word",
        font=("Arial", 12, "bold"),
        bg="#4b0082",
        fg="white",
        command=lambda: search(entry_text.get())
    )
    search_btn.pack(pady=10)

    # Result Label
    result_label = Label(
        window,
        textvariable=result,
        font=("Arial", 14),
        bg="#f0f8ff",
        fg="green",
        wraplength=300
    )
    result_label.pack(pady=10)

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

    window.mainloop()

# Ensure the script runs properly when executed
if __name__ == "__main__":
   japanese_app()
