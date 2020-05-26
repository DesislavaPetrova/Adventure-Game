import time
import random

item = []
enemy = ["Maleficent", "Mother Gothel", "Rumpelstiltskin", "Baba Yaga"]
creature = random.choice(enemy)


def print_pause(message):
    print(message)
    time.sleep(3)


def intro():
    print_pause("You find yourself on a mountainous island, surrounded "
                "by houses on steeping hills and a beautiful palace.")
    print_pause(f"Rumor has it that {creature} has bewitched the princess "
                "and only a magical flower can break the spell.")
    print_pause("In front of you is the palace.")
    print_pause("To your left lies a green meadow.")
    print_pause("In your pocket you hold some healing "
                "(but not that effective) herbs.\n")
    choice()


def choice():
    print_pause("Enter 1 to knock on the door of the palace.\n"
                "Enter 2 to go to the meadow.\n"
                "What would you like to do?\n")
    enter()


def inside_palace():
    print_pause("You approach the door of the palace.")
    print_pause("You are about to knock when a steward opens the door "
                "and invites you in.")
    print_pause(f"You see {creature} guarding the princess and when")
    print_pause(f"{creature} sees you threatens to kill the princess.")
    print_pause("You feel a bit unprepared for this, because the only "
                "thing you can do for the princess is heal her.")
    heal_go()


def away():
    print_pause("You have escaped the palace. Luckily, the princess is safe "
                "and it seem that you haven't been followed.\n")
    choice()


def heal():
    if 'magical flower' in item:
        print_pause(f"As {creature} tries to kill the princess, you "
                    "use the magical healing flower to save her.")
        print_pause("The Sundrop Flower glows brightly in your hand "
                    "as you use it's healing abilities to heal the princess.")
        print_pause(f"{creature} takes one look at the magical flower and "
                    "defeated runs away from the kingdom forever!")
        print_pause(f"You have rid the kingdom of {creature}. "
                    "And you have healed the princess! "
                    "You are victorious!")
        play_again()
    else:
        print_pause("You try your best ...")
        print_pause("But your healing herbs are not enough to save the "
                    f"princess from the magic spell of {creature}.")
        print_pause("You have failed your quest!")
        play_again()


def error():
    print_pause("I don't recogize that choice.\n")


def heal_go():
    answer_1 = input("Would you like to (1)heal the princess or (2)go away?\n")
    if answer_1 == '1':
        heal()
    elif answer_1 == '2':
        away()
    else:
        error()
        heal_go()


def meadow_again():
    print_pause("You walk to the vast and beautiful green meadow.")
    print_pause("You've been here before, and you have found "
                "the magical healing flower.")
    print_pause("You walk back to the town.\n")
    choice()


def enter():
    responce = input("(Please enter 1 or 2.)\n")
    if responce == '2' and 'magical flower' in item:
        meadow_again()
    elif responce == '1':
        inside_palace()
    elif responce == '2':
        item.append("magical flower")
        print_pause("You walk to the vast green meadow.")
        print_pause("You have to search for a while for the magical flower.")
        print_pause("After some time your eye catches a glint of a glowing "
                    "golden flower.")
        print_pause("You have found the magical Sundrop Flower!")
        print_pause("You discard your not so useful healing herbs and take "
                    "The Sundrop Flower with you.")
        print_pause("You walk back to the town.\n")
        choice()
    else:
        enter()


def play_again():
    answer = input("Would you like to play again? (y/n)\n").lower()
    if answer == 'y' or answer == 'yes':
        print_pause("\n\n\nExcellent! Restarting the game ...\n\n\n")
        play_game()
    else:
        if answer == 'n' or answer == 'no':
            print_pause("\nThank you for playing! See you next time!")
            exit()
        else:
            error()
            play_again()


def play_game():
    intro()
    enter()


play_game()
