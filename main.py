import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dic = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dic)


# output_list = ""

def write():
    word = input("Write what you want: ").upper()
    try:
        output_list = [phonetic_dic[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        write()
    else:
        print(output_list)


write()
