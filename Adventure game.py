# We are still in the red room, we updated the program with the function you_died with a reason
# https://github.com/codinggrace/text_based_adventure_game
# actions
def you_died(why):
    # you expect a reason wy the player died, it's a string.
    # In: Passing in the string showing player how they die. Result: Prints reason why the player died.
    # Program exits without error.

    print(f"{why}. Good job!".format(why))

    # this exits the program entirely
    exit(0)

# end actions

# We now have a premise. We are in a room and have two doors to choose from.
# Each door leads to a room and we need to do something, in the red room specifically

# CHARACTERS

def guard():
    '''
    Encountering the guard, the player chooses to attack, check or sneak.
    - attack: player dies and it is game over
    - check: sees what the guard is doing, but nothing else happens, and get 3 options again
    - sneak: player sneaks past the guard and wins the game
    :return:
    '''
    # actions on the guard
    actions_dict = {"check":"You see the guard is still sleeping, you need to get to that door on the right of him. "
                            "What are you waiting for?",
                    "sneak":"You approach the guard, he's still sleeping. Reaching for the door, you open it slowly and"
                            " slip out.",
                    "attack":"You swiftly run towards the sleeping guard and knock him out with the hilt of your shiney"
                             " sword. Unfortunately it wasn't hard enough."}
    # while loop
    while True:
        action = input("What do you do? [attack | check | sneak] >").lower()
        if action in actions_dict.keys():
            print(actions_dict[action])
            if action == "sneak":
                print("You just slipped through the door before the guard realised it.")
                print("You are now outside, home free! Huzzah!\n")
                return
            elif action == "attack":
                you_died("Guard woke up with a grunt, and reached for his dagger and before you know it, the world goes "
                         "dark and you just died. \n<GAME OVER>")

# END OF CHARACTERS

# ROOMS #

def blue_door_room():
    # this is the blue door room
    # The player finds a treasure chest, options to investigate the treasure or guard.
    # If player chooses Treasure chest - show it's contents. Guard - nothing for now.

    treasure_chest = ["diamonds", "gold", "silver", "crystal sword", "rubies", "bitcoin"]
    print("You see a room with a wooden treasure chest on the left, and a sleeping guard "
          "on the right in front of the door.")
    action = input("What do you do? > ")
    if action.lower() in ["treasure", "chest", "silver"]:
        print("Ooh, treasure!")

        # New code starts here!
        print("Open it? Press '1'")
        print("Leave it alone? Press '2'")
        choice = input("> ")

        if choice == "1":
            print("Let's see what's in here... /grins")
            print("The chest creaks open, and the guard is still sleeping. That's one heavy sleeper!")
            print("You find some:")

            # for loop, for each treasure (variable created on the fly in the for loop in treasure_chest list,
            # print the treasure
            for treasure in treasure_chest:
                print(treasure)
                # Funny thing! I noticed the code posted online was missing the "Else" statement. Was good to see the
                # potential issue.

                # So much treasure, what to do? Take it or leave it!
                print("What do you want to do?")

                num_items_in_chest = len(treasure_chest)

                print(f"To take all {num_items_in_chest} treasure pieces, press '1'")
                print("To leave it, press '2'")

                treasure_choice = input("> ")
                if treasure_choice == '1':
                    treasure_chest.remove("crystal sword")
                    print("\tYou take the shinier sword from the treasure chest. It does look exceedingly shiny.")
                    print("\tWoohoo! Bounty and a shiney new sword. /drops your crappy sword in the empty treasure "
                          "chest.")

                    temp_treasure_list = treasure_chest[:]
                    treasure_contents = ", ".join(treasure_chest)
                    print(f"\tYou also receive {treasure_contents}.")

                    # removing all the rest of the items in the treasure chest
                    for treasure in temp_treasure_list:
                        # use a list remove() function to remove each item in the chest
                        treasure_chest.remove(treasure)
                    treasure_chest.append("crappy sword")
                    print(f"\tYou close the lid of the chest containing {treasure_chest} for the next adventure. /grins")
                    print("Now onward to get past this sleeping guard and the door to freedom.")
                elif treasure_choice == '2':
                    print("It will still be here (I hope), right after I get past this guard.")
        elif choice == '2':
            print("Who needs treasure? Let's get out of here!")
    elif action.lower() in ["guard", "right"]:
        print("Let's have fun with the guard.")
    else:
        print("Well, not sure what you picked there, let's poke the guard cos it's fun!")
    guard()

def red_door_room():
    # this is the red door room
    print("There you see a great red dragon.")
    print("It stares at you through one narrowed eye.")
    print("Do you flee for your life or stay?")

    next_move = input("> ")

    # flee to return to the start of the game in the room with the blue and red door or die

    if "flee" in next_move:
        start_adventure()
    else:
        you_died("It eats you. Well, that was tasty!")
# end rooms

def get_player_name():
    '''
    Gets players name, may or may not be renamed depending on player's action.
    Returns player name back (altered or unaltered)
    :return:
    '''
    name = input("What's your name? > ")

    alt_name = "Rainbow Unicorn"

    answer = input(f"Your name is {alt_name.upper()}, is that correct? [Y|N] > ")

    if answer.lower() in ["y", "yes"]:
        name = alt_name

    elif answer.lower in ["n", "no"]:
        print(f"Ok, picky. {name.upper()} it is. Let's get started on our adventure!")
    else:
        print(f"Trying to be funny? Well you will now be called {alt_name.upper()} anyway!")
        name = alt_name
    ''' 
    Now notice that we are returning the variable called name. In main(), it doesn't know what the variable
    "name" is, as it only exists in the get_player_name() function.
    This is why indentation is important, variables declared in this block only exist in that block.
    '''
    return name
def start_adventure():
    print("You enter a room, you see a red door to your left and a blue door to your right")
    door_picked = input("Do you pick the red door or the blue door? > ")

    if door_picked == 'red':
        red_door_room()
    elif door_picked == 'blue':
        blue_door_room()
    else:
        print("Sorry, it's either 'red' or 'blue' as the choice. You are the weakest link, goodbye!")

def main():
    player_name = get_player_name()

    start_adventure()

    print("\nThe end\n")
    print(f"Thanks for playing, {player_name.upper()}!")

if __name__ == '__main__':
    main()