

navn = "Ola Nordmann"
alder = 42



print(f"Hei, {navn}! Du er {alder} år gammel.")
print("Hei, " + navn + "! Du er " + str(alder) + " år gammel.")
print("Hei, {}! Du er {} år gammel.".format(navn, alder))
print("Hei, {0}! Du er {1} år gammel.".format(navn, alder))
print("Hei, {navn}! Du er {alder} år gammel.".format(navn=navn, alder=alder))
print("Hei, %s! Du er %d år gammel." % (navn, alder))

tekst = "     Ola Nordmann;  "
print(tekst)
print(tekst.lower())
print(tekst.strip())
print(tekst.strip().lower())
print(tekst.strip(' ;'))
print(tekst.replace(' ', '').replace(';', ''))


print("\nVelg stein, saks eller papir:")
svar = input("(Skriv inn svar og fortsett med enter)\n")
print(f"Du valgte: {svar}")
print("Du valgte:", svar)
print("Du valgte", svar, sep=": ")

print("stein", "saks", "papir", sep="\n")

input("Velg stein, saks eller papir: ")


