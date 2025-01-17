# Del 2: Brukerinndata og Streng-metoder

## Introduksjon
En viktig del av interaktive programmer er å hente og behandle brukerinndata. I stein-saks-papir-spillet må vi få spillerens valg og sørge for at det er i riktig format.

## Hente Brukerinndata
```python
# Enkel inndata
spiller_valg = input("Skriv inn ditt valg: ")
print("Du skrev:", spiller_valg)

# Inndata med meldingstekst
navn = input("Hva heter du? ")
print("Hei,", navn)

# Husk: input() gir oss alltid en tekststreng!
alder_tekst = input("Skriv inn alderen din: ")  # Hvis du skriver 25, får du "25" (tekst)
alder_tall = int(alder_tekst)                   # Konverterer "25" til 25 (tall)
```

## Streng-metoder
Strenger kommer med innebygde metoder for å endre eller sjekke tekst:
```python
valg = "STEIN"

# Endre store/små bokstaver
små_bokstaver = valg.lower()    # "stein"
store_bokstaver = valg.upper()  # "STEIN"
første_stor = valg.title()      # "Stein"

# Fjerne ekstra mellomrom
rotete_inndata = "   stein   "
ren_inndata = rotete_inndata.strip()   # "stein"

# Sjekke strenginnhold
er_store = valg.isupper()       # True
er_små = valg.islower()         # False
er_tall = valg.isdigit()        # False
```

## Streng-sammenligninger
```python
# Enkel sammenligning (skiller mellom store/små bokstaver)
valg = "stein"
if valg == "stein":
    print("Gyldig valg!")

# Sammenligning uavhengig av store/små bokstaver
valg = "StEiN"
if valg.lower() == "stein":
    print("Gyldig valg!")

# Sjekke flere muligheter
gyldige_valg = ["stein", "saks", "papir"]
if valg.lower() in gyldige_valg:
    print("Gyldig valg!")
```

## Mønster for Inndatavalidering
Vanlig mønster for å få gyldig inndata:
```python
gyldige_valg = ["stein", "saks", "papir"]

# Fortsett å spørre til vi får gyldig inndata
while True:
    valg = input("Velg stein, saks eller papir: ").lower()
    if valg in gyldige_valg:
        break  # Gyldig inndata, avslutt løkken
    print("Ugyldig valg! Prøv igjen.")

print("Du valgte:", valg)
```

## Øvingsoppgaver
1. Grunnleggende Inndataprogram:
```python
# Skriv et program som:
# - Spør om spillerens navn
# - Konverterer det til stor forbokstav
# - Skriver ut "Hei, Navn!"
```

2. Valg-validator:
```python
# Skriv et program som:
# - Spør om stein, saks eller papir
# - Konverterer inndata til små bokstaver
# - Skriver ut om valget var gyldig
```

3. Gjenta-mønster:
```python
# Skriv et program som:
# - Fortsetter å spørre om valg til det er gyldig
# - Teller antall forsøk som trengs
# - Skriver ut "Det tok X forsøk å få et gyldig valg"
```

## Vanlige Problemer og Løsninger
```python
# Problem: Ekstra mellomrom
valg = "  stein  "
# Løsning: Bruk strip()
valg = valg.strip()

# Problem: Ulike bokstavstørrelser
valg = "STEIN"
# Løsning: Konverter til små bokstaver
valg = valg.lower()

# Problem: Ugyldig inndata
# Løsning: Bruk valideringsløkke
while True:
    valg = input("Valg: ").lower().strip()
    if valg in ["stein", "saks", "papir"]:
        break
    print("Ugyldig valg!")
```

## Eksempel: Komplett Inndatahåndterer
```python
def få_spiller_valg():
    gyldige_valg = ["stein", "saks", "papir"]
    
    while True:
        # Hent inndata og rens den
        valg = input("Skriv inn ditt valg: ").lower().strip()
        
        # Sjekk om gyldig
        if valg in gyldige_valg:
            return valg
        
        # Hvis vi kommer hit, var inndata ugyldig
        print(f"Vennligst velg mellom: {', '.join(gyldige_valg)}")
```