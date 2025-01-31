
tall = 5
tall2 = 2

if tall > tall2:
    print(f"{tall} er større enn {tall2}")
else:
    print(f"{tall} er ikke større enn {tall2}")


gyldige_trekk = ["stein", "saks", "papir"]

trekk = "stein"
trekk2 = "pistol"

if trekk in gyldige_trekk:
    print(f"{trekk} er et gyldig trekk")

if trekk2 in gyldige_trekk:
    print(f"{trekk2} er et gyldig trekk")
else:
    print(f"{trekk2} er ikke et gyldig trekk")

trekk3 = "steinn"

if trekk3 == "stein" or trekk3 == "saks" or trekk3 == "papir":
    print(f"{trekk3} er et gyldig trekk")


def sjekk_gyldig_trekk(trekk):
    for gyldig_trekk in gyldige_trekk:
        print([bokstav in gyldig_trekk 
                for bokstav in trekk])
        if all([bokstav in gyldig_trekk 
                for bokstav in trekk]):
            return True
    return False

trekk = input("Velg stein, saks eller papir: ").lower().strip()
gyldig = sjekk_gyldig_trekk(trekk)
if gyldig:
    print(f"{trekk} er et gyldig trekk")
else:    
    print(f"{trekk} er ikke et gyldig trekk")