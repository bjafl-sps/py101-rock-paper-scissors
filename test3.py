



liste = [1, 2, 3, 4, 5]

liste2 = [num for num in range(1, 6)]

liste3 = []
for num in range(1, 6):
    liste3.append(num)






#print(range(1, 6))
#print(list(range(1, 6)))

print(liste)

print(1, 2, 3, 4, 5)
print(*liste)
liste2 = ["1", "2", "3", "4", "5"]
print(" ".join(liste2))
print("|".join(str(tall) for tall in liste))

tallrekke = "12345"
liste3 = list(tallrekke)
print(liste3)
tallrekke2 = "".join(liste3)
print(tallrekke2)

trekk_dict = {
    "1": "stein",
    "2": "saks",
    "3": "papir"
}

for trekk_nr in trekk_dict:
    print(trekk_nr, trekk_dict[trekk_nr])

for trekk_nr, trekk in trekk_dict.items():
    print(trekk_nr, trekk)

gyldig = ""
for trekk_nr, trekk in trekk_dict.items():
    gyldig += f'{trekk_nr}, {trekk}, '

print(gyldig)

gyldig = ", ".join([f'{trekk_nr}, {trekk}' 
                    for trekk_nr, trekk in trekk_dict.items()])
print(gyldig)

steg1 = [
    ", ".join([trekk_nr, trekk]) 
    for trekk_nr, trekk in trekk_dict.items()
]

print(steg1)

steg2 = ", ".join(steg1)
print(steg2)
