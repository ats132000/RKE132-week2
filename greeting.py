#alusta programm
#kusi kasutaja perenime
#kusi kasutaja sugu
#kui sugu on "m", siis väljasta "Tere, harra [perekonnanimi]!"
#kui sugu on "n", siis valjasta "Tere, proua [perekonnanimi]!"
#kui ere tulemast, [perekonnanimi]! (sugu ei olegi tahtis).
#kui kasutaja sisestab midagi muud valjasta "Tere tulemast,[perenimi]! (sugu ei olegi tahtis)
#lopeta programm

sur_name = input ("Kuidas on Teie perenimi?")
#print("Tere, (sur_name)")
gender = input("Sisesta sugu(m-mees voi n-naine):")

if gender == "m":
    print(f"Tere, harra {sur_name}!")
elif gender == "n":
    print(f"Tere, proua {sur_name}!")
else:
    print(f"Tere tulemast, {sur_name}! (sugu ei olegi tahtis)")
    