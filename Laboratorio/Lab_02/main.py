import translator as tr

t = tr.Translator()
t.loadDictionary("dictionary.txt")

while(True):
    t.printMenu()

    txtIn = input()
    # Add input control here!
    if not txtIn.isdigit():
        print("Errore: valori inseriti non correttamente")
        continue

    if int(txtIn) == 1:
        print("Ok, quale parola devo aggiungere?\n")
        txtIn = input()
        try:
            t.handleAdd(txtIn)
            print("Aggiunta!")
        except ValueError as e:
            print(f"Errore: {e}")
        continue

    if int(txtIn) == 2:
        print("Ok, quale parola devo cercare?\n")
        txtIn = input()
        txtTransl = t.handleTranslate(txtIn)
        print(txtTransl)
        continue

    if int(txtIn) == 3:
        print("Ok, quale parola devo cercare?\n")
        txtIn = input()
        txtTransl = t.handleWildCard(txtIn)
        print(txtTransl)
        continue

    if int(txtIn) == 4:
        t.dict.printAll()

    if int(txtIn) == 5:
        break
