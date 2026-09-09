""" Kirjutame koos programmi, mis küsib kasutajalt, mis päev on homme (tööpäev või puhkepäev), ning väljastab vastuse põhjal
kasutaja sisestab ühe sõna:
"tööpäev"
või "puhkepäev" """

#alusta programmi
#kusi kasutjalt: "Mis paev on homme? (toopaev/puhkepaev)"
#salvesta vastus muutujasse day
#kui day on vordne sonaga "toopaev", siis valjasta ekraanile: "Ma lahen magama, head ood!"
#muidu kui day on vordne"puhkepaev" valjasta ekraanile "Veel uks osa Netflixist!"
#muidu kui sisestus polnud oige valjasta ekraanile "Vale vaartus!"
#lopeta programm

""" day = input("Mis paev on homme? (toopaev/puhkepaev):")

if day == "toopaev":
    print("Ma lahen magama, head ood!")
elif day == "puhkepaev":
    print("Veel uks osa Netflixist!")
else:
    print("Vale vaartus!") """



#finantsnoustaja
""" Sa tahad osta endale uue iPhone 17 Pro, aga sa oled otsustanud, et krediiti sa ei võta. Selle asemel oled sa palunud range
ja vastutustundliku finantsnõustaja programmi kujul.
See programm:
- küsib, kui palju sul on praegu raha,
- võrdleb seda iPhone 17 Pro hinnaga (näiteks 2 500 €),
- ja annab sulle täiesti ratsionaalse, emotsioonideta soovituse. """


""" print("Tere tulemast programmi 'Finantsnoustaja'!")
print("Sinu isiklik noustaja ei tee emotsionaalseid oste.")

money = int(input("Kui palju raha sul on praegu?"))

if money < 2500:
    print("Sul pole praegu piisavalt raha. Ole hoolas ja kogu edasi!")
elif money == 2500:
    print("Palju onne saad osta endale uue Iphone 17 Pro sularahas!")
else:
    print("Saad osta uue Iphone 17 Pro ja jaab raha veel ulegi.") """




#sammulugeja

""" Sul on eesmärk teha iga päev 10 000 sammu. Programm küsib kasutajalt, mitu sammu ta on juba teinud, arvutab täitmise
protsendi ja annab tagasisidet.
- Kui protsent < 50: „Alles poolel teel, liigu edasi!“
- Kui protsent < 75: „Tubli, oled peaaegu kohal!“
- Kui protsent ≥ 100: „Palju õnne, oled oma eesmärgi täitnud!“
"""

goal = 10000
steps = int(input("Mitu sammu oled juba teinud?"))

percent = (100*steps)/10000 

print(f"{percent}%")

if percent <50:
    print("Alles poolel teel liigu edasi!")
elif percent <75:
    print("Tubli, oled peaaegu kohal!")
elif percent <100:
    print("Suureparane oled peaaegu kohal!")
else:
    print("Palju onne, oled oma eesmargi taitnud!")


