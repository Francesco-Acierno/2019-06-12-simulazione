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
        traduzioni = []
        if len(entry.split(" ")) < 2:
            print("Errore nel formato dell'input.")
            return
        parole = entry.split(" ")
        for p in parole:
            if not p.isalpha():
                print("Errore: caratteri non ammessi.")
                return
        parola_aliena = parole.pop(0)

        if parola_aliena not in self.dizionario.keys():
            self.dizionario[parola_aliena] = []
            self.dizionario[parola_aliena].append(parole)
            file_name = open("dictionary.txt", 'a')
            file_name.write(f"{parola_aliena} {parole}\n")
            print(f"Aggiunta: {entry}")
        else:
            traduzioni.extend(parole)
            self.dizionario[parola_aliena] = traduzioni
            with open("dictionary.txt", 'r+') as file:
                # Leggi tutte le righe del file
                righe = file.readlines()

                # Itera attraverso le righe
                for i, riga in enumerate(righe):
                    # Dividi la riga in due colonne separate da uno spazio
                    colonne = riga.split()

                    # Se la prima colonna contiene la parola da cercare
                    if colonne[0] == parola_aliena:
                        # Verifica il tipo di dato nella seconda colonna
                        if len(colonne) > 1 and colonne[1][0] == '[' and colonne[1][-1] == ']':
                            # Se la seconda colonna è una lista, convertila in una lista Python
                            colonne[1] = eval(colonne[1])
                            # Aggiungi le parole dalla lista alla seconda colonna
                            colonne[1] += traduzioni
                            # Ricostruisci la riga aggiornata
                            riga_aggiornata = colonne[0] + ' ' + str(colonne[1]) + '\n'
                        else:
                            # Se la seconda colonna è una stringa, aggiungi le parole direttamente a essa
                            colonne[1:] += traduzioni
                            # Ricostruisci la riga aggiornata
                            riga_aggiornata = ' '.join(colonne) + '\n'
                        # Sovrascrivi solo la parte interessata nel file
                        file.seek(0)
                        righe[i] = riga_aggiornata
                        file.writelines(righe)
                        break
            print(f"Aggiunta: {entry}")


    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        return self.dizionario.get(query)

    def handleWildCard(self, query):
    # query is a string with a ? --> <par?la_aliena>
        parole_soddisfacenti = []

        # Itera attraverso le chiavi del dizionario

        for parola_aliena, traduzione in self.dizionario.items():
            # Assicurati che la lunghezza delle due parole sia la stessa
            if len(query) != len(parola_aliena):
                continue

            # Confronta carattere per carattere
            for i in range(len(query)):
                if query[i] != "?" and query[i] != parola_aliena[i]:
                    break
            else:
                # Se il ciclo non viene interrotto, la parola soddisfa il criterio di ricerca
                parole_soddisfacenti.append((parola_aliena, traduzione))

        return parole_soddisfacenti

