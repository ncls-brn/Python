import crew

members = [
    {
        "first_name": "Bel",
        "last_name": "Riose",
        "gender": "M",
        "age": 48,
        "role": "commandant",
    },
    {
        "first_name": "Gaal",
        "last_name": "Dornick",
        "gender": "F",
        "age": 34,
        "role": "technicien",
    },
    {
        "first_name": "Salvor",
        "last_name": "Hardin",
        "gender": "F",
        "age": 28,
        "role": "PiLoTe",
    },
]

# crew.display_crew(members)
# crew.remove_member(members)
# crew.check_crew(members)

while True:
    print("\n MENU :")
    print("1. Ajouter un membre")
    print("2. Supprimer un membre")
    print("3. Afficher l'équipage")
    print("4. Vérifier l'équipage")
    print("5. rapport d'équipage")
    print("6. Quitter le menu")

    choice = int(input("Choisissez l'option souhaitée : "))

    match choice:
        case 1:
            crew.add_member(members)
        case 2:
            crew.remove_member(members)
        case 3:
            crew.display_crew(members)
        case 4:
            crew.check_crew(members)
        case 5:
            crew.crew_report(members)
        case 6:
            break
        case _:
            print("Le choix sélectionné n'existe pas.")
