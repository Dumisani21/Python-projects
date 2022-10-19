'''
Nine lives games
'''
from random import randint as select

lives = 9
word_compeleted = False

def request_words():

    # pull words from the words.txt file
    file_name = "words.txt"
    with open(file_name,'r') as f:
        words = f.readlines()
        f.close()

    return words


def request_word():

    words = request_words()
    word = words[select(0,len(words)-1)]
    word = word.strip()
    guess = []


    for letter in word:
        guess.append('?')

    return {'guess':guess, 'correct':word}


def check_word(guess,correct,answer):

    build_word = ''
    global word_compeleted
    for letter in guess:
        build_word += letter

    if build_word == correct:
        word_compeleted = True

    if len(answer) > 1:

        if answer == correct:

            return {"msg":f"You won! The secret word was: {correct}","code":1}
        
        else:

            return {"msg":"Incorrect. You lose a life","code":0}

    else:

        if answer in correct:

            for i in range(len(correct)):

                if answer == guess[i]:
                    pass
                else:
                    for i in range(len(correct)):

                        if answer == guess[i]:
                            pass
                        else:
                            if correct[i] == answer and not answer == guess[i]:
                                guess.pop(i)
                                guess.insert(i,answer)
                                if build_word == correct:
                                    word_compeleted = True

            return {"code":2}
        return {"msg": "Incorrect. You lose a life","code":0} 


def request_live():

    lives_icon = ""

    for index in range(lives):

        lives_icon +="♥"

    return f"Lives left: {lives_icon}"


def prompt(cmd):

    cmd1 = ''

    while True:

        cmd1 = input(cmd)

        if cmd1 == "":

            pass
        else:
            break

    return cmd1


selected_word = request_word()

while not lives == 0 or word_compeleted:

    # print(selected_word["correct"])

    if word_compeleted == True:
        break

    # print(word_compeleted)

    print(selected_word["guess"])
    print(request_live())
    cmd = prompt("Guess a letter or the whole word: ")

    check = check_word(selected_word["guess"],selected_word["correct"],cmd)

    if lives == 0:

        break

    if check["code"] == 0:
        lives = lives - 1
        print(check["msg"])

    elif check["code"] == 1:

        print(check["msg"])
        break
    else:
        pass
