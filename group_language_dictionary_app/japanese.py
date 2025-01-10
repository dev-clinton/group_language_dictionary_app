from tkinter import *

def japanese_app():
    window = Tk()
    window.title("Japanese Dictionary")
    window.geometry("300x250")

    japanese_dictionary = {
        "Kawa": "River",
        "Yama": "Mountain",
        "Gomen": "Sorry",
        "Neko": "Cat",
        "Inu": "Dog",
        "Hana": "Flower",
        "Kami": "Paper",
        "Mizu": "Water",
        "Kaze": "Wind",
        "Hi": "Sun",
        "Yuki": "Snow",
        "Ame": "Rain",
        "Umi": "Sea",
        "Sora": "Sky",
        "Ki": "Tree",
        "Tori": "Bird",
        "Uma": "Horse",
        "Natsu": "Summer",
        "Fuyu": "Winter",
        "Haru": "Spring"
    }

    # The dictionary search function
    def search(word):
        if word in japanese_dictionary:
            result.set(japanese_dictionary[word])
        else:
            result.set("japanese Word Not Found")

    entry_text = StringVar()
    result = StringVar()

    entry_box = Entry(window, textvariable=entry_text, font=("Times New Roman", 14))
    entry_box.pack(pady=8)

    result_label = Label(window, textvariable=result, font=("Times New Roman", 14))
    result_label.pack(pady=8)

    title_lable = Label(window, text = "japanese dictionary", font = ("Times New Roman", 15, "bold" ),fg = "blue")
    title_lable.pack(pady = 8)

    search_btn = Button(
        window,
        text="Search word",
        font=("Times New Roman", 14),
        command=lambda: search(entry_text.get())
    )
    search_btn.pack(pady=8)

    window.mainloop()

japanese_app()
