from art import greetings
from programs import band_name_generator

print(greetings)
print("Welcome to the Python Playbook!")
print("This is a collection of Python programs that demonstrate various concepts and techniques.")

programs = {
    "1": "Band Name Generator",
    "2": "Tip Calculator",
    "3": "Treasure Island Game",
    "4": "Rock Paper Scissors Game",
    "5": "Hangman Game",
    "6": "Password Generator",
    "7": "Caesar Cipher",
    "8": "Blackjack Game",
}

while True:
    print("\nAvailable Programs:")
    for number, program in programs.items():
        print(f"| {number} | {program} ")

    select_programs = input("Type the number of the program you want to run or type 'q' to exit: \n")

    if select_programs == "1":
        band_name_generator.run()
    elif select_programs == "2":
        import program2
    elif select_programs.lower() == 'q':
        print("Exiting the Python Playbook. Goodbye!")
        break
    else:
        print("Invalid selection. Please try again.")