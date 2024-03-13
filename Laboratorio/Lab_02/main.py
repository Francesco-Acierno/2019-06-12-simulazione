import translator as tr

t = tr.Translator("dictionary.txt")


while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        print(f"Ok, quale parola devo aggiungere?")
        txtIn = input()
        print(t.handleAdd(txtIn))
    elif int(txtIn) == 2:
        print(f"Ok, quale parola devo tradurre?")
        txtIn = input()
        print(t.handleTranslate(txtIn))
    elif int(txtIn) == 3:
        print(f"Ok, quale parola devo cercare?")
        pass
    elif int(txtIn) == 4:
        break
