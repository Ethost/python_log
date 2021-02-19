def listing():
    check=0
    CUSTOMERCODE=input("\n\t [+] Entrer le customer code: \n\t\t> ")

    with open('host.txt', 'r') as fl:
                for line in fl.readlines() :
                        if CUSTOMERCODE in line:
                            tmp=line.split("|")
                            print("\n\t\t -",CUSTOMERCODE,':\n\t\t\t Nom:',tmp[1],'\n\t\t\t IP:',tmp[2])
                            check=1
                if check!=1:
                    print("\n\t [!] Le customer code entré n'est pas dans la base de donnée.\n\t\t->", CUSTOMERCODE)

def repeat():
    repeat=input("\n\t [+] Voulez-vous recommencer le script? (Oui/Non) \n\t\t>")
    return repeat

def pathlog():
    check=0
    path=""
    tmp=[]
    CUSTOMERCODE=input("\n\t [+] Entrer le customer code: \n\t\t> ")
    NAME=input("\n\t [+] Entrer le nom de l'appareil(RT1,SW1..): \n\t\t> ")
    MOUNTH=input("\n\t [+] Entrer le mois des logs recherché (01,02..): \n\t\t> ")
    DAY=input("\n\t [+] Entrer le jour des logs recherché (1,2..): \n\t\t> ")

    with open('host.txt', 'r') as fl:
        for line in fl.readlines() :
                if CUSTOMERCODE in line:
                    tmp=line.split("|")
                    if tmp[1]==NAME:
                        path="/var/log/cisco/" + tmp[2].rstrip('\n') + "/" + MOUNTH + "/" + DAY + "/cisco.log"
                        check=1
    if check!=1:
        print("\n\t [!] Aucune donnée pour",CUSTOMERCODE,"à l'appareil",NAME,"en date du %s/%s" %(MOUNTH, DAY))


    return path

def main():
    choose=0
    while choose==0:
        print("\n\t [+] Choisissez l'une des options suivantes(1,2..):\n")
        print("\t\t |> 1. Afficher la liste des appareils d'un client.")
        print("\t\t |> 2. Afficher toutes les logs d'un appareils cisco.")
        print("\t\t |> 3. Sortir.")
        try:
            choose=int(input("\n\t\t -> "))
        except Exception as e:
                print('Error: %s' %(e))

        if choose == 1:
            listing()

        elif choose == 2:
            path=pathlog()
            try:
                with open(path, 'r') as log:
                    print(log.read())
            except Exception as e:
                print('Error: %s' %(e))

        elif choose==3:
            exit()

        else:
            print("\t\n [!] Vous n'avez pas choisis l'une des options afficher.")

        if repeat()=='Oui':
            main()
        else:
            exit()
main()
