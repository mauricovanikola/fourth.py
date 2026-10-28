def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se král nebo jezdec může přesunout na danou pozici.
    """
    aktualni_pozice = figurka["pozice"]
    typ = figurka["typ"]

    # 1. Kontrola hranic šachovnice
    radek, sloupec = cilova_pozice
    if not (1 <= radek <= 8 and 1 <= sloupec <= 8):
        return False

    # 2. Kontrola obsazenosti
    if cilova_pozice in obsazene_pozice:
        return False

    # 3. Pohyb podle typu figurky
    if typ == "král":
        rozdil_radku = abs(cilova_pozice[0] - aktualni_pozice[0])
        rozdil_sloupcu = abs(cilova_pozice[1] - aktualni_pozice[1])

        if rozdil_radku <= 1 and rozdil_sloupcu <= 1:
            return cilova_pozice != aktualni_pozice

    elif typ == "jezdec":
        rozdil_radku = abs(cilova_pozice[0] - aktualni_pozice[0])
        rozdil_sloupcu = abs(cilova_pozice[1] - aktualni_pozice[1])

        if (rozdil_radku == 2 and rozdil_sloupcu == 1) or \
           (rozdil_radku == 1 and rozdil_sloupcu == 2):
            return True

    return False



if __name__ == "__main__":
    kral = {"typ": "král", "pozice": (4, 4)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    obsazene_pozice = {(4, 4), (5, 5), (3, 5)}

    # Testy pro krále
    print(je_tah_mozny(kral, (5, 5), obsazene_pozice))  # False (obsazeno)
    print(je_tah_mozny(kral, (5, 4), obsazene_pozice))  # True (o 1 pole dolů)
    print(je_tah_mozny(kral, (6, 6), obsazene_pozice))  # False (příliš daleko - o 2 pole)
    print(je_tah_mozny(kral, (0, 4), obsazene_pozice))  # False (mimo šachovnici)

    # Testy pro jezdce
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # True (tvar L: 2 nahoru, 1 doprava)
    print(je_tah_mozny(jezdec, (5, 5), obsazene_pozice))  # False (obsazeno)
    print(je_tah_mozny(jezdec, (4, 6), obsazene_pozice))  # True (tvar L)
    print(je_tah_mozny(jezdec, (10, 3), obsazene_pozice)) # False (mimo šachovnici)
