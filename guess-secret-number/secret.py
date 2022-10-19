from random import randint as gen

def gen_secret():
    return ''.join(str(gen(1,8)) for i in range(4))

def check_guess(num,secret_num):

    number_guess_correct = 0
    number_guess_wrong = 0
    num,s_num = str(num), str(secret_num)

    for index in range(len(s_num)):
        if not (num[index] in s_num) and not (num[index] == s_num[index]):
            number_guess_wrong += 1
        elif (num[index] in s_num) and (num[index] == s_num[index]):
            number_guess_correct += 1
        else:
            number_guess_wrong += 1

    return {'correct': number_guess_correct,
            'wrong': number_guess_wrong}


secret = int(gen_secret())
guess_left = 12
# print(secret)
print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
while not guess_left == 0:

    guess = input('Input 4 digit code: ')

    if not guess.isdigit():
        print('Please enter a valid number')
    elif len(guess) < 4 or len(guess) > 4:
        print('Please enter exactly 4 digits.')
    else:
        check = check_guess(int(guess),secret)
        if int(guess) == secret:
            print(f"correct numbers: {check['correct']}",f"wrong numbers: {check['wrong']}",sep='\n')
            print('Correct the was : {}'.format(secret))
            break
        else:
            print(f"correct numbers: {check['correct']}",f"wrong numbers: {check['wrong']}",sep='\n')
            guess_left -= 1

else:

    print('You have run out of guesses')

