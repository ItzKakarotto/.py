#DAY 5 - ASCII GENERATOR
#CODE WRITTEN BY - GitHub.com/ItzKakarotto

"""generate cool ASCII texts"""

x = "enter 'random' or just press enter to generate random text\nenter 'all' to generate all texts available\nenter <font name> to generate the text with that font\nenter 'listfonts' to get list of all fonts available\nenter 'new' to change the text\nenter 'clear' to clear\n"

#install pyfiglet - "pip install pyfiglet"
import pyfiglet
import random
from os import system, name 

#get all the fonts
FONTS = list()
for fnt in pyfiglet.FigletFont.getFonts():
    FONTS.append(fnt)

def clear():
    """clear the console/terminal"""
    if name == 'nt': 
         _ = system('cls') 
    else: 
         _ = system('clear') 
    print(x)

def listfonts():
    """prints all the fonts available"""
    for font in FONTS:
        if font.endswith("_") or font.startswith("cl"):
            continue
        else:
            print(font, end=", ")
            

def generate(text, font):
    """takes font and text as input and provides ASCII text"""
    try:
        f = pyfiglet.Figlet(font=font)
        result = f.renderText(text)
        print("\n"+result)
    except:
        print("Invalid Font! Type 'listfonts' to get the list of fonts available\n")

def generateall(text):
    """takes text as input and generate all ASCII texts available"""
    for fnt in FONTS:
        f = pyfiglet.Figlet(font=fnt)
        results = f.renderText(text)
        print("Font: ", fnt+"\n"+results)
        
def generaterandom(text):
    """takes text as input and generates a random ASCII text"""
    fnt = random.choice(FONTS)
    f = pyfiglet.Figlet(font=fnt)
    result = f.renderText(text)
    if text=="ASCII":
        print(result)
    else:
        print(f"\nFont: {fnt}\n"+result)
  
def main():
    """the switch"""
    text = input("\nEnter the Text: ")
    def gen():
        inp = (input(f"\nText='{text}': ")).lower()
        if inp.startswith("clear"):
            clear()
        elif inp.startswith("rand") or inp=='':
            generaterandom(text)
        elif inp=="all":
            generateall(text)
        elif inp.startswith("list"):
            listfonts()
        elif inp=="new":
            return main()
        elif inp in FONTS:
            generate(text, font=inp)
        else:
            print("Invalid input!")
        return gen()
    clear()
    gen()

generaterandom("ASCII")
main()
