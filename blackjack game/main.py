import random as r
from deface import logo
print(logo[0])

cards = ['11', '2', '3', '4', '5','6', '7', '8', '9', '10', '10', '10']

menu = ""
while "quit" not in menu:
    #* gives 2 card to user
    user_cards = []
    pc_cards = []
    for i in range(0,2):
        user_cards += r.choices(cards)
        pc_cards += r.choices(cards)

    user_sum = 0
    pc_sum = 0
    for i in range(0,2):
        user_sum += int(user_cards[i])
        pc_sum += int(pc_cards[i])

    print(f"Your cards {user_cards} and sum {user_sum}")
    print(f"Pc cards ['{pc_cards[0]}']")

    if user_sum == 21:
        if pc_sum == 21:
            print("Draw")
        else:
            print("You win")
    elif pc_sum == 21:
        if user_sum == 21:
            print("Draw")
        else:
            print("Pc wins")
    else:

        play = ""
        while "over" not in play:
            user_input = input("Do you want to take another card? if yes type 'y' or see'n' \n=>").lower()
            if user_input == 'y':
                user_cards += r.choice(cards)
                print(user_cards)
                user_sum += int(user_cards[2])
                if user_sum == 21:
                    if pc_sum == 21:
                        print("Draw")
                        play = "over"
                    else:
                        print("You win")
                        play = "over"
                elif pc_sum == 21:
                    if user_sum == 21:
                        print("Draw")
                        play = "over"
                    else:
                        print("Pc wins")
                        play = "over"
                elif user_sum > 21:
                    print("You lose")
                    play = "over"
                else:
                    if user_sum == pc_sum:
                        print("Draw")
                        play = "over"
                    if user_sum > pc_sum:
                        print("You win")
                        play = "over"
                    else:
                        print("You lose")
                        play = "over"
            elif user_input == 'n':
                if user_sum == pc_sum:
                    print("Draw")
                    play = "over"
                elif user_sum > pc_sum:
                    print("You win")
                    play = "over"
                else:
                    print("Pc wins")
                    play = "over"
            else:
                print("Invalid Input")
    
    
    print(f"Your cards {user_cards} and sum {user_sum}")
    print(f"Pc cards {pc_cards} and sum {pc_sum}")
    menu = input("Type 'play again' or to quit type 'quit' \n=>")
                            
            

        
# print(user_sum, pc_sum)
# print(user_cards, pc_cards)
#* gives 2 card to computer