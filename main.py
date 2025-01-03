from spanish import spanish_dictionary_app
def main():
    while True:  #true Loop is to keep the program running
        print("\nWelcome to this Multi_lingual Dictionary!")
        print("Select a dictionary:")
        print("1. Spanish")
        print("2. Igbo (coming soon)")
        print("3. Yoruba (coming soon)")
        print("4. Idoma (coming soon)")
        print("5. Japanese (coming soon)")
        print("6. Exit")

        choice = input("Enter your choice from (1-6): ")

        if choice == "1":
            spanish_dictionary_app()  # Calls the Spanish dictionary

            """the remaining dictionary will be added after creating the main.py code
             for the other collaborators to join, then the code will change"""

        elif choice == "2":
            print("sorry,The Igbo dictionary is not available yet.")
        elif choice == "3":
            print("sorry,The Yoruba dictionary is not available yet.")
        elif choice == "4":
            print("sorry,The Idoma dictionary is not available yet.")
        elif choice == "5":
            print(" sorry,The Japanese dictionary is not available yet.")
        elif choice == "6":
            print("you are Exiting the program now!")
            break
        else:
            print("Invalid ,Please try again.")
# main program
if __name__ == "__main__":
    main()
