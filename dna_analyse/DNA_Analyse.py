gueltige_nukleotide = ['A', 'T', 'G', 'C']

# Molekulargewichte in mg/mol
# Nukleotidmonophosphate ohne 3'-OH-Gruppe
mw_a = 313210
mw_t = 304200
mw_g = 329210
mw_c = 289180
# freie OH-Gruppe am 3'-Ende eines DNA-Fragments
mw_oh = 17010


def hole_dna_sequenz():
    """Liefere eine vom Nutzer erfragte und validierte DNA-Sequenz.

    Um gültig zu sein, darf die Sequenz nur aus den Buchstaben
    A, G, T, C, a, g, t, c bestehen.
    """

    # Hinweis: Verwende eine while-Schleife, innerhalb derer Du eine
    # Sequenz vom Nutzer erfragst und die Eingabe validierst.
    # Nur wenn die Validierung klappt, brichst Du die Schleife ab
    # und lieferst die Sequenz zurück.
    while True:
        sequence = input('Gib eine DNA-Sequenz ein: ')
        
        # Hier fehlt natürlich noch die Validierung.
        # Dafür brauchst Du noch eine Schleife, in der jeder Buchstabe
        # der Eingabe auf Gültigkeit geprüft werden muss.
        # Für einen Anfänger ist das schon eine ordentlich harte Nuss,
        # die aber mit etwas Anstrengung zu knacken sein sollte.

        if erfolgreiche_validierung:
            break
        else:
            # Dieser Teil wird ausgeführt wenn die Bedingung hinter if
            # nicht erfüllt war.
            print()
            print(
                'Bei der Eingabe handelt es sich nicht um eine gültige '
                'DNA-Sequenz!'
                )
            print()
            print()
        
    return sequence


seq = hole_dna_sequenz()
# Hier sollten jetzt die nötigen Berechnungen durchgeführt werden.

# Und hier erfolgt dann die Ausgabe.
print()
print('Eingelesene Sequenz:')
