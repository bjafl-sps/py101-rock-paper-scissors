import random
import time
import os

# Konstanter
GYLDIGE_TREKK = ["stein", "saks", "papir"]
TALL_TIL_TREKK = {
    "1": "stein",
    "2": "saks",
    "3": "papir"
}
TREKK_TIL_EMOJI = {
    "stein": "🪨",
    "saks": "✂️",
    "papir": "📜"
}
VINNER_KOMBINASJONER = {
    "stein": "saks",
    "saks": "papir",
    "papir": "stein"
}

KANTLINJER_ENKEL = {
    'hjorne_vt_tegn': '┌',
    'hjorne_ht_tegn':'┐',
    'hjorne_vb_tegn':'└',
    'hjorne_hb_tegn':'┘',
    'horisontal_tegn':'─',
    'vertikal_tegn':'│'
}
KANTLINJER_DOBBEL = {
    'hjorne_vt_tegn': '╔',
    'hjorne_ht_tegn':'╗',
    'hjorne_vb_tegn':'╚',
    'hjorne_hb_tegn':'╝',
    'horisontal_tegn':'═',
    'vertikal_tegn':'║'
}
KANTLINJER_DOBBEL_UTEN_HORISONTAL = KANTLINJER_DOBBEL | {'vertikal_tegn': ' '}

def faa_spiller_valg():
    """
    Ber om og validerer spillerens valg.
    Returnerer: str - validert valg i små bokstaver
    """

    while True:
        valg = input("\nVelg stein (1), saks (2), eller papir (3): ").lower().strip()
        
        if valg in GYLDIGE_TREKK:
            return valg
        elif valg in TALL_TIL_TREKK:
            return TALL_TIL_TREKK[valg]
        
        gyldig_input = ", ".join(
            ", ".join([tall, trekk]) for tall, trekk in TALL_TIL_TREKK.items()
        )
        print(f"Ugyldig valg! Velg mellom: {gyldig_input}")

def faa_datamaskin_valg():
    """
    Genererer datamaskinens valg.
    Returnerer: str - tilfeldig valg
    """
    return random.choice(GYLDIGE_TREKK)

def rens_skjerm():
    """Tømmer skjermen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def vis_nedtelling():
    """Viser en nedtelling før valget avsløres"""
    rens_skjerm()

    print("\nStein...", end=" ", flush=True)
    time.sleep(0.7)
    print("Saks...", end=" ", flush=True)
    time.sleep(0.7)
    print("Papir!\n", flush=True)
    time.sleep(0.3)

def finn_vinner(spiller_valg, datamaskin_valg):
    """
    Bestemmer vinneren av runden.
    Returnerer: str - "spiller", "datamaskin" eller "uavgjort"
    """
    if spiller_valg == datamaskin_valg:
        return "uavgjort"
    elif VINNER_KOMBINASJONER[spiller_valg] == datamaskin_valg:
        return "spiller"
    return "datamaskin"

def vis_tabell(data: dict[list], kol_bredde=20, skilletegn_rader=True):
    """
    Viser en tabell med to kolonner
    """
    kolonner = list(data.keys())
    print("|".join([kolonne.center(kol_bredde) for kolonne in kolonner]))
    print("+".join(["-"*kol_bredde for _ in kolonner]))

    maks_rader = max(len(data[kolonne]) for kolonne in kolonner)
    rader = [
        data[kolonne] + [""]*(maks_rader-len(data[kolonne])) 
        for kolonne in kolonner
    ]

    skilletegn = "|" if skilletegn_rader else ""
    for rad in range(maks_rader):
        print(skilletegn.join([
            rader[kolonne][rad].center(kol_bredde) 
            for kolonne in range(len(kolonner))
        ]))

def vis_tekstboks(tekst: str, horisontal_tegn, vertikal_tegn, 
                  hjorne_vt_tegn, hjorne_ht_tegn, hjorne_vb_tegn,
                  hjorne_hb_tegn, bredde=50, center=True):
    """Viser en tekstboks med valgt tekst"""
    tekst_lengde = len(tekst)
    if tekst_lengde > bredde-4:
        tekst = [tekst[i:i+bredde-4] 
                 for i in range(0, tekst_lengde, bredde-4)]
    if not isinstance(tekst, list):
        tekst = [tekst]
        
    print(hjorne_vt_tegn + horisontal_tegn*(bredde-2) + hjorne_ht_tegn)
    
    for linje in tekst:
        if center:
            print(vertikal_tegn + linje.center(bredde-2) + vertikal_tegn)
        else:
            print(vertikal_tegn + linje.ljust(bredde-2) + vertikal_tegn)
    
    print(hjorne_vb_tegn + horisontal_tegn*(bredde-2) + hjorne_hb_tegn)


def vis_resultat(spiller_valg, datamaskin_valg, vinner):
    """Viser resultatet av runden"""

    vis_tabell({
        "Spiller": [TREKK_TIL_EMOJI[spiller_valg]],
        "Datamaskin": [TREKK_TIL_EMOJI[datamaskin_valg]]
    }, skilletegn_rader=False)
    
    print()
    if vinner == "uavgjort":
        vinner_tekst = "Det ble uavgjort! ⚖️"
    elif vinner == "spiller":
        vinner_tekst = "Du vinner! 🎉"
    else:
        vinner_tekst = "Datamaskinen vinner! 💀"

    vis_tekstboks(vinner_tekst, **KANTLINJER_DOBBEL_UTEN_HORISONTAL)

def oppdater_poeng(poeng, vinner):
    """
    Oppdaterer poengsummen.
    Returnerer: dict - oppdatert poengtabell
    """
    if vinner == "spiller":
        poeng["spiller"] += 1
    elif vinner == "datamaskin":
        poeng["datamaskin"] += 1
    return poeng

def vis_poengsum(poeng):
    """Viser nåværende poengsum"""
    print()
    vis_tekstboks("Stilling:", bredde=15, **KANTLINJER_ENKEL)
    vis_tabell({
        "Spiller": [str(poeng["spiller"])],
        "Datamaskin": [str(poeng["datamaskin"])]
    })

def spill_runde(poeng):
    """
    Spiller én runde og oppdaterer poengsummen.
    Returnerer: bool - True hvis spilleren vil spille igjen
    """
    spiller_valg = faa_spiller_valg()
    datamaskin_valg = faa_datamaskin_valg()
    
    vis_nedtelling()
    
    vinner = finn_vinner(spiller_valg, datamaskin_valg)
    vis_resultat(spiller_valg, datamaskin_valg, vinner)
    
    oppdater_poeng(poeng, vinner)
    vis_poengsum(poeng)
    
    fortsett = input("\nVil du spille igjen? (ja/nei): ").lower().strip()
    return fortsett.lower().startswith("j")

def vis_velkomst():
    """Viser velkomstmelding"""
    rens_skjerm()

    vis_tekstboks("Velkommen til Stein, Saks, Papir!", **KANTLINJER_DOBBEL)
    print()
    tekst = [
        "Regler:",
        "---------",
        "- Stein knuser saks",
        "- Saks klipper papir",
        "- Papir pakker inn stein"
    ]
    vis_tekstboks(tekst, **KANTLINJER_ENKEL, center=False, bredde=30)

def vis_avslutning(poeng):
    """Viser avslutningsmelding med endelig resultat"""
    rens_skjerm()

    vis_tekstboks("Takk for at du spilte!", **KANTLINJER_DOBBEL)
    print()
    vis_tekstboks("Endelig resultat:", **KANTLINJER_ENKEL, 
                  bredde=22)
    print()
    vis_tabell({
        "Du": [str(poeng["spiller"])],
        "Datamaskin": [str(poeng["datamaskin"])]
    }, kol_bredde=20)

    if poeng['spiller'] > poeng['datamaskin']:
        vinner_tekst = "Gratulerer, du vant turneringen! 🏆"
    elif poeng['spiller'] < poeng['datamaskin']:
        vinner_tekst = "Datamaskinen vant turneringen! 💀"
    else:
        vinner_tekst = "Turneringen endte uavgjort! ⚖️"
    
    vis_tekstboks(vinner_tekst, **KANTLINJER_DOBBEL_UTEN_HORISONTAL)

def start_spill():
    """Hovedfunksjonen som kjører spillet"""
    vis_velkomst()
    
    poeng = {
        "spiller": 0,
        "datamaskin": 0
    }
    
    ny_runde = True
    while ny_runde:
        ny_runde = spill_runde(poeng)
    
    vis_avslutning(poeng)

#if __name__ == "__main__":
start_spill()