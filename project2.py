from random import randint
from random import shuffle

def main():

    print("Welcome to CRYPTO_LOGIC! Try to guess the scrambled word, one letter at a time.")

    wordlist = get_word_list()              

    repeat = True

    while (repeat):

        incorrectguesses = 0

        secret = get_next_word(wordlist)        

        scrambled_secret = scramble_word(secret) 

        correctguesses = []
    
        currentletter = 0
    
        while(len(correctguesses) != len(scrambled_secret)):
        
            print_word(scrambled_secret)
            print_word(correctguesses)
            print("Incorrect guesses: " + str(incorrectguesses))
        
            guess = input("Your guess? ").upper()
        
            if(guess == secret[currentletter]):
            
                correctguesses.append(guess)
                currentletter += 1
            
            else:
            
                incorrectguesses += 1
            

        print("Congratulations! You guessed the word: ")
        print_word(secret)

        play_again = input("Do you want to play again (Y/N)? ").upper()

        if (play_again == "N"):
            repeat = False

    print("Thanks for playing!")

def scramble_word(secret):

    secret_copy = list(secret)
    shuffle(secret_copy)
    return secret_copy

def get_next_word(wordlist):

    choice = randint(0,len(wordlist)-1)
    secretword = (wordlist[choice]).upper()
    secretwordlist = list(secretword)
    return secretwordlist

def get_word_list():
    
    inputFile= open('wordlist.txt', 'r')
    line = inputFile.readline()
    wordlist = []

    while( len(line) > 0 ):
        line = line.strip().upper()
        wordlist.append(line)
        line = inputFile.readline()

    inputFile.close()
    return wordlist
    

def print_word(word):
    
    print("".join(word))

main()
