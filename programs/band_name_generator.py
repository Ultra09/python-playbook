from programs.utils import get_yes_or_no_input

def generate_band_name(city, pet):
    return f"{city} {pet}"

def run():
    print("\n=== Welcome to the Band Name Generator! ===\n")

    while True:
        city = input("What's the name of the city you grew up in? \n")
        pet = input("What's the name of your pet? \n")
        band_name = generate_band_name(city, pet)

        print(f"Your band name could be: {band_name} \n")

        restart = get_yes_or_no_input("Would you like to generate another band name? (yes/no): \n")
        if restart == 'no':
            print("Thank you for using the Band Name Generator. Returning to Main Menu... \n")
            break