print('''
 __      _            _        _      
 / _|    (_)          | |      | |     
| |_ __ _ _ _ __ _   _| |_ __ _| | ___ 
|  _/ _` | | '__| | | | __/ _` | |/ _ \
| || (_| | | |  | |_| | || (_| | |  __/
|_| \__,_|_|_|   \__, |\__\__,_|_|\___|
                  __/ |                
                 |___/          
''')
print("Welcome to your twisted Fairytale.")
print("Your mission is to rescue Princess Esmerelda, trapped in the castle.")
choice1 = input('As you waltz along a cobbled road, you are met with a fork in the road and only two directions to go. Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You have made it to the castle. Type "stairs" to ascend the spiral staircase. Type "rope" to slowly inch yourself upwards to the top of the castle. \n').lower()
  if choice2 == "rope":
    choice3 = input('You have reached the top of the castle where Princess Esmerelda eagerly awaits your arrival. She has been trapped in the castle for the last decade and has not seen a soul since. She calls out asking for the secret codeword. Open Sesame. Dog Biscuits. Magic Mushrooms. Which secret codeword do you choose? \n').lower()
    if choice3 == "dog biscuits":
      print("The walls begin to close in all around you. You are squashed to a pulp.")
    elif choice3 == "open sesame":
      print("This is the secret code for almost everything, except this. You spontaneously combust into a raging ball of fire.")
    elif choice3 == "magic mushrooms":
      print("Congratulations. The door to Princess Esmerelda's chambers opens. She greets you with a kiss on the cheek and starts to cry hysterically with joy.")
    else:
      print("You picked an option that wasn't an option. Game Over.")
  else:
    print("Wrong choice buddy.")
else:
  print("Wrong choice buddy!")