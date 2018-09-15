import random
import copy

def only_integers(a):
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  for i in a:
    if i not in numbers:
      return False
  return True

def check_int_and_in_list(x, b):
  if only_integers(x) == True:
    if int(x) <= b[len(b) - 1]:
      return True
  return False

def mastermind():
    print "   This game is called Mastermind. Your goal is to correctly guess the 5-digit code. After each guess you will be told how many numbers you got exacly right and how many numbers you guessed that were in the code but not in the correct position. You have 10 tries to correctly guess the code. Good luck."
    code = []
    
    print "" # To help with the spacing
    
    level_of_difficulty = raw_input("   Do you want to play the easy, modedrate, or hard mode? In the easy mode the code will involve 5 unique digits for the digits 0 to 9. In the moderate mode the code will only involve the numbers 0 to 6 and can have repeated digits. In the hard mode uses the numbers 0 to 9 and can also have repeated digits (respond with either easy, moderate, or hard) " )
    print ""
    
    # This makes sure that the user puts in an acceptable response to the level of difficulty
    while level_of_difficulty != 'easy' and level_of_difficulty != 'moderate' and level_of_difficulty != 'hard':
      level_of_difficulty = raw_input("You have to answer with either easy, moderate, or hard. What level would you like to play?") 
      print ""
    
    # Asks the user if they want the in-game notes
    notes = raw_input("Do you want to play with the on screen notes or not?")
    print ""
    
    # Makes sure that the user puts in an acceptable respond for whether they want notes or not
    while notes != 'yes' and notes != 'no':
      notes = raw_input("You must respond with either yes or no. Do you want to play with the on screen notes or not?")
      print ""
    
    # If the uuser want the notes then asks if the user wants to use x's or no's in the notes
    if notes == 'yes':
      type_notes = raw_input("Do you want to play the notes with x's or no's? respond with either no or x.")
      print ""
      
      # Makes sure that the user inputs a correct response to what type of notes they want
      while type_notes != 'x' and type_notes != 'no':
        type_notes = raw_input("  You must answer with either no or x. Do you want to play the notes with x's or no's? respond with either no or x.")
        print ""
    
    if level_of_difficulty == "easy":              # This randomly selects 5 distinct digits to form code
      numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
      for i in range(0,5):
        a = random.randint(0,9-i)
        code.append(numbers[a])
        del numbers[a]

    if level_of_difficulty == 'moderate':             # This randomly selects 5 digits to form the code from the digits 0 through 6
      for i in range (0,5):        
        a = random.randint(0,6)
        code.append(a)

    if level_of_difficulty == "hard":
      for i in range (0,5):        # This randomly selects 5 digits to form the code from the digits 0 through 9
        a = random.randint(0,9)
        code.append(a)
      
    code_string = ""               # Creates a string version of the code
    for i in range(0,5):
      code_string += str(code[i])
    
    tries = 0 
    condtitional = False
    if notes == 'yes':
      if type_notes == 'no':
        possible_number_positions = {0 : ['__','__','__','__','__'],
          1 : ['__','__','__','__','__'],
          2 : ['__','__','__','__','__'],
          3 : ['__','__','__','__','__'],
          4 : ['__','__','__','__','__'],
          5 : ['__','__','__','__','__'],
          6 : ['__','__','__','__','__'],
          7 : ['__','__','__','__','__'],
          8 : ['__','__','__','__','__'],
          9 : ['__','__','__','__','__']
          } # This is the dictionary of possible number positions if the user wants to play with no's
          
      else:
        possible_number_positions = {0 : ['_','_','_','_','_'],
          1 : ['_','_','_','_','_'],
          2 : ['_','_','_','_','_'],
          3 : ['_','_','_','_','_'],
          4 : ['_','_','_','_','_'],
          5 : ['_','_','_','_','_'],
          6 : ['_','_','_','_','_'],
          7 : ['_','_','_','_','_'],
          8 : ['_','_','_','_','_'],
          9 : ['_','_','_','_','_']
          } # This is the dictionary of possible number positions if the user wants to play with x's
      if level_of_difficulty == 'moderate':
            del possible_number_positions[7]
            del possible_number_positions[8]
            del possible_number_positions[9]  
      possible_number_positions_original = copy.deepcopy(possible_number_positions)# This is the dictionary of possible number positions if the user wants to play with x's

    count = 0
    
    while tries < 10:   # So that you only have ten tries to guess the sequence
        guess = []
        tries += 1 # Increases tries each time

        guess_number = raw_input("What is your guess? ") # Asks for the players guess
        print ""
        
        while len(guess_number) != 5 and guess_number!= '000000' and guess_number != '000001' and guess_number != '000002':
          guess_number = raw_input("Your guess must contain 5 digits. What is your guess? ") # Asks for the players guess if their original guess is not acceptable
          print ""

        # Resets flags that may be changed if a cheat code in added
        bull_and_cow_flg = True  
        notes_flg = True

        # Cheat Codes
        if guess_number == '000000':            # This creates a cheat code so that when the player enters 000000 the computer will print the code
            print "The code is " + code_string + "."
            if tries == 9:
              print "You have 1 try left."
            else:  
              print "You have " + str(10-tries) + " tries left."
            print ""
            bull_and_cow_flg = False
        if guess_number == "000001":            # This creates a cheat code so that when the player enters 000001 the ccomputer will give the player an extra try
          tries = tries - 2
          print "You have " + str(10-tries) + " tries left."
          print ""
          bull_and_cow_flg = False
          notes_flg = False # since this cheat code doesn't give the user any information the notes shouldn't come up
        if guess_number == '000002':
          # This cheat code ends the game and results in the player losing
          print "big mistake..."
          print ""
          bull_and_cow_flg = False
          notes_flg = False
          tries = 10 

        if bull_and_cow_flg: # This way the computer doesn't check the imput against the code if the input is one of the cheat codes
            bulls = 0
            cow = 0
            for i in range(0,5):                    # This turns the guess into a list
                guess.append(int(guess_number[i]))
                
            # This checks for exact matches
            for i in range(0,5):
                if guess[i] == code[i]:
                    bulls += 1

            # This sets up the list for the simplified version of the guess and creates a dictionary that will be used to store to frequence of each number in the guess
            simplified_guess = []
            dictionary_guess = {0 : 0,
              1 : 0,
              2 : 0,
              3 : 0,
              4 : 0,
              5 : 0,
              6 : 0,
              7 : 0,
              8 : 0,
              9 : 0
            }
            
            # This breaks the guess up into a list that only contains the unique digits in the guess
            simplified_guess.append(guess[0])

            if guess[1] != guess[0]:
                simplified_guess.append(guess[1])

            if guess[2] !=guess[1] and guess[2] != guess[0]:
                simplified_guess.append(guess[2])

            if guess[3] != guess[2] and guess[3] != guess[1] and guess[3] != guess[0]:
                simplified_guess.append(guess[3])
                
            if guess[4] != guess[3] and guess[4] != guess[2] and guess[4] != guess[1] and guess[4] != guess[0]:
                simplified_guess.append(guess[4])
            
            # This breaks the guess into a dictionary that stores the frequency of each number
            for i in range(0, len(simplified_guess)):
              for element in range(0, len(guess)):
                if guess[element] == simplified_guess[i]:
                  dictionary_guess[simplified_guess[i]] += 1
                  
          # This sets up the list for the simplified version of the code and creates a dictionary that will be used to store to frequence of each number in the code
            simplified_code = []
            dictionary_code = {0 : 0,
              1 : 0,
              2 : 0,
              3 : 0,
              4 : 0,
              5 : 0,
              6 : 0,
              7 : 0,
              8 : 0,
              9 : 0
            }
            
            # This breaks the code up into a list that only contains the unique digits in the code
            simplified_code.append(code[0])

            if code[1] != code[0]:
                simplified_code.append(code[1])

            if code[2] !=code[1] and code[2] != code[0]:
                simplified_code.append(code[2])

            if code[3] != code[2] and code[3] != code[1] and code[3] != code[0]:
                simplified_code.append(code[3])
                
            if code[4] != code[3] and code[4] != code[2] and code[4] != code[1] and code[4] != code[0]:
                simplified_code.append(code[4])
            
            # This breaks the code into a dictionary that stores the frequency of each number
            for i in range(0, len(simplified_code)):
              for element in range(0, len(code)):
                if code[element] == simplified_code[i]:
                  dictionary_code[simplified_code[i]] += 1

            # This checks the two dictionaries for which one has the lower value for each number and then adds that value to the cow variable
            for i in range(0,10):
              if dictionary_code[i] >= dictionary_guess[i]:
                cow += dictionary_guess[i]
              else:
                cow += dictionary_code[i]
              
            
            cows = cow - bulls # Gets the number of correct numbers that are not in the correct spots

            if bulls == 5: # Cases for if the player wins
                condtitional = True
                if tries == 1:
                    print "You Win!"
                    print "It took you " + str(tries) + " try."
                else:
                    print "You win!"
                    print "It took you " + str(tries) + " tries."
                break

            else: # Reports results of the players guess for so that they can use that information to try again
                
                if bulls == 1:
                  print "You got " + str(bulls) + " number exactly correct"
                else:
                  print "You got " + str(bulls) + " numbers exactly correct"
                
                
                if cows == 1:
                  print "You got " + str(cows) + " number that is in the code but not in the correct position."
                else:
                  print "You got " + str(cows) + " numbers that are in the code but not in the correct position."
                if tries == 9:
                  print "You have 1 try left."
                else:  
                  print "You have " + str(10-tries) + " tries left."
                print ""
        
        # This if statement makes sure that if the user enters moderate as the level of difficulty then it will delete the last three rows for the possible positions
        if notes == 'yes' and notes_flg == True and tries != 10:
          print 'Your notes are:'
          for i in possible_number_positions:
            print str(i) + ": " + str(possible_number_positions[i])
          print ""
          
          if count % 2 == 0:
            possible_number_positions1 = copy.deepcopy(possible_number_positions)
            count += 1
          else:
            possible_number_positions2 = copy.deepcopy(possible_number_positions)
            count += 1
          print ''
          
          useless_numbers = raw_input("Would you like to delete any numbers from this list? Respond with either 'no' or the numbers you would like to delete (separate them with a comma). You may also respond with 'go back one step' to reset the notes to the notes from your last guess or 'reset notes' to reset the notes to their original version.") # Asks the user if they want to delete any numbers from the list
          
          print ''
          # Makes sure that the user either enters an integer in the list of possible numbers or enters no
          '''while useless_numbers != 'no' and check_int_and_in_list(useless_numbers, possible_numbers) == False:
            useless_numbers = raw_input("You must respond with either an integer in the list or no. Would you like to delete any numbers from this list? Respond with either no or the numbers you would like to delete (put them in a list).")'''
          
          # This deletes the useless numbers from the possible number positions and prints the updated dictionary
          while useless_numbers == 'go back one step':
            if count % 2 == 0:
              possible_number_positions = copy.deepcopy(possible_number_positions1)
              
            else:
              possible_number_positions = copy.deepcopy(possible_number_positions2)
            
            print 'Your updated notes are:'
            print ''
            for i in possible_number_positions:
              print str(i) + ": " + str(possible_number_positions[i])
            print ""
              
            useless_numbers = raw_input("Would you like to delete any numbers from this list? Respond with either 'no' or the numbers you would like to delete (separate them with a comma). You may also respond with 'reset notes' to reset the notes to their original version.") # Asks the user if they want to delete any numbers from the list
            
          while useless_numbers == "reset notes":
            possible_number_positions = possible_number_positions_original
            
            print 'Your updated notes are:'
            print ''
            for i in possible_number_positions:
              print str(i) + ": " + str(possible_number_positions[i])
            print ''
            
            useless_numbers = raw_input("Would you like to delete any numbers from this list? Respond with either no or the numbers you would like to delete (separate them with a comma)") # Asks the user if they want to delete any numbers from the list
            print ''
            
          if useless_numbers != 'no' and useless_numbers != 'go back one step' and useless_numbers != 'reset notes':
            useless_numbers = useless_numbers.replace(' ', '')
            useful_list = useless_numbers.split(',')
            for i in useful_list:
              del possible_number_positions[int(i)]
            for i in possible_number_positions:
              print str(i) + ": " + str(possible_number_positions[i])
          print ""
          
          useless_positions = raw_input("Would you like to eliminate any positions? Respond with number : position, ... For example if you wanted to eliminate 0 for the first position you would respond 0:1. You can also respond with no.") # This asks the user about any useless positions that they want to delete from the possible number positions
          print ''
          
          if useless_positions != 'no':
            useless_positions = useless_positions.replace(' ','')
            useful_positions = useless_positions.split(',')
          
            for element in useful_positions:
              i = element.split(':')
              x = possible_number_positions[int(i[0])]
              if type_notes == 'no':
                x[int(i[1])-1] = 'No'
              else:
                x[int(i[1])-1] = 'x'
              possible_number_positions[int(i[0])] = x
          
            print 'Your updated notes are:'
            for i in possible_number_positions:
              print str(i) + ": " + str(possible_number_positions[i])
            print ""
          else:
            print 'Your updated notes are:'
            for i in possible_number_positions:
              print str(i) + ": " + str(possible_number_positions[i])
            print ""
            
        if tries == 10 and condtitional == False: # If they take too many tries then prints a you lose statement
          print "You lose :("
          print "The correct code was " + code_string
          print ""
          
    return "Good game"
print mastermind()
