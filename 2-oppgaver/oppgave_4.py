# Stein Saks Papir - Utviklingsoppgave

# Bruk startkoden under for å lage et enkelt spill av Stein, Saks, Papir.
# Se videre instruksjoner i oppgaveteksten, 1-instruksjoner/4-stein_saks_papir.md
#
# Den brune teksten under hver funksjon er en 'docsrting'. Denne beskriver 
# hva funksjonen skal gjøre, og brukes til å gi andre (inkludert deg selv)
# informasjon om koden du har skrevet. Vi kan gå mer inn i dette senere.
#
# Lykke til!

from random import choice

# Liste med gyldige valg
GYLDIGE_VALG = ["stein", "saks", "papir"]

def faa_spiller_valg():
    """
    Ber om og returnerer spillerens valg.
    Fortsetter å spørre til et gyldig valg er gitt.
    """
    # TODO: Implementer denne funksjonen
    pass # Fjern denne linjen når du har begynt å skrive koden

def spill_runde():
    """
    Spiller én runde av spillet.
    Returnerer True hvis spilleren vil spille igjen, False hvis ikke.
    """
    # TODO: Implementer denne funksjonen
    pass # Fjern denne linjen når du har begynt å skrive koden

def start_spill():
    """
    Hovedfunksjonen som kjører spillet.
    """
    print("Velkommen til Stein, Saks, Papir!")
    # TODO: Implementer denne funksjonen

if __name__ == "__main__":
    start_spill()