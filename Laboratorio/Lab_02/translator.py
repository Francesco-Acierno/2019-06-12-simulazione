class Translator:

    def __init__(self, file_name):
        self.file_name = file_name
        self.dizionario = {}

    def printMenu(self):
        print(f"1. Aggiungi nuova parola \n2. Cerca una traduzione \n3. Cerca con wildcard \n4. Exit")

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        with open(self.file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                pAlieno = line.split(" ")[0]
                pItaliano = line.split(" ")[1]
                self.dizionario[pAlieno] = pItaliano

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        parola_aliena = entry.split(" ")[0]
        traduzione = entry.split(" ")
        new_traduzione = traduzione[1:]
        self.dizionario[parola_aliena] = new_traduzione
        file_name = open("dictionary.txt", 'a')
        file_name.write(f"{parola_aliena} {new_traduzione}\n")

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        return self.dizionario.get(query)

    def handleWildCard(self, query):
        # query is a string with a ? --> <par?la_aliena>
        pass
