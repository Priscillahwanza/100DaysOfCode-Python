import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇


elements = [rock, paper, scissors]
choice = int(input('What do you choose? Type 0 for Rock, 1 for paper and 2 for scissors.\n'))

if choice >= 3 or choice < 0:
    print('Invalid input.')
else:
    choice_user = elements[choice]
    print(choice_user)

    computer_choice = random.choice(elements)
    print(f'Computer chose: {computer_choice}')

    # Rock wins against scissors.
    # Scissors win against paper.
    # Paper wins against rock.

    if choice_user == rock and computer_choice == scissors:
        print('You win!')
    elif choice_user == scissors and computer_choice == paper:
        print('You win!')
    elif choice_user == paper and computer_choice == rock:
        print('You win!')
    elif choice_user == computer_choice:
        print('You draw!')

    else:
        print('You lose!')
