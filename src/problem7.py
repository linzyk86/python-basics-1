def reverseSentence(sentence):
    word = sentence.split(" ") 
    words = (word[::-1])
    # print(words)
    return (' '.join(words))
print(reverseSentence("Man bites dog"))