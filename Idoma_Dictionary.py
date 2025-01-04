from tkinter import Tk, Entry, Label, Button, StringVar

def create_gui(window, idoma_dict):
    entry_text = Entry(window)
    entry_text.pack()

    result = StringVar()
    result_label = Label(window, textvariable=result)
    result_label.pack()

    def search_word():
        word = entry_text.get().strip().lower()
        for key, value in idoma_dict.items():
            if word == key.lower():
                result.set(value)
                return
        result.set("Not Found")

    search_btn = Button(window, text="Search", command=search_word)
    search_btn.pack()

def idoma_dictionary_app():
    window = Tk()
    window.title("Idoma Dictionary")
    window.geometry("300x200")

    idoma_dict = {
        "Wa": "Come",
        "Ehi": "Gift",
        "Enem": "My Mother",
        "Nyor": "Go",
        "Ole": "House",
        "Ola": "Fire or light",
        "Oine": "My relative",
        "Odedere": "Food",
        "Ewa": "Knife",
        "Ewu": "Goat",
        "Agodo": "Bed",
        "Ily": "Cloth",
        "Anor": "Oil",
        "Anor le": "Red oil",
        "Ije": "Money",
        "Eje": "Lion",
        "Eche": "Earth",
        "Adah": "Father",
        "Ena": "Cow",
        "Ebo": "Peace",
    }

    create_gui(window, idoma_dict)
    window.mainloop()

if __name__ == "__main__":
    idoma_dictionary_app()
