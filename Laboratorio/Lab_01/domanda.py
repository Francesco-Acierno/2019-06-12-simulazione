import random


class Domanda:
    def __init__(self, testo, livello, risposta_corretta, risposte_errate):
        self.testo = testo
        self.livello = livello
        self.risposta_corretta = risposta_corretta
        self.risposte_errate = risposte_errate


def leggi_domande():
    domande = []
    with open("domande.txt", "r") as file:
        righe = file.readlines()
        i = 0
        while i < len(righe):
            if righe[i].strip():  # Controlla se la riga non è vuota
                testo = righe[i].strip()
                livello = int(righe[i + 1].strip())
                risposta_corretta = righe[i + 2].strip()
                risposte_errate = [riga.strip() for riga in righe[i + 3:i + 6]]
                domanda = Domanda(testo, livello, risposta_corretta, risposte_errate)
                domande.append(domanda)
                i += 6  # Salta le righe delle risposte errate e la riga vuota
            else:
                i += 1  # Salta la riga vuota

    # Ordina le domande per livello di difficoltà
    domande.sort(key=lambda x: x.livello)

    return domande


def aggiorna_punteggi(nickname, punteggio):
    with open("punti.txt", "a") as file:
        file.write(f"{nickname} {punteggio}\n")


def main():
    domande = leggi_domande()
    livello_corrente = 0
    punteggio = 0

    while livello_corrente < len(domande):
        domande_livello_corrente = [domanda for domanda in domande if domanda.livello == livello_corrente]

        if not domande_livello_corrente:
            print("Non ci sono domande per il livello corrente. Fine del gioco.")
            break

        domanda_corrente = random.choice(domande_livello_corrente)
        risposte_possibili = [domanda_corrente.risposta_corretta] + domanda_corrente.risposte_errate
        random.shuffle(risposte_possibili)

        print(f"Livello {livello_corrente}) {domanda_corrente.testo}?")
        for i, risposta in enumerate(risposte_possibili):
            print(f"{i + 1}. {risposta}")

        risposta_utente = int(input("Inserisci la risposta: ")) - 1
        if risposte_possibili[risposta_utente] == domanda_corrente.risposta_corretta:
            print("Risposta corretta!\n")
            punteggio += 1
            livello_corrente += 1
        else:
            print(f"Risposta sbagliata! La risposta corretta era: {domanda_corrente.risposta_corretta}\n")
            break

    print(f"Hai totalizzato {punteggio} punti!")
    nickname = input("Inserisci il tuo nickname: ")
    aggiorna_punteggi(nickname, punteggio)


if __name__ == "__main__":
    main()
