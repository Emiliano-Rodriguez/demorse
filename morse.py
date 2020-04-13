


# Dictionary representing the morse code chart 
# Dictionaries store data in this form: { 'Key': 'Value'}
DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 

# Accessing dictionary key/value pairs using a list 
print("############# DICTIONARY ##############")
print(DICT)
print("\n\n")

morkeys = list(DICT)
morvals = list(DICT.values())

#printing list of keys
print("############# LIST OF KEYS ##############")
print(morkeys)
print("\n\n")


#printing list of values
print("############# LIST OF VALUES ##############")
print(morvals)
print("\n\n")

print("############# KEY INDEX ##############")
# through indexing keys or values
print("Key: " + morkeys[0])
print("\n\n")

print("############# VALUE INDEX ##############")
print("Value: " + morvals[0])
print("\n\n")

print("############# EXAMPLE OF ACCESS DICT['A'] ##############")
print("A : " + DICT['A'])
