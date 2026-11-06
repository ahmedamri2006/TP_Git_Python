def main():
    print("=== Mon assistant de revision ===")
    nom = input("Quel est votre prenom ? ")
    print(f"Bonjour {nom} ! Bon courage pour tes revisions.")
    matiere=input("quelles matiere revise tu")
    print(f"tu revises :{matiere}.")
    duree = input("Combien de minutes vas-tu reviser ? ")
    print(f"Objectif : reviser {matiere} pendant {duree} minutes.")
main()