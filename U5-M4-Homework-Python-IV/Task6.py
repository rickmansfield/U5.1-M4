"""
- initialize index to zero
- initialize empty string to variable new_word
- initialize alphabet to all leters in the alphabet
- loop over eachLetter in the inputString (convert to lower case inline)
    - conditionals
    - if the string char is a letter 
        - set index to alphabet.index +1
        - set new_word to alphabet[index] +1
    - else if the char is not a letter
        - add each char to the new_word 
-return new_word

"""
def alphabeticShift(inputString):
    index = 0
    new_word = ""
    alphabet = "abcdefghijklmnopqrstuvwxyzacd"
    for eachLetter in inputString.lower():
        if eachLetter.islower(): #check if eachLetter is a lower case letter
            index = alphabet.index(eachLetter) + 1 #get the index of the following letter
            new_word += alphabet[index]    
        else: #if not letter
            new_word += eachLetter    
    return new_word

print(alphabeticShift("crazy")) # dsbaz