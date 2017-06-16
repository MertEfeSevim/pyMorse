import sys

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

def translateToMorse(entry=None,fileName=None):
    """
    Will be used hopefully in GUI version
     
    if entry is None:
        entry=int(get_input("Entry: "))
    else:
        entry=entry[0]
    """

    assert not (entry != None and fileName != None), "only one param please"

    if fileName is not None:
        entry = open(fileName,'r').read()
        print("filename",entry)
    else:
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
    get_input = input

    if sys.version_info[:2] <= (2, 7):
        get_input = raw_input

    #translateToMorse(entry="mert")             #works
    #translateToMorse(fileName="sample.txt")    #works

    #translateFromMorse("...---...") #not working
    #entry="S"
    #print(matching.get(entry))