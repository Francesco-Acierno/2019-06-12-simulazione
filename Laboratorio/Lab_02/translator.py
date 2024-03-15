from dictionary import Dictionary
import re

class Translator:

    def __init__(self, dict_instance=None):
        if dict_instance is None:
            self._dict = Dictionary()
        else:
            self._dict = dict_instance

    def printMenu(self):
        print("______________________________\n" +
              "   Translator Alien-Italian\n" +
              "______________________________\n" +
              "1. Aggiungi nuova parola\n" +
              "2. Cerca una traduzione\n" +
              "3. Cerca con wildcard\n" +
              "4. Stampa tutto il Dizionario\n" +
              "5. Exit\n" +
              "______________________________\n")

    def loadDictionary(self, txtDict):
        # dict is a string with the filename of the dictionary
        self._dict.loadDictionary(txtDict)

    def handleAdd(self, txtEntry):
        # entry is a string '<parola_aliena> <traduzione1 traduzione2 ...>'
        # Add input control here!
        key, *values = txtEntry.split()  # Separare la parola e le traduzioni
        # Verificare che sia la parola che le traduzioni siano composte solo da lettere dell'alfabeto
        if all(re.match("^[a-zA-Z]+$", word) for word in [key] + values):
            self._dict.addWord((key, ', '.join(values)))  # Aggiungere le traduzioni valide al dizionario
        else:
            raise ValueError("Sia le parole che le traduzioni devono contenere solo lettere dell'alfabeto.")

    def handleTranslate(self, query):
        # query is a string '<parola_aliena>'
        translations = self._dict.translate(query)
        if translations:
            return(translations)
        else:
            return("Nessuna corrispondenza trovata per la query.")

    def handleWildCard(self, query):
        # query is a string with a ? --> <par?la_aliena>
        matches = self._dict.translateWordWildCard(query)
        result = ""
        if matches:
            for match in matches:
                translations = ', '.join([''.join(sublist.split()) for sublist in match[1].split(',')])
                result += f"Alien Word: {match[0]}, Translations: {translations}\n"
        else:
            result = "Nessuna corrispondenza trovata per la query."
        return result

    # Aggiungere un metodo per la stampa diretta dei risultati
    def printResult(self, results):
        if results:
            for alien_word, translations in results:
                return f"Alien Word: {alien_word}, Translations: {translations}"
        else:
            return "Nessuna corrispondenza trovata per la query."

    @property
    def dict(self):
        return self._dict
