import csv
from csv import reader
def carica_da_file(file_path):
    biblioteca = {}
    try:
        with open(file_path,'r', encoding='utf-8') as csv_file:
            csv_reader = reader(csv_file)
            next(csv_reader)             #salto la prima riga del csv
    except FileNotFoundError:            #gestione del file non trovato
        print('None')

    for riga in csv_reader:
        titolo = riga[0]
        autore = riga[1]
        anno = riga[2]
        pagine = riga[3]
        sezione = riga[4]
        biblioteca[sezione] = [titolo, autore, anno, pagine]

    return biblioteca
    """Carica i libri dal file"""
    # TODO

def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):
    #verifico che la sezione sia già esistente, altrimenti restituisco None
    if sezione not in biblioteca[sezione]:
        return None

    nuovo_libro= [titolo, autore, anno, pagine]
    for libro in biblioteca[sezione]:
        if libro[0].lower() == nuovo_libro[0].lower():
            return None     #verifica del titolo

    biblioteca[sezione].append(nuovo_libro)
    try:
        with open(file_path, 'a', newline ='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([titolo, autore, anno, pagine, sezione])

    except FileNotFoundError:
        return None

    """Aggiunge un libro nella biblioteca"""
    # TODO


def cerca_libro(biblioteca, titolo):
    """Cerca un libro nella biblioteca dato il titolo"""
    # TODO
    for sezione in biblioteca:
        libri = biblioteca[sezione]
        for libro in libri:
            if libro[0].lower() == titolo.lower():
                return libro
    else:
        return None

def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    """Ordina i titoli di una data sezione della biblioteca in ordine alfabetico"""
    # TODO
    if sezione not in biblioteca:
        return None

    titoli = []
    for libri in biblioteca[sezione]:
        titoli.append(libri[0])
    titoli.sort()
    return titoli


def main():
    biblioteca = []
    file_path = "biblioteca.csv"

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca = carica_da_file(file_path)
                if biblioteca is not None:
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path)
            if libro:
                print(f"Libro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()

