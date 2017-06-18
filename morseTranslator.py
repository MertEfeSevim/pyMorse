import sys
import os
import time


def morseTranslator(entry=None, fromFile=None, fromMorse=False, writeToFile=None):
    """
    Takes one of the parameters(entry or fileName) and converts to Morse code or vice versa,
    either gets from file or as a entry.
    :param entry: 
    :param fromFile:
    :param fromMorse:
    :param writeToFile:
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
        '':''
}

    # Checks if one of the parameters have entered
    assert not (entry != None and fromFile != None), "Entry and fileName can not be used together"

    #If fileName parameter is entered, it is going to read as an entry
    if fromFile is not None:
        entry = open(fromFile, 'r').read()

    #If translation will be going to occur from Morse code to alphabet
    if fromMorse is True:
        entry=entry.split(" ")
        reversedMatching = {v: k for k, v in matching.items()}
        matching=reversedMatching

    #changes the characters and adds to result
    result = ""

    for character in entry:
        if character!='' and fromMorse is True:
            result += matching[character]
        else:
            result += matching[character] + " "

    if (fromMorse==False):
        message=result
    else:
        message=""
        for i in entry:
            for j in i:
                message+=j

    #if os.name() == "linux" or "linux2":
        #beep function will be in here (linux)
    if os.name == "darwin":
        import Carbon.Snd #beep function will be in here (Mac)
        for i in message:
            if i == ".":
                Carbon.Snd.SysBeep(0.15)
            elif i == "-":
                Carbon.Snd.SysBeep(0.4)

    elif os.name == "win32" or os.name == "nt":
        import winsound
        print(message)
        for i in message:
            if i == ".":
                winsound.Beep(1160,150)
            elif i == "-":
                winsound.Beep(1200,400)

    #writes result to specified file if entered
    if writeToFile is not None:
        newFile = open(writeToFile, 'w').write(result)
    else:
        print(result)
        return result


if __name__ == '__main__':
    get_input = input
    morseTranslator(entry="... --- ...",fromMorse=True)

    #If python2 is used, func still can work
    if sys.version_info[:2] <= (2, 7):
        get_input = raw_input