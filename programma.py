def ierakstit(teksts, faila_nosaukums):
    fails = open(faila_nosaukums, "w", encoding='utf-8')
    fails.write(teksts)
    fails.close()

# ierakstit("Sveiki!" "  " "Draugi, nav labi!", "tekstam/teksts.txt")

def pierakstit(teksts, faila_nosaukums):
    fails = open(faila_nosaukums, "a", encoding='utf-8')
    fails.write(teksts)
    fails.close()

# pieierakstit("\n jauns saturs!!!", "tekstam/teksts.txt")

def nolasit(faila_nosaukums):
    with open(faila_nosaukums, "r", encoding='utf-8') as fails:
        rindas = fails.readlines()
    return rindas

# print(nolasit("tekstam/teksts.txt"))

vardi = ["Saulvedis", "Delle", "Adriana", "Ita", "Dainis"]
uzvardi = ["Krauklis", "Novada", "Maurina", "Kozakevica", "Īvāns"]
vecums = [24, 18, 14, 45, 37]
dzimums = ["v", "s", "s", "s", "v"]
statuss = ["Neprecējies", "Neprecējies", "Neprecējies", "Precējies", "Precējies"]

ierakstit("", "tekstam/cilveki.txt")
for i in range( len(vardi) ):
    if dzimums[i] == "s":
        rakstamais = "sieviete"
    else:
        rakstamais = "vīrietis"
    teksts = "{} {} - {}, {}, {} \n".format(vardi[i], uzvardi[i], vecums[i], rakstamais, statuss[i])
    pierakstit(teksts, "tekstam/cilveki.txt" )

# Izveidojas fails, kur katrā rindiņā ir vārds, uzvārds - vecums

def uzrakstit_vestuli(vards, uzvards, dzimums, vecums, index):
    if dzimums == "s":
        sveiciens = "Sveika"
        laimets = "Jūs esat laimējusi"
    else:
        sveiciens = "Sveiks"
        laimets = "Jūs esat laimējis"
        

    vestule = open("vestules/vestule{}.txt".format(index), "w", encoding="utf-8")
    vestule.write("{}, {} {}! \n".format(sveiciens, vards, uzvards))
    vestule.write("{} {} EUR!".format(laimets, vecums*100))

    return

# Faili, kuru nosaukums ir vestule0.txt, 
# saturs - Sveiki, Marta! Jūs esat laimējusi vecums*100 (3200) dolārus!

def apstradat_datus(dati):
    dati = dati.split()
    if dati[4] == "Sieviete,":
        dzimums = "s"
    else:
        dzimums = "v"
    return [dati[0], dati[1], dzimums, int(dati[3][:-1])]



cilveki = nolasit("tekstam/cilveki.txt")
index = 1
for cilveks in cilveki:
    cilveka_dati = apstradat_datus(cilveks)
    uzrakstit_vestuli(cilveka_dati[0], cilveka_dati[1], cilveka_dati[2], cilveka_dati[3], index)
    index+=1

