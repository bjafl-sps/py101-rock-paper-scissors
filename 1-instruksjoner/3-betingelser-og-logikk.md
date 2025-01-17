# Del 3: Betingelseslogikk (If-setninger) i Python

## Introduksjon
Betingelseslogikk lar programmet ditt ta beslutninger og kjøre forskjellig kode basert på ulike betingelser.

## Grunnleggende If-setninger
```python
# Enkel if-setning
if spiller_valg == "stein":
    print("Du valgte stein!")

# If-else setning
if spiller_valg == "stein":
    print("Du valgte stein!")
else:
    print("Du valgte ikke stein!")

# If-elif-else (flere betingelser)
if spiller_valg == "stein":
    print("Du valgte stein!")
elif spiller_valg == "saks":
    print("Du valgte saks!")
elif spiller_valg == "papir":
    print("Du valgte papir!")
else:
    print("Ugyldig valg!")
```

## Sammenligningsoperatorer
```python
# Er lik: ==
if poeng == 10:
    print("Spillet er over!")

# Er ikke lik: !=
if valg != "avslutt":
    print("Fortsett å spille!")

# Større enn: >
if poeng > 5:
    print("Høy poengsum!")

# Mindre enn: 
if liv < 20:
    print("Lite liv igjen!")

# Større enn eller lik: >=
if poeng >= 100:
    print("Du vinner!")

# Mindre enn eller lik: <=
if liv <= 0:
    print("Spillet er over!")
```

## Logiske Operatorer
```python
# and - begge betingelser må være Sanne
if spiller_valg == "stein" and datamaskin_valg == "saks":
    print("Spilleren vinner!")

# or - minst én betingelse må være Sann
if valg == "avslutt" or valg == "stopp":
    print("Avslutter spillet...")

# not - snur en betingelse
if not spill_over:
    print("Fortsett å spille!")
```

## Sammensatte Betingelser
```python
# Kombinere flere betingelser
if (spiller_valg == "stein" and datamaskin_valg == "saks") or \
   (spiller_valg == "papir" and datamaskin_valg == "stein") or \
   (spiller_valg == "saks" and datamaskin_valg == "papir"):
    print("Du vinner!")

# Sjekke om verdi finnes i en liste
gyldige_valg = ["stein", "saks", "papir"]
if spiller_valg in gyldige_valg:
    print("Gyldig trekk!")

# Sjekke om verdi IKKE finnes i en liste
if spiller_valg not in gyldige_valg:
    print("Ugyldig trekk!")
```

## Øvingsoppgaver
1. Enkel Vinner-sjekk:
```python
# Skriv et program som:
# - Tar to inndata (spiller1 og spiller2)
# - Sjekker om spiller1 valgte stein og spiller2 valgte saks
# - Skriver ut om spiller1 vinner
```

2. Komplett Spillogikk:
```python
# Skriv et program som:
# - Tar to gyldige valg (stein, saks eller papir)
# - Bestemmer vinneren ved hjelp av if-elif-setninger
# - Skriver ut hvem som vant og hvorfor
```

3. Inndatavalidering:
```python
# Skriv et program som:
# - Tar imot et spillervalg
# - Sjekker om det er gyldig ved hjelp av in-operatoren
# - Hvis gyldig, sjekker om det kan slå stein
# - Skriver ut passende meldinger
```

## Nøstede Betingelser
```python
if spiller_aktiv:
    if poeng > høyeste_poeng:
        print("Ny rekord!")
        høyeste_poeng = poeng
    else:
        print("Fortsett å prøve!")
else:
    print("Spillet er ikke aktivt")
```

## Vanlige Mønstre i Stein-Saks-Papir
```python
def finn_vinner(spiller, datamaskin):
    if spiller == datamaskin:
        return "Uavgjort!"
    
    vinnende_trekk = {
        "stein": "saks",
        "papir": "stein",
        "saks": "papir"
    }
    
    if vinnende_trekk[spiller] == datamaskin:
        return "Du vinner!"
    else:
        return "Datamaskinen vinner!"
```

## Vanlige Feil og Tips
- Husk å bruke `==` for sammenligning (ikke `=` som er for tilordning)
- Vær nøye med innrykk - det er viktig i Python!
- Ikke glem kolon `:` etter if/elif/else-setninger
- Tenk gjennom alle mulige tilfeller når du bruker if-elif-else

Vil du at jeg skal forklare noen av disse konseptene mer detaljert, eller vil du se noen mer komplekse eksempler? Vi kan også øve ved å skrive spesifikk spillogikk for stein-saks-papir.