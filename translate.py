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

def writeMorse(lst):
    with open("MorseTranslated.txt", "w") as F:
        temp = ""
        for i in lst:
            temp += (i+" ")
        F.write(temp)
        F.close()
        print("string was translated and written to the 'MorseTranslated.txt'. ")
    return 0

def writeNormal(lst):
    with open("NormalTranslated.txt", "w") as F:
        temp=""
        for i in lst:
            temp+=i
        F.write(temp)
        F.close()
        print("string was translated and written to the 'NormalTranslated.txt'. ")
    return 0

def readMorse():
    output=[]
    with open("MorseTranslated.txt", "r") as F:
        temp=F.read().split("/")
        for i in temp:
            output.extend(i.split())
        print(F.read())
        F.close()
    return output

def readNormal():
    with open("NormalTranslated.txt", "r") as F:
        output=F.read().split()
        print(F.read())
        F.close()
    return output


def translateToMorse(*entry):
    if (entry==None):                   #if input parameter is Null take new input
        entry = str(input('Entry: '))
    else:                               #else use input parameter
        entry = entry[0]

    result = []

    for character in entry:
        if character == "":
            raise IOError("entry is empty")
        else:
            result.append(matching[character.upper()])
            #not working
    print(result)
    return result

def translateFromMorse(*entry):
    if (entry==None):                   #if input parameter is Null take new input
        entry = str(input('Entry: '))
    else:                               #else use input parameter
        entry = entry[0]

    result = ""

    for character in entry:
        if character == '':
            raise IOError("entry is empty")
        else:
            result += matching.values([character])

    print(result)
    return result


if __name__ == '__main__':
    translateToMorse("asd")
    #translateFromMorse()