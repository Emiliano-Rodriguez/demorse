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

morkeys = list(DICT)
morvals = list(DICT.values())

def encrypt(message):
    my_cipher = ''
    for myletter in message:
        if myletter != ' ':
            my_cipher += DICT[myletter] + ' '
        else:
            my_cipher += ' '
        return my_cipher

def main():
    my_message = "SIMP"
    output = encrypt(my_message.upper())
    print(my_message + ": " + output)
if __name__ == '__main__':
    main()
