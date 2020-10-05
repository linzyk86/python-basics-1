import math

def incorrectPasscodeAttempts(passcode, attempts):
    # keep track of number of consecutive incorrect attempts
    incorrect_attempts = 0
    # iterate through the array
    for attempt in attempts: 
        if attempt != passcode: 
            incorrect_attempts += 1
        else:
            incorrect_attempts = 0
        if incorrect_attempts >= 10: 
            print(incorrect_attempts)
            return True
    return False

incorrectPasscodeAttempts("1111",["1111", 
 "4444", 
 "9999", 
 "3333", 
 "8888", 
 "2222", 
 "7777", 
 "0000", 
 "6666", 
 "7285", 
 "5555", 
 "1111"])
#########
def digitSumsDifference(n):
    digits = list(str(n))
    odds_list = []
    even_list = []
    diff = 0
    while n > 0 :
        current = n % 10
        if current % 2 == 0:
            even_list.append(current)
        else:
            odds_list.append(current)
        print(n, current, n/10, math.floor(n / 10))
        n = math.floor(n / 10)
    print(sum(even_list) - sum(odds_list))
digitSumsDifference(412)
#############
def countVowelConsonant(s):
    vowels = ['a', 'e', 'i', 'o','u']
    consonants = not vowels
    num_consonants = 0
    for letter in s:
        if vowels:
            num_vowels =  1
        else:
            num_consonants= 2   
    add = num_vowels+num_consonants
    print(add)
countVowelConsonant("kahfkhafhkahf")
