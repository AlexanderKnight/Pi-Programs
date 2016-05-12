def Collatz(N):
    '''
    This method produces the next number in a collatz sequence.
    It follows the following logic:
    N_{n+1} = N_n/2 if even
    N_{n+1} = N_n*3+1 if odd
    It then returns N_{n+1}
    '''
    
    if N%2 ==0:
        return int(N/2)
    else:
        return int(3*N+1)

print("Hello, I am here to print a Collatz sequence")
print("Do you know what a Collatz sequence is? (y/n)")

#This asks if the user knows what a collatz sequence is, and explains if not
checker = 0
while checker==0:
    knowledge = input()
    if knowledge == 'n': #Explains rules
        print("The rules are simple:")
        print("Pick a natural number (non-zero, non-negative integer)")
        print("If the number is even, divide it by two")
        print("If the number is odd, multiply it by three and add one")
        print("Now take this new number, and repeat the process.")
        print("Do this long enough, and you will get to one. \n")
        checker = 1
    elif knowledge == 'y': #Skips and compliments
        print("You are pretty smart then. \n")
        checker = 1
    else: #Error proofing, and redirecting
        print("Please answer (y/n). I am too simple to process anything else.")
repeat = True

#This starts the actual sequencing program, which will repeat until quitted
while repeat == True:
    print("Please type in a natural number:(eg, 7, not 'seven')") #asks for a number
    checker = 0
    while checker==0:
    
        try:
            N = int(input()) #Gets number from user
            if N == 0:
                print("That is not a natural (non-zero) number")#checks for zero
            elif N<0:
                print("That is not a natural (non-negative) number")#checks negativec
            else:
                checker =1
        except:
            print("That is not a natural number")#shows if not an integer
    run = 0 #starts a counter to show number of steps to reach 1
    while N!=1: #starts collatz sequence, continues until 1 is reached
        print(N)
        N = Collatz(N)
        run+=1
    print(N)
    print("It took %i steps to complete the sequence"%(run)) #prints the number of steps
    repeatTest = True
    while repeatTest == True: #asks if you want to repeat the collatz sequence
        print("Would you like to repeat this? (y/n)")
        repeatQuestion = input()

        if repeatQuestion =='n':
            print("I hope you had fun. Thank you.")
            repeatTest = False
            repeat = False
        elif repeatQuestion =='y':
            repeatTest = False
        else:
            print("Please answer (y/n)")
 
            
