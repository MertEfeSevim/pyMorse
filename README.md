# pyMorse
PyMorse is a Python library project that translates the Morse code into a Latin alphabet or vice versa. Currently thinking to add new features. Any idea would be appreciated.

# Dependency
PyGame is needed to play translations if asked for.

# Installation
    git clone https://github.com/MertEfeSevim/pyMorse.git

# Here is what function provides;

Translates entries to Morse Code or vice versa;

    morseTranslator(entry="sos")                        
    #returns "... --- ..."
    
    morseTranslator(entry="... --- ...",fromMorse:True) 
    #return "sos"

Reads from file;
    
    morseTranslator(fromFile="sample.txt") 
    #sample.txt contains "sos", func returns "... --- ..."
    
    morseTranslator(fromFile="sample.txt") 
    #sample.txt contains "... --- ...", func returns "sos"
    
Writes to specified file;
    
    morseTranslator(entry="sos",writeToFile="greatDocumentation.txt")
    #writes "... --- ..." to greatDocumentation.txt
    
    morseTranslator(entry="... --- ...",writeToFile="greatDocumentation.txt")
    #writes "sos" to greatDocumentation.txt

Plays Morse Code's sound;
    
    morseTranslator(entry="sos",playSound=True)
    #Returns translation and plays the translated code
    
    morseTranslator(entry="... --- ...",playSound=True,fromMorse=True)
    #Returns error, can not play latin alphabet

