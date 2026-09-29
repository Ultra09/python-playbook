def get_yes_or_no_input(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in ['yes', 'no']:
            return user_input
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")