import sys

def translateToMorse(entry=None,fileName=None,fromMorse=False):
    """
    Takes one of the parameters(entry or fileName) and converts to Morse code or vice versa,
    either gets from file or as a entry. But, not at the same time.
    :param entry: 
    :param fileName:
    :param fromMorse:
    :return: 
    """
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

    # Checks if one of the parameters have entered
    assert not (entry != None and fileName != None), "only one param please"

    #If fileName parameter is entered, it is going to read as an entry
    if fileName is not None:
        entry = open(fileName,'r').read()

    #If translation will be going to occur from Morse code to alphabet
    if fromMorse is True:
        entry=entry.split(" ")
        reversedMatching = {v: k for k, v in matching.items()}
        matching=reversedMatching

    result = ""

    for character in entry:
        if character is not None:
            result += matching[character]
        else:
            pass

    #print(result)
    return result



if __name__ == '__main__':
    get_input = input

    if sys.version_info[:2] <= (2, 7):
        get_input = raw_input

    #There will be another parameter which is going to write result to a file.

    #################TESTING##################

    #translateToMorse(fileName="sample.txt",fromMorse=True) #works sample.txt contains "... -- ..."
    #translateToMorse(entry="mert")                         #works
    #translateToMorse(fileName="sample.txt")                #works sample.txt contains "sos"
    #translateToMorse("... --- ...",fromMorse=True)         #works

    """
       Will be used hopefully in GUI version

       if entry is None:
           entry=int(get_input("Entry: "))
       else:
           entry=entry[0]
    """