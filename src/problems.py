

def oddNumbersBeforeZero(sequence):

    result = 0
    for i in range(0, len(sequence)):
        if sequence[i] == 0:
            break
        if sequence[i] % 2 == 1:
            result += 1
    return result
    
oddNumbersBeforeZero([1, 2, 3, 0, 4, 5, 6, 0, 1])

def split_in_parts(s, part_length):
    # Your code here
    #create a variable for the new string
    return_list = []

    #loop through
    for letter in s:
        print(letter)

    #string_slice = s
split_in_parts("supercalifragilisticexpialidocious", 3)
# Your code here