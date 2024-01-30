def ierakstit(teksts, faila_nosaukums):
    fails = open(faila_nosaukums, "w", encoding='utf-8')
    fails.write(teksts)
    fails.close()

# ierakstit("Sveiki!" "  " "Draugi, nav labi!", "tekstam/teksts.txt")

def pieierakstit(teksts, faila_nosaukums):
    fails = open(faila_nosaukums, "a", encoding='utf-8')
    fails.write(teksts)
    fails.close()

# pieierakstit("\n jauns saturs!!!", "tekstam/teksts.txt")

def nolasit(faila_nosaukums):
    with open(faila_nosaukums, "r", encoding='utf-8') as fails:
        rindas = fails.readline()
    return rindas

print(nolasit("tekstam/teksts.txt"))


vardi = ["Saulvedis", "Delle", "Adriana"]
uzvardi = ["Krauklis", "Novada", "Maurina"]
vecums = [24, 18, 45 ]

ierakstit("", "tekstam/cilveki.txt")
for i in range( len(vardi) ):
    teksts = "{} {} - {} \n".format(vardi[i], uzvardi[i], vecums[i])
    pieierakstit(teksts, "faili/cilveki.txt")