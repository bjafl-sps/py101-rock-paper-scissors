# Del 1: Grunnleggende Python Syntaks og Datatyper

## Introduksjon
Python er et lesbart programmeringsspråk hvor mellomrom og innrykk er viktig. Hver kodelinje er en instruksjon, og vi bruker innrykk for å gruppere relaterte instruksjoner.

## Kommentarer
Kommentarer hjelper med å forklare koden og blir ignorert av Python:
```python
# Dette er en enkellinjekommentar
"""
Dette er en
flerlinjet kommentar
"""
```

## Variabler og Grunnleggende Datatyper
Variabler lagrer data for senere bruk:
```python
# String (tekst)
spiller_navn = "Ole"
spillvalg = "stein"

# Integer (heltall)
poeng = 0
spill_spilt = 5

# Boolean (Sant/Usant)
spiller_nå = True
har_vunnet = False

# Skrive ut variabler
print(spiller_navn)     # Utskrift: Ole
print(poeng)           # Utskrift: 0
print(spiller_nå)      # Utskrift: True
```

## Grunnleggende Operasjoner
```python
# String-operasjoner
hilsen = "Hei " + spiller_navn  # Sette sammen tekst
rope = spillvalg.upper()        # Konverter til store bokstaver
hviske = spillvalg.lower()      # Konverter til små bokstaver

# Talloperasjoner
poeng = poeng + 1      # Legg til ett poeng
spill_spilt += 1      # Samme som: spill_spilt = spill_spilt + 1
```

## Lister
Lister lagrer flere elementer:
```python
# Lage en liste
valg = ["stein", "saks", "papir"]

# Få tak i listeelementer (posisjoner starter på 0)
første_valg = valg[0]     # "stein"
andre_valg = valg[1]      # "saks"

# Listeoperasjoner
valg.append("øgle")       # Legg til element på slutten
valg.remove("øgle")       # Fjern element
liste_lengde = len(valg)  # Få lengden på listen
```


## Vanlige Feil og Tips
- Python skiller mellom store og små bokstaver: `Navn` og `navn` er forskjellige variabler
- Tekst trenger matchende anførselstegn: `"hei"` eller `'hei'`
- Lister bruker hakeparenteser: `[element1, element2]`
- Husk å bruke stor forbokstav for `True`/`False`
- Bruk norske variabelnavn hvis du vil, men unngå æ, ø, å

## Praktisk Eksempel
```python
# Enkelt program som demonstrerer grunnleggende konsepter
spiller_navn = input("Hva heter du? ")
alder = int(input("Hvor gammel er du? "))
valg = ["stein", "saks", "papir"]

print(f"Hei {spiller_navn}!")
print(f"Du er {alder} år gammel")
print("Du kan velge mellom:", valg)

poeng = 0
er_første_spill = True
```