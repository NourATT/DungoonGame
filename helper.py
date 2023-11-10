def player_choice(prompt, num_choices):
    print("\nMake your choice.\n")
    while True:
        player_input = input(prompt)
        if player_input.isnumeric():
            if int(player_input) in range(1, num_choices+1):
                return int(player_input)
            else:
                print(f"Invalid input, must be a number 1-{num_choices}!")
        else:
            print(f"Invalid input: {player_input} is not a number!")
