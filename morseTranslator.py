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

    #writes result to specified file if entered
    if writeToFile is not None:
        newFile = open(writeToFile, 'w').write(result)
    else:
        #pygame.mixer.pre_init(22050,16,2,4096)

        import pygame


        pygame.init()
        pygame.mixer.get_init()
        #os.getcwd()

        dotSound = pygame.mixer.Sound('dotSound.mp3')
        dashSound = pygame.mixer.Sound('dashSound.mp3')

        for character in result:
            if character is ".":
                pygame.mixer.Sound.play(dotSound)
                #dotSound.play()
                time.sleep(1)
                #dotSound.stop()
            if character is "-":
                pygame.mixer.Sound.play(dashSound)
                #dashSound.play()
                time.sleep(1)
                #dashSound.stop()
        print(result)
        return result


if __name__ == '__main__':
    import sys
    import pygame, time, os
    from pygame.locals import *

    get_input = input

    #If python2 is used, func still can work
    if sys.version_info[:2] <= (2, 7):
        get_input = raw_input

    morseTranslator(entry="sos")




