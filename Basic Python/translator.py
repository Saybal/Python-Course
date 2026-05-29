def translator(sentence):
    translate = ''
    for letter in sentence:
        if letter in 'AEIOUaeiou':
            translate += 'g'
        else:
            translate += letter
    return translate;

sen = input("Enter a sentence: ")
trans = translator(sen)
print(trans)