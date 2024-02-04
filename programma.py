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

ierakstit("", "tekstam/cilveki.txt")
for i in range( len(vardi) ):
    if dzimums[i] == "s":
        rakstamais = "sieviete"
    else:
        rakstamais = "vīrietis"
    teksts = "{} {} - {}, {} \n".format(vardi[i], uzvardi[i], vecums[i], rakstamais)
    pierakstit(teksts, "tekstam/cilveki.txt" )

# Izveidojas fails, kur katrā rindiņā ir vārds, uzvārds - vecums

ierakstit("", "tekstam/cilveks0.txt")
for i in range( len(vardi) ):
    if dzimums[i] == "s":
        sveiciens = "Sveika"
    else:
        sveiciens = "Sveiks"

for i in range( len(vardi) ):
    if dzimums[i] == "s":
        laimets = "Jūs esat laimējusi"
    else:
        laimets = "Jūs esat laimējis"

    teksts = "{}, {} {}, {} \n".format(sveiciens, vardi[i], uzvardi[i], laimets)
    pierakstit(teksts, "tekstam/cilveks0.txt")

    balva = "{} {} \n".format(vecums[i]*100, "dolārus!!!! :)))")
    pierakstit(balva, "tekstam/cilveks0.txt")

# Faili, kuru nosaukums ir cilveks0.txt, 
# saturs - Sveiki, Marta! Jūs esat laimējusi vecums*100 (3200) dolārus!