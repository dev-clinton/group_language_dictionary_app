from tkinter import *

def igbo_dictionary_app():
    window = Tk()
    window.title("Igbo Dictionary")
    window.geometry("350x250")
    window.configure(bg="#f0f0f0")

    header_label = Label(window, text="Igbo Dictionary", font=("Arial", 18, "bold"), bg="#f0f0f0")
    header_label.pack(pady=10)

    igbo_dict = {
        "Iko": "Cup",
        "Efele": "Plate",
        "Nni": "Food",
        "Mmiri": "Water",
        "Elekere": "Time",
        "Ngazi": "Spoon",
        "Ute": "Mat",
        "Akukwo": "Book",
        "Ugwu": "Mountain",
        "Akpa": "Bag",
        "Akwa": "Cloth",
        "Okuko": "Chicken",
        "Agwagwa": "Lizard",
        "Okpa": "Leg",
        "Anya": "Eye",
        "ISI": "Head",
        "Nna": "Father",
        "Nne": "Mother",
        "Ekwenti": "Phone",
        "Osikapa": "Rice",

    }

    entry_text = Entry(window, font=("Arial", 14), width=25)
    entry_text.pack(pady=10)

    result = StringVar()
    result_label = Label(window, textvariable=result, font=("Arial", 14), bg="#f0f0f0")
    result_label.pack(pady=10)

    def search():
        word = entry_text.get().strip().lower()
        for key, value in igbo_dict.items():
            if word == key.lower():
                result.set(value)
                return
        result.set("Not Found")

    search_btn = Button(window, text="Search", command=search, font=("Arial", 14), bg="#4CAF50", fg="#fff")
    search_btn.pack(pady=10)

    window.mainloop()

igbo_dictionary_app()
