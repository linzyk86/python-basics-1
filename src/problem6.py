def threeCharsDistinct(s):
    num_distinct = 0
    # keep a count of num distinct triplets
    # iterate through the characters in s: 
    for i in range(0, len(s) - 2): 
        # get the triplet
        substring = s[i:i+3]
        # check if they're all distinct
        # check the count of each character
        substring_chars = set(substring)
        if len(substring_chars) == 3: 
            num_distinct += 1
        
    print(num_distinct)
threeCharsDistinct("abcdaaae")