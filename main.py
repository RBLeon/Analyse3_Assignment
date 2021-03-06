from Catalog import Catalog
catalog = Catalog()
# Dit is hoe je een loanId kan pakken van een user
# user = catalog.returnUsers()[1].getBookLoans()[0].getUserId()
# catalog.reserveer_boek(catalog.returnUsers()[0], catalog.returnUsers()[0].getUserId())
start_reservering = True
start_reservering_gebruiker = True
start_keuze = None
start_keuze_gebruiker = "5"
while start_reservering or start_keuze == "0":
    start_reservering_gebruiker = True
    # Het menu als je niet bent ingelogd
    print("***** Reserverings systeem *****")
    start_keuze = input("1) Bekijk boeken \n2) Filter boeken \n3) Login \n4) Exit\n")

    if start_keuze == "1":
        print("***** Bekijk boeken *****")
        catalog.printBooks()
        start_keuze = input("Press enter to continue.")
    if start_keuze == "2":
        print("***** Filter boeken *****")
        catalog.filter()
        start_keuze = input("Press enter to continue.")
    if start_keuze == "4":
        print("***** See you later! *****")
        start_reservering = False
        break
    if start_keuze == "3":
        print("***** Login *****")
        catalog.login()
        if catalog.loggedInUser != None and catalog.loggedInUser.isAdmin() == "False":
            while start_reservering_gebruiker:
                print("***** Reserverings systeem *****")
                print("***** Welkom " + catalog.loggedInUser.getFirstName() + " *****")
                start_keuze_gebruiker = input("1) Bekijk boeken \n2) Filter boeken"
                                                " \n3) Reserveer een boek \n4) Logout\n")
                while start_keuze_gebruiker == "1":
                    print("***** Bekijk boeken *****")
                    catalog.printBooks()
                    start_keuze_gebruiker = input("Press enter to continue.")
                while start_keuze_gebruiker == "2":
                    print("***** Filter boeken *****")
                    catalog.filter()
                    start_keuze_gebruiker = input("Press enter to continue.")
                while start_keuze_gebruiker == "3":
                    print("***** Reserveer een boek *****")
                    catalog.reserveer_boek(catalog.loggedInUser, catalog.loggedInUser.getUserId())
                    start_keuze_gebruiker = input("Press 5 to go back")
                if start_keuze_gebruiker == "4":
                    catalog.loggedInUser = None
                    start_keuze = "0"
                    start_reservering_gebruiker = False
        elif catalog.loggedInUser != None and catalog.loggedInUser.isAdmin() == "True":
            while start_reservering_gebruiker:
                print("***** Reserverings systeem *****")
                print("***** Welkom " + catalog.loggedInUser.getFirstName() + " *****")
                start_keuze_gebruiker = input("1) Bekijk boeken \n2) Filter boeken "
                                              " \n3) Voeg een boek toe \n4) Voeg een gebruiker toe \n"
                                              "5) Voeg een gebruiker toe met admin rechten\n6) Logout\n7) "
                                              "Restore from backup\n8) Save to backup\n")

                while start_keuze_gebruiker == "1":
                    print("***** Bekijk boeken *****")
                    catalog.printBooks()
                    start_keuze_gebruiker = input("Press enter to continue")
                while start_keuze_gebruiker == "2":
                    print("***** Filter boeken  *****")
                    catalog.filter()
                    start_keuze_gebruiker = input("Press enter to continue.")
                # nieuw boek toevoegen
                while start_keuze_gebruiker == "3":
                    print("***** Voeg een boek toe *****")
                    catalog.addBook()
                    start_keuze_gebruiker = input("Press enter to continue.")
                # nieuwe gebruiker toevoegen
                while start_keuze_gebruiker == "4":
                    print("***** Voeg een nieuwe gerbuiker toe *****")
                    catalog.addPerson()
                    start_keuze_gebruiker = input("Press enter to continue.")
                while start_keuze_gebruiker == "5":
                    print("***** Voeg een nieuwe gerbuiker toe *****")
                    catalog.addPerson(True)
                    start_keuze_gebruiker = input("Press enter to continue.")
                if start_keuze_gebruiker == "6":
                    catalog.loggedInUser = None
                    start_keuze_gebruiker = input("Press enter to continue.")
                    start_reservering_gebruiker = False
if start_keuze == "4":
    start_reservering = False
