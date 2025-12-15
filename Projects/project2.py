extrovert_points = 0
introvert_points = 0
ambivert_points = 0

answer1 = input("do you prefer A staying at home, B a big party, or C a small gathering?")
if answer1 == "A" or answer1 == "a":
    introvert_points += 1
    extrovert_points -= 1
elif answer1 == "B" or answer1 == "b":
    extrovert_points += 2
    introvert_points -= 1
elif answer1 == "C" or answer1 == "c":
    ambivert_points += 1
print("")
answer2 = input("are you better at A listening, B talking, or C both?")
if answer2 == "A" or answer2 == "a":
    introvert_points += 1
elif answer2 == "B" or answer2 == "b":
    extrovert_points += 1
elif answer2 == "C" or answer2 == "c":
    ambivert_points += 1
print("")

answer3 = input("would you rather have A a cat, B a dog, or C a bunny?")
if answer3 == "A" or answer3 == "a":
    introvert_points += 1
elif answer3 == "B" or answer3 == "b":
    extrovert_points += 1
elif answer3 == "C" or answer3 == "c":
    ambivert_points += 1
print("")

answer4 = input("do you prefer A reading, B shopping, or C both?")
if answer4 == "A" or answer4 == "a":
    introvert_points += 1
elif answer4 == "B" or answer4 == "b":
    extrovert_points += 1
elif answer4 == "C" or answer4 == "c":
    ambivert_points += 1
print("")

answer5 = input("do you like to go A online shopping, B Shopping in person, or C both")
if answer5 == "A" or answer5 == "a":
    introvert_points += 2
elif answer5 == "B" or answer5 == "b":
    extrovert_points += 2 
elif answer5 == "C" or answer5 == "c":
    ambivert_points += 1
print("")

answer6 = input("do you think you wear more of A bright colors, B neutral colors, or C both")
if answer6 == "A" or answer6 == "a":
    extrovert_points == + 1
    ambivert_points == + 1
elif answer6 == "B" or answer6 == "b":
    introvert_points == + 1
    ambivert_points == + 1
elif answer6 == "C" or answer6 == "c":
    ambivert_points == +1
print("")

# end of the quiz: 
if extrovert_points > introvert_points and extrovert_points > ambivert_points:
    print("you are an extrovert! a social butterfly and super outgoing. you would rather spend time with others rather then by yourself. you are much more focused on external factors rather then internal thoughts and feelings.")
elif introvert_points > extrovert_points and introvert_points > ambivert_points:
    print("you are an introvert! you are much more quiet and like to observe things. you are a great listener and you focus on your internal thoughts and feelings much more then your social interactions.")
elif ambivert_points > introvert_points and ambivert_points > extrovert_points:
    print("you are an ambivert! you are a mix of outgoing and quiet usually depending on how comfortable you feel. you enjoy hanging out with friends but you also need time alone to balance things out.")
elif extrovert_points == introvert_points and extrovert_points == ambivert_points:
    print("you are a mix of everything so i can't decide what to call you!")
elif introvert_points == ambivert_points and introvert_points == extrovert_points:
    print ("you are a mix of everything so i can't decide what to call you!")
elif ambivert_points == extrovert_points and ambivert_points == introvert_points:
    print ("you are a mix of everything so i can't decide what to call you!")
