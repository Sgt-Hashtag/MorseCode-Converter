MorseCharDict ={"A":".-",
                "B":"-...",
                "C":"-.-.",
                "D":"-..",
                "E":".",
                "F":"..-.",
                "G":"--.",
                "H":"....",
                "I":"..",
                "J":".---",
                "K":"-.-",
                "L":".-..",
                "M":"--",
                "N":"-.",
                "O":"---",
                "P":".--.",
                "Q":"--.-",
                "R":".-.",
                "S":"...",
                "T":"-",
                "U":"..-",
                "V":"...-",
                "W":".--",
                "X":"-..-",
                "Y":"-.--",
                "Z":"--.."}
MorseOtherDict =",1234567890.,?!'()&;:/=+-$@"

def TextToMorse(code):
    s=""
    s1 = list(code)
    for i in range(len(s1)):
        if(s1[i] != " "):
            s += MorseCharDict[s1[i].upper()]
        else:
            s += "/"
    return s

x = input("what is your message: ")
print(TextToMorse(x))      
        