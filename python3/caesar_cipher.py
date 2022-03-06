#CAESAR CIPHER - DAY 4
#CODE - GitHub.com/ItzKakarotto

print("""
   ___                               ___ _       _               
  / __\__ _  ___  ___  __ _ _ __    / __(_)_ __ | |__   ___ _ __ 
 / /  / _` |/ _ \/ __|/ _` | '__|  / /  | | '_ \| '_ \ / _ \ '__|
/ /__| (_| |  __/\__ \ (_| | |    / /___| | |_) | | | |  __/ |   
\____/\__,_|\___||___/\__,_|_|    \____/|_| .__/|_| |_|\___|_|   
                                          |_|                    
|______________________________________________________________|\n""")

TIPS = (
    "A Caesar cipher is a simple method of encoding messages.",
    "Caesar ciphers use a substitution method where letters in the alphabet are shifted by some fixed number of spaces to yield an encoded message",
    "Scope=Shift, Note: scope only accepts Integer",
#    "Type 'hack' to get the Decoded message without Entering Scope huehue"
)
for tips in TIPS:
    print("× " +tips, end="\n\n")
    
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encode(msg, scope):
    alphabets_1 = alphabets.copy()
    encoded_msg=""
    for i in range(scope):
        x = alphabets_1.pop(0)
        alphabets_1.append(x)
    for letter in msg:
        if letter.isupper():
            index = alphabets.index(letter.lower())
            encoded_msg+= alphabets_1[index].upper()
        elif letter not in alphabets_1:
            encoded_msg+=letter
        else:
            index = alphabets.index(letter)
            encoded_msg += alphabets_1[index]
    
    return encoded_msg

def decode(msg, scope):
    alphabets_1 = alphabets.copy()
    decoded_msg = ""
    for i in range(scope):
        x = alphabets_1.pop(0)
        alphabets_1.append(x)
    for letter in msg:
        if letter.isupper():
            index = alphabets_1.index(letter.lower())
            decoded_msg+=alphabets[index].upper()
        elif letter not in alphabets_1:
            decoded_msg+=letter
        else:
            index = alphabets_1.index(letter)
            decoded_msg += alphabets[index]
        
    return decoded_msg
    
def main():
    """the switch which mostly takes input and provides output"""
    inp = input("\nType 'encode' to encode and 'decode' to decode\n  > ").lower()
    if inp.startswith("en"):
        msg = input("\nType the message you wanna encode\n  > ")
        scope = int(input("\nType the scope\n  > "))
        print("\nEncoded Message:", encode(msg, scope))
        return main()
    elif inp.startswith("de"):
        msg = input("\nType the message you wanna decode\n  > ")
        scope = int(input("\nType the scope\n  > "))
        print("\nDecoded Message:", decode(msg, scope))
        return main()
    elif inp.startswith("hack"):
        decode26()
    else:
        print("Error: Invalid Input!")
        return main()

def decode26():
    """Decode any Caesar Cipher encoded message ; )"""
    msg = input("\nEnter a Text\n  > ")
    for i in range(1, 26):
        print(decode(msg, i))
    return main()
        
    
main()
