matching = {'A': '.-',  'B': '-...', 'C': '-.-.',
            'D': '-..', 'E': '.',    'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..',
            'J': '.---','K': '-.-',  'L': '.-..',
            'M': '--',  'N': '-.',   'O': '---',
            'P': '.--.','Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-',    'U': '..-',
            'V': '...-','W': '.--',  'X': '-..-',
            'Y': '-.--','Z': '--..', ' ': '/',
            
            '0': '-----', '1': '.----', '2': '..---',
            '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..',
            '9': '----.',

            "." : ".-.-.-", "," : "--..--", ":" : "---...",
            "?" : "..--..", "'" : ".----.", "-" : "-....-",
            "/" : "-..-.",  "@" : ".--.-.",
            "=" : "-...-"
            }

def translateToMorse():

    entry = input('Entry: ')

    result = []

    for character in entry:
        if character == ' ':
            raise IOError("entry is empty")
        else:
            result.append(matching[character.upper()])
            #not working
    print(result)
    return result

def translateFromMorse():

    entry = input('Entry: ')

    result = ""

    for character in entry:
        if character == ' ':
            raise IOError("entry is empty")
        else:
            result += matching.values([character.upper()])

    print(result)

if __name__ == '__main__':
    translateToMorse()
    #translateFromMorse()