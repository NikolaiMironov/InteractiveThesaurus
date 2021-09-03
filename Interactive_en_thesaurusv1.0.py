import json
from difflib import get_close_matches
data = json.load(open("Resources/data.json"))

def definitions(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data: #checks if user has entered a name of city
        return data[word.title()]
    elif word.upper() in data: #in case user enters words like USA or NATO
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        confirm = input("Did you mean '%s' instead? Enter Y if yes or N if no: " % get_close_matches(word, data.keys())[0])
        if confirm == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif confirm == "N":
            return "PLease, check the word you are searching for."
        else:
            return "Incorrect input!"
    else:
        return "The word doesn't exists"


word = input("Enter a word: ")
output = definitions(word)

#print(" ".join(definitions(word)))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
