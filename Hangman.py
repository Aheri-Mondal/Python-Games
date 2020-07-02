
import random
import sys
class HangMan(object):
    
    #Hanging Stand
    hang = []
    hang.append(' +---+')
    hang.append(' |   |')
    hang.append('     |')
    hang.append('     |')
    hang.append('     |')
    hang.append('     |')
    hang.append('=======')
    
    #The hanging man
    man = {}
    man[0] = [' 0   |']
    man[1] = [' 0   |', ' |   |']
    man[2] = [' 0   |', '/|   |']
    man[3] = [' 0   |', '/|\\  |']
    man[4] = [' 0   |', '/|\\  |', '/    |']
    man[5] = [' 0   |', '/|\\  |', '/ \\  |']
    
    pics = []

    #taking words from Words_hangman.txt file
    f=open("Words_hangman.txt", "r")
    f1=f.readlines()
    words=[]

    for i in range(len(f1)):
        words.append(f1[i].strip("\n"))#Removing new line character,if any, within the array

    infStr="\n+_^+_+^+_+^+_+^+_+^+_+^+_+^+_+^+_+^+_+^+\n"
  
    #creating the hangman picture array
    def __init__(self, *args, **kwargs):
        i, j = 2, 0
        self.pics.append(self.hang[:])
        for ls in self.man.values():
            pic, j = self.hang[:], 0
            for m in ls:
                pic[i + j] = m
                j += 1
            self.pics.append(pic)

    def pickWord(self): #Random word is being chosen
        return self.words[random.randint(0, len(self.words) - 1)]
    
    def printPic(self, idx, wordLen): #func to print hangman pic
        for line in self.pics[idx]:
            print(line)
            
    def askAndEvaluate(self, word, result, missed):
        guess = input()
        guess = guess.lower()#converting input character into lowercase
        
        #Checking for invalid input
        if guess == None or len(guess) != 1 or (guess in result) or (guess in missed) or (guess<'a') or (guess>'z'):
            return None, False
            
        i = 0
        right = guess in word #Checking if the entered alphabet is present in the word
        for c in word:
            if c == guess:
                result[i] = c #Replacing the '*' with the entered alphabet wherever present 
            i += 1
        return guess, right

    def info(self, info):
        ln=len(self.infStr)
        print(self.infStr[:-3])
        print(info)
        print(self.infStr[3:])
            
    def start(self):
        print('Welcome to Hangman !')
        print("Rules: \n 1.You have to guess a word by guessing the missing alphabets. \n 2.You have total 5 chances.On giving incorrect answer for the 6th time, the man hangs!")
        print("Enter your name please")
        name=str(input()) #Taking name of the player
        word = list(self.pickWord())
        result = list('*' * len(word))#Printing '*' in place of the alphabets
        print('The word is: ', result)
        success, i, missed = False, 0, []
        while i < len(self.pics)-1:
            print('\nGuess the word: ', end='')
            guess,right = self.askAndEvaluate(word, result, missed)

            if guess == None: #When the input is invalid
                print('You have already entered this character or invalid input')
                continue
            print("\n",''.join(result),"\n")
            if result == word:
                self.info(f'\nCongratulations {name}! You have just saved a life !\n')
                user_input = input('Press C to play again or any other key to quit\n')[0]
                 
                if user_input =='c' or user_input=='C':#To play again
                    a = HangMan().start()

                if user_input!= 'c' or user_input!='C':#To quit game
                    sys.exit()   

                success = True
                break
            if not right:
                missed.append(guess)
                i+=1 #Counting the number of missed chances
            self.printPic(i,len(word))
            print('Missed characters: ', missed)#Printing the missed characters
        
        if not success:
            self.info('\nThe word was \''+''.join(word)+f'\' {name}, you have just killed a man! Better luck next time.\n')
            user_input = input('Game over, press C to play again or any other key to quit\n')[0]
            
            if user_input =='c' or user_input=='C':#To play again
                a = HangMan().start()   

            if user_input!='c' and user_input!='C':#To quit game
                sys.exit()    

           

a = HangMan().start()