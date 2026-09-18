#algus
#kusi palju klaase on kasutaja paevas vett tarbinud?
#uks klaas=250ml
#paevane kogus=2000ml
#arvuta palju % on kasutaja paeva normist tarbinud
#kui protsent <50, valjasta "Joo rohkem vett, keha vajab seda!"
#kui protsent >50, valjasta "Tubli, jatka samas vaimus!"
#kui protsent >= 100, valjasta "Suureparane, oled oma paevase eesmargi taitnud!"
#lopp



glasses = int(input("Mitu klaasi vett oled tana joonud?"))

water_ml = glasses*250
percentage=water_ml/2000*100
print(f"Oled taitnud {percentage}% paevasest eesmargist.")

if percentage<50:
    print("Joo rohkem vett, su keha vajab seda!")
elif percentage<100:
    print("Tubli, jatka samas vaimus!")
else:
    print("Suureparane, oled oma paevase eesmargi taitnud!")
    