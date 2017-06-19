class pyMorse(object):
    def morseTranslator(entry=None, fromFile=None, fromMorse=False, writeToFile=None, playSound=False):

        """
        Takes one of the parameters(entry or fileName)
        and converts to Morse code or vice versa,
        also able to play sounds of translations.

        :param entry:
        :param fromFile:
        :param fromMorse:
        :param writeToFile:
        :param playSound:
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

        # Checks if parameters have entered properly
        assert not (entry != None and fromFile != None), "Entry and fileName can not be used together"
        assert not (fromMorse == True and playSound == True), "Only Morse code can be voiced"

        #If fileName parameter is entered, it is going to read as an entry
        if fromFile is not None: entry = open(fromFile, 'r').read()

        #If translation will be going to occur from Morse code to alphabet
        if fromMorse is True:

            entry = entry.split(" ")
            reversedMatching = {v: k for k, v in matching.items()}
            matching = reversedMatching

        #changes the characters and adds to result
        result = ""

        for character in entry:

            if character!='' and fromMorse is True:
                result += matching[character]
            else:
                result += matching[character] + " "

        #writes result to specified file if entered
        if writeToFile is not None: newFile = open(writeToFile, 'w').write(result)

        #plays result as sound if fromMorse is False
        if playSound is True:

            try :
                import pygame, time

            except ImportError:
                raise ImportError("You need to import PyGame to use this feature")

            else:
                pygame.mixer.init()

                dotSound = pygame.mixer.Sound('dotSound.wav')
                dashSound = pygame.mixer.Sound('dashSound.wav')

                for character in result:

                    if character is ".":
                        dotSound.play()
                        time.sleep(0.2)

                    if character is "-":
                        dashSound.play()
                        time.sleep(0.2)

                    if character is " ":
                        time.sleep(0.2)

        #print(result)
        return result

    if __name__ == '__main__':
        import sys
        get_input = input

        #If python2 is used, func still can work
        if sys.version_info[:2] <= (2, 7):
            get_input = raw_input


#pyMorse.morseTranslator(entry="sos", playSound=True)
