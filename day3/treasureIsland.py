print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

side = input("You're at a cross road, Which direction do you want to go? left or right?\n ").lower()

if side == 'left':
    water = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for the "
                  "boat. Type 'swim' to swim across.\n").lower()
    if water == 'wait':
        door = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one Yellow and one '
                     'blue. Which color do you choose?\n ').lower()
        if door == 'yellow':
            print('You win! The treasure is yours!')
        elif door == 'blue':
            print("It's a room full of snakes. Game Over!")
        elif door == 'red':
            print("It's a room full of fire. Game Over!")
        else:
            print("Door doesn't exit.Game over!")
    else:
        print('Attacked by an angry trout. Game Over!')

else:
    print('You fell into a hole.Game Over!')
