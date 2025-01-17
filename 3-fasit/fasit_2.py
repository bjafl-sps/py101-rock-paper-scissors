# losning_2.py

# Oppgave 1: Grunnleggende inndataprogram
def navneprogram():
    navn = input("Hva heter du? ")
    navn_formatert = navn.strip().title()
    print(f"Hei, {navn_formatert}!")

# Oppgave 2: Valg-validator
def valg_validator():
    valg = input("Velg stein, saks eller papir: ").lower().strip()
    gyldige_valg = ["stein", "saks", "papir"]
    
    if valg in gyldige_valg:
        print(f"'{valg}' er et gyldig valg!")
    else:
        print(f"'{valg}' er ikke gyldig. Velg mellom: {', '.join(gyldige_valg)}")

# Oppgave 3: Gjenta-mønster
def gjenta_til_gyldig():
    gyldige_valg = ["stein", "saks", "papir"]
    forsøk = 0
    
    while True:
        forsøk += 1
        valg = input("Velg stein, saks eller papir: ").lower().strip()
        
        if valg in gyldige_valg:
            break
        print("Ugyldig valg, prøv igjen!")
    
    print(f"Det tok {forsøk} forsøk å få et gyldig valg.")
    return valg

# Test alle funksjoner
if __name__ == "__main__":
    print("Test av navneprogram:")
    navneprogram()
    
    print("\nTest av valg-validator:")
    valg_validator()
    
    print("\nTest av gjenta-mønster:")
    gjenta_til_gyldig()