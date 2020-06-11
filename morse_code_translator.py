#This is the easy morse code, which ignores most of punctuation.
def ignore_punctuation():
    punctuation_list = [",", ":", " ", "'"]
    for letter in list_of_char:
        if letter in punctuation_list:
            list_of_char.remove(letter)


def trans_to_up():
    for letter in list_of_char:
        list_of_char_up.append(letter.upper())

def translate():
    for letter in list_of_char_up:
        translate = morse_code[letter]
        list_translated.append(translate)
        text = "".join(list_translated)
    print("|".join(list_translated))

list_translated = []
list_of_char_up = []
morse_code = {'0' : '-----', '1' : '.----', '2' : '..---', '3' : '...--',
'4' : '....-', '5' : '.....', '6' : '-....', '7' : '--...',
'8' : '---..', '9' : '----.', 'A' : '.-'   , 'B' : '-...' , 'C' : '-.-.' ,
'D' : '-..'  , 'E' : '.'    , 'F' : '..-.' , 'G' : '--.'  ,
'H' : '....'  , 'I' : '..'   , 'J' : '.---' , 'K' : '-.-'  ,
'L' : '.-..' , 'M' : '--'   , 'N' : '-.'   , 'O' : '---'  ,
'P' : '.--.' , 'Q' : '--.-' ,'R' : '.-.'  , 'S' : '...'  ,
'T' : '-'    , 'U' : '..-'  , 'V' : '...-' , 'W' : '.--'  ,
'X' : '-..-' , 'Y' : '-.--' , 'Z' : '--..', '.':'STOP', "?":"STOP", "!":"STOP", " ":"/"}

text = input("Write the text which will be translated to the Morse code: ")
list_of_char = []
for word in text:
    for letter in word:
        list_of_char.append(letter)
ignore_punctuation()
trans_to_up()
translate()
