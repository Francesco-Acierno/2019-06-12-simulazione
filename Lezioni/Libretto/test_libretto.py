from voto import Libretto, Voto

lib = Libretto()

v1 = Voto("Analisi I", 10, 28, False, '2022-01-30')
lib.append(v1)

lib.append(Voto("Fisica I", 10, 25, False, '2022-07-12'))
lib.append(Voto("Analisi II", 8, 30, True, '2023-02-15'))

voti25 = lib.findByPunteggio(25, False)
for v in voti25:
    print(v.esame)

voto_analisi2 = lib.findByEsame("Analisi III")
if voto_analisi2 is None:
    print("Nessun voto trovato")
else:
    print(f"Hai preso {voto_analisi2.str_punteggio()}")

try:
    voto_analisi2 = lib.findByEsame2("Analisi III")
    print(f"Hai preso {voto_analisi2.str_punteggio()}")
except ValueError:
    print("Nessun voto trovato")

nuovo1 = Voto("Fisica I", 10, 25, False, '2022-07-13')
nuovo2 = Voto("Fisica II", 10, 25, False, '2022-07-13')
print("1)", lib.has_voto(nuovo1))
print("2)", lib.has_voto(nuovo2))

lib.append(Voto("Analisi 1", 10, 18, False, '2020-01-01'))
lib.append(Voto("Chimica", 8, 30, False, '2020-01-02'))
lib.append(Voto("Informatica", 8, 30, True, '2020-01-03'))
lib.append(Voto("Algebra Lineare", 10, 24, False, '2020-06-01'))
lib.append(Voto("Fisica 1", 10, 21, False, '2020-06-02'))

migliorato = lib.crea_migliorato()
lib.append(Voto("Tesi", 3, 0, False, '2020-06-01'))

print("Libretto originario")
lib.stampa()
print("\nLibretto migliorato")
migliorato.stampa()

ordinato = lib.crea_ordinato_per_esame()
print("\nLibretto ordinato")
ordinato.stampa()

ordinato.cancella_inferiori(24)
print("\nLibretto senza voti brutti")
ordinato.stampa()
