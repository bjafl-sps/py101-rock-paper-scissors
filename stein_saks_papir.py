import random

GYLDIGE_VALG = ["stein", "saks", "papir"]
PC = "datamaskin"
SPILLER = "spiller"
UAVGJORT = "ingen"

def faa_bruker_valg():
    """
    Ber om og validerer spillerens valg.
    Returnerer: str - validert valg i små bokstaver
    """

    print("\nHva vil du spille?")
    print("1: Stein")
    print("2: Saks")
    print("3: Papir")

    while True:
        valg = input("Skriv 1, 2, eller 3, etterfulgt av enter: ")
        valg_strippet = valg.strip()
        if valg_strippet == "1":
            return "stein"  # return returnerer en verdi og avslutter funksjonen
                            # slik bryter vi også ut av den uendelige while-løkken
        elif valg_strippet == "2":
            return "saks"
        elif valg_strippet == "3":
            return "papir"
        else:
            print("Ugyldig valg! Prøv igjen...")


def faa_datamaskin_valg():
    """
    Returnerer et tilfeldig valg for datamaskinen.
    Returnerer: str - tilfeldig valg i små bokstaver
    """
    return random.choice(GYLDIGE_VALG) # random.choice velger et tilfeldig element fra en liste

def avgjor_vinner(bruker_valg, datamaskin_valg):
    """
    Avgjør vinneren av en runde.
    Returnerer: str - vinneren av runden
    """

    if bruker_valg == datamaskin_valg:
        return UAVGJORT

    # Her sjekker vi alle mulige vinnerkombinasjoner
    # Spiller vinner hvis en av disse kombinasjonene er oppfylt:
    # - Spiller velger stein og datamaskin velger saks
    # - Spiller velger saks og datamaskin velger papir
    # - Spiller velger papir og datamaskin velger stein
    # Dette sjekkes ved å bruke en eller-operator (or) for å sjekke 
    # om en av disse kombinasjonene er oppfylt
    if (bruker_valg == "stein" and datamaskin_valg == "saks") or \
        (bruker_valg == "saks" and datamaskin_valg == "papir") or \
        (bruker_valg == "papir" and datamaskin_valg == "stein"):
        return SPILLER
    else:
        return PC
    
def vis_resultat(bruker_valg, datamaskin_valg, vinner):
    """
    Viser resultatet av en runde.
    """
    print(f"\nDu valgte {bruker_valg}. Datamaskinen valgte {datamaskin_valg}.")

    if vinner == UAVGJORT:
        print("Det ble uavgjort!")
    elif vinner == SPILLER:
        print("Du vant!")
    else:
        print("Datamaskinen vant!")

def start_spill():
    """
    Starter et spill av stein, saks, papir.
    """
    # Variabler for å holde styr på poeng
    poeng_spiller = 0
    poeng_pc = 0
    print("Velkommen til Stein, Saks, Papir!")

    ny_runde = True
    while ny_runde:
        bruker_valg = faa_bruker_valg()
        datamaskin_valg = faa_datamaskin_valg()
        vinner = avgjor_vinner(bruker_valg, datamaskin_valg)
        vis_resultat(bruker_valg, datamaskin_valg, vinner)

        spill_igjen = input("\nVil du spille igjen? (ja/nei): ").lower().strip()
        if spill_igjen != "ja":
            break

    print("Takk for at du spilte!")