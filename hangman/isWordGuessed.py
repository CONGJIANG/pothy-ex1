def isWordGuessed(secretWord, lettersGuessed):

    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    
    '''
    rawAnswer = secretWord
    guess = lettersGuessed
    answer = [] # initialize a list(array)
    num = 0
    #print 'Secret Word: ', answer
    #print 'Letters Guessed: ', guess

    for i in rawAnswer:
        #print i
        answer.append(i)   # acquair secretWord array
    print answerList
    answerListSize = len(answerList)
    #print 'Size of SecretWord: ', answerListSize
        
    size = len(guess)
    for i in range(size):
        for j in range(answerListSize): 
            #print 'Guessed Letter:', guess[i]
            #print 'Secret Letter: ', j
            if guess[i] == answer[j]:
                print 'Very Happy'
                print 'Guessed Letter:', guess[i]
                print 'Secret Letter: ', j
                num += 1

    print 'Number of Same Letters: ', num     

    if answerListSize <= num:
        return True
    else:
        return False
