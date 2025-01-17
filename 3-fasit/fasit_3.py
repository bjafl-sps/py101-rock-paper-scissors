# losning_3.py

# Oppgave 1: Enkel vinner-sjekk
def enkel_vinner_sjekk():
    spiller1 = input("Spiller 1, velg stein, saks eller papir: ").lower().strip()
    spiller2 = input("Spiller 2, velg stein, saks eller papir: ").lower().strip()
    
    if spiller1 == "stein" and spiller2 == "saks":
        print("Spiller 1 vinner!")
    else:
        print("Spiller 1 vinner ikke med dette trekket.")

# Oppgave 2: Komplett spillogikk
def komplett_spill_logikk():
    gyldige_valg = ["stein", "saks", "papir"]
    
    spiller1 = input("Spiller 1: ").lower().strip()
    spiller2 = input("Spiller 2: ").lower().strip()
    
    if spiller1 not in gyldige_valg or spiller2 not in gyldige_valg:
        print("Ugyldig valg!")
        return
    
    if spiller1 == spiller2:
        print("Uavgjort!")
    elif (spiller1 == "stein" and spiller2 == "saks") or \
         (spiller1 == "saks" and spiller2 == "papir") or \
         (spiller1 == "papir" and spiller2 == "stein"):
        print(f"Spiller 1 vinner! {spiller1} slår {spiller2}")
    else:
        print(f"Spiller 2 vinner! {spiller2} slår {spiller1}")

# Oppgave 3: Inndatavalidering
def valider_og_sjekk_mot_stein():
    gyldige_valg = ["stein", "saks", "papir"]
    valg = input("Velg stein, saks eller papir: ").lower().strip()
    
    if valg not in gyldige_valg:
        print("Ugyldig valg!")
        return
    
    print(f"Du valgte {valg}")
    
    if valg == "stein":
        print("Uavgjort mot stein!")
    elif valg == "papir":
        print("Du vinner mot stein!")
    else:  # saks
        print("Du taper mot stein!")

# Test alle funksjoner
if __name__ == "__main__":
    print("Test av enkel vinner-sjekk:")
    enkel_vinner_sjekk()
    
    print("\nTest av komplett spillogikk:")
    komplett_spill_logikk()
    
    print("\nTest av validering og stein-sjekk:")
    valider_og_sjekk_mot_stein()