import time
# Dictionary representing the morse code chart
# Dictionaries store data in this form: { 'Key': 'Value'}
morse = []
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
                    '(':'-.--.',' ': ' ', ')':'-.--.-'}

# Accessing dictionary key/value pairs using a list
print("############# DICTIONARY ##############")
print(DICT)
print("\n\n")

morkeys = list(DICT)
morvals = list(DICT.values())

##printing list of keys
#print("############# LIST OF KEYS ##############")
#print(morkeys)
#print("\n\n")
#
#
##printing list of values
#print("############# LIST OF VALUES ##############")
#print(morvals)
#print("\n\n")
#
#print("############# KEY INDEX ##############")
## through indexing keys or values
#print("Key: " + morkeys[0])
#print("\n\n")
#
#print("############# VALUE INDEX ##############")
#print("Value: " + morvals[0])
#print("\n\n")
#
#print("############# EXAMPLE OF ACCESS DICT['A'] ##############")
#print("A : " + DICT['A'])
#print("\n\n")



#######################################PSEUDO C?ODE##########################################
#Introduce app with a welcome messge translated into morse code??
#Make option (maybe with keyboard buttons or something else to switch between morse/english or english/morse)
#maybe make it roboust enough to just type something and translates it and do this infinitely; unless special key is pressed to switch between languages
#translate sentence accordingly
#
#- display welcome message only once, showing options/buttons that can be used; think of a main menu
#- based on what user inputs for menu go to that function
#- using input varibale ask user what should be translated;
#- store that sentence into a list/array 
#- parse through sentence to decipher the message by comparing to dictionary OR simply passing to Dictionary and outputting its values
#- repeat process until another button is pressed or app is exited

print("Hello <user>, welcome to the morse translator gadget tool thing, \n")
time.sleep(.5)
print("what are you trying to do today?")
time.sleep(.5)

while True: 
    
    print("\n(a) translate ENGLISH to MORSE \nOR\n(b) translate MORSE to ENGLISH (ctrl-z to exit)\n")
    user_in = input("type a or b and press enter: ")
    if(user_in == 'a'):
        print("very well, guess you don't know much morse. Let's see if you even know english.")
        word = input("Type a sentence you want me to translate: ")
        print("so.. you want me to translate '"+word+"'?\nfine, but first, let me think about how to write this program first.")
        sentence = list(word.upper())
        sen_len = len(sentence)
        print(sentence)
          
        for i in range(sen_len):
            morse.append(DICT[sentence[i]])
        print(morse) 
        translation = ''.join(morse)
        print("\n\nTranslated word: ")
        print(translation)
    elif(user_in == 'b'):
        print("Please. You can barely speak english, lets start with option a. restart the program and try again.")
    else:
        print("invalid answer, seriously? there's only two options.. try again")
    time.sleep(1)
