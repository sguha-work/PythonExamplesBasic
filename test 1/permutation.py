userGivenWord = None
print ('Enter the word, program will print all permuted options')
userGivenWord = input()
print (f'The user provided word is "{userGivenWord}"')
lengthOfUserGivenWord = len(userGivenWord)
print (f'The number of charecters of user given word is: "{lengthOfUserGivenWord}"')
print (f'The number of {lengthOfUserGivenWord} charecters words which can be prepared using charecters form "{userGivenWord}" is {lengthOfUserGivenWord}!.')
print (f'{lengthOfUserGivenWord}! means')
index=1
numericalResult = 1
stringResult = ''
while index<=lengthOfUserGivenWord:
    stringResult += str(index) + '*'
    numericalResult *= index
    index += 1
stringResult = stringResult[0:-1]
print (f'{stringResult} = {numericalResult}')
