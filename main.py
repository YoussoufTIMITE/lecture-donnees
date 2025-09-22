#### Imports et définition des variables globales

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename, mode="r", encoding="utf8") as f:
        lines = f.readlines()
    # Chaque ligne devient une liste d'entiers
    data = [list(map(int, line.strip().split(';'))) for line in lines if line.strip()]
    return data

def get_list_k(data, k):
    # Retourne la k-ième liste (indice k)
    return data[k]

def get_first(l):
    return l[0] if l else None

def get_last(l):
    return l[-1] if l else None

def get_max(l):
    return max(l) if l else None

def get_min(l):
    return min(l) if l else None

def get_sum(l):
    return sum(l) if l else None


#### Fonction principale


def main():
    data = read_data(FILENAME)
    print("Données lues :")
    for i, l in enumerate(data):
        print(f"Ligne {i}: {l}")

    if data:
        print("Première liste:", get_first(data))
        print("Dernière liste:", get_last(data))
        print("Max de la première liste:", get_max(data[0]))
        print("Min de la première liste:", get_min(data[0]))
        print("Somme de la première liste:", get_sum(data[0]))

        # Test get_list_k
        k = 0
        print(f"Liste d'indice {k}:", get_list_k(data, k))

        # Test sur la 10e liste (indice 9)
        k_test = 9
        if len(data) > k_test:
            l_test = get_list_k(data, k_test)
            print(f"\nTest sur la liste d'indice {k_test} : {l_test}")
            print("Premier élément:", get_first(l_test))
            print("Dernier élément:", get_last(l_test))
            print("Max:", get_max(l_test))
            print("Min:", get_min(l_test))
            print("Somme:", get_sum(l_test))

    # Test sur une liste vide
    l_vide = []
    print("\nTest sur une liste vide:")
    print("Premier élément:", get_first(l_vide))
    print("Dernier élément:", get_last(l_vide))
    print("Max:", get_max(l_vide))
    print("Min:", get_min(l_vide))
    print("Somme:", get_sum(l_vide))


if __name__ == "__main__":
    main()
