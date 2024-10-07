import random

ascii_art = r"""

  _________      .__                             _________ __         .__         __________               .__              
 /   _____/ ____ |  |__   ___________   ____    /   _____//  |_  ____ |__| ____   \______   \_____  ______ |__| ___________ 
 \_____  \_/ ___\|  |  \_/ __ \_  __ \_/ __ \   \_____  \\   __\/ __ \|  |/    \   |     ___/\__  \ \____ \|  |/ __ \_  __ \
 /        \  \___|   Y  \  ___/|  | \/\  ___/   /        \|  | \  ___/|  |   |  \  |    |     / __ \|  |_> >  \  ___/|  | \/
/_______  /\___  >___|  /\___  >__|    \___  > /_______  /|__|  \___  >__|___|  /  |____|    (____  /   __/|__|\___  >__|   
        \/     \/     \/     \/            \/          \/           \/        \/                  \/|__|           \/       
                                                     
"""

options = ["Schere", "Stein", "Papier"]
user_score = 0
computer_score = 0

print(ascii_art)

while user_score < 3 and computer_score < 3:
    print("1. Schere")
    print("2. Stein")
    print("3. Papier")
    user_input = input("Wählen Sie von 1-3: ")
    user_choice = options[int(user_input) - 1] if user_input.isdigit() and 1 <= int(user_input) <= 3 else None

    computer_choice = random.choice(options)

    if user_choice is None:
        print("Ungültige Eingabe. Bitte wählen Sie 1, 2 oder 3.")
        continue

    print("\nDu hast gewählt:", user_choice)
    print("Computer hat gewählt:", computer_choice)
    
    if user_choice == computer_choice:
        print("Unentschieden!")
    elif (user_choice == "Stein" and computer_choice == "Schere") or \
         (user_choice == "Schere" and computer_choice == "Papier") or \
         (user_choice == "Papier" and computer_choice == "Stein"):
        print("Du gewinnst diese Runde!")
        user_score += 1
    else:
        print("Computer gewinnt diese Runde!")
        computer_score += 1

    print(f"\nScore: Player {user_score} - {computer_score} Computer\n")

if user_score == 3:
    print("Du das Spiel gewonnen!")
else:
    print("Computer das das Spiel gewonnen")
