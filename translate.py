matching = {
        'A': '.-',              'a': '.-',
        'B': '-...',            'b': '-...',
        'C': '-.-.',            'c': '-.-.',
        'D': '-..',             'd': '-..',
        'E': '.',               'e': '.',
        'F': '..-.',            'f': '..-.',
        'G': '--.',             'g': '--.',
        'H': '....',            'h': '....',
        'I': '..',              'i': '..',
        'J': '.---',            'j': '.---',
        'K': '-.-',             'k': '-.-',
        'L': '.-..',            'l': '.-..',
        'M': '--',              'm': '--',
        'N': '-.',              'n': '-.',
        'O': '---',             'o': '---',
        'P': '.--.',            'p': '.--.',
        'Q': '--.-',            'q': '--.-',
        'R': '.-.',             'r': '.-.',
        'S': '...',             's': '...',
        'T': '-',               't': '-',
        'U': '..-',             'u': '..-',
        'V': '...-',            'v': '...-',
        'W': '.--',             'w': '.--',
        'X': '-..-',            'x': '-..-',
        'Y': '-.--',            'y': '-.--',
        'Z': '--..',            'z': '--..',
        '0': '-----',           ',': '--..--',
        '1': '.----',           '.': '.-.-.-',
        '2': '..---',           '?': '..--..',
        '3': '...--',           ';': '-.-.-.',
        '4': '....-',           ':': '---...',
        '5': '.....',           "'": '.----.',
        '6': '-....',           '-': '-....-',
        '7': '--...',           '/': '-..-.',
        '8': '---..',           '(': '-.--.-',
        '9': '----.',           ')': '-.--.-',
        ' ': ' ',               '_': '..--.-',
}

def translateToMorse(*entry,fileName=None):

    if fileName is not None:
        entry = open(fileName,'r').read()
        print("filename",entry)
    else:
        print("normal",entry)
        pass

    result = ""

    for character in entry:
        if character is None:
            raise IOError("Entry is empty")
        else:
            result += matching[character]

    print("result",result)
    return result

def translateFromMorse(entry): #not working

    result = ""

    for character in entry:
        if character == ' ':
            raise IOError("entry is empty")
        else:
            result += matching.get(entry)

    print(result)

if __name__ == '__main__':
    translateToMorse("mert")                #not working
    #translateToMorse(fileName="sample.txt") #works














    #translateFromMorse("...---...") #not working




    #entry="S"
    #print(matching.get(entry))