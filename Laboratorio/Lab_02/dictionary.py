import re

class Dictionary:
    def __init__(self):
        self._dict = {}

    def addWord(self, key_value):
        if len(key_value) >= 2:
            key = key_value[0]
            values = key_value[1:]
            if key not in self._dict:
                self._dict[key] = values
            else:
                existing_values = self._dict[key]
                self._dict[key] = existing_values + values

    def translate(self, key):
        translations = self._dict.get(key)
        if translations:
            translations = ', '.join(''.join(sublist) for sublist in translations)
            return translations
        else:
            return "Parola non trovata nel dizionario."

    def translateWordWildCard(self, wildCard):
        wildCard = wildCard.replace("?", ".")
        matches = []
        for w in self._dict.keys():
            if re.search(wildCard, w):
                matches.append((w, ', '.join(' '.join(sublist) for sublist in self._dict.get(w))))
        return matches if matches else None

    def loadDictionary(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                key_value = line.strip().split()
                if len(key_value) >= 2:
                    key = key_value[0]
                    values = key_value[1:]
                    self.addWord((key, values))

    def printAll(self):
        for key, values in self._dict.items():
            if len(values) > 1:
                translations = ', '.join(''.join(sublist) for sublist in values)
                print(f"Alien Word: {key}, Translations: {translations}\n")
            else:
                translations = ''.join(values[0])
                print(f"Alien Word: {key}, Translations: {translations}\n")
