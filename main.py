'encoder une chaine de caractères par une liste de tuples'

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(10000)


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    c = [s[0]]  # liste des caractères rencontrés
    o = [1]     # liste des occurrences correspondantes
    k = 1       # index courant
    n = len(s)
    while k < n:
        if s[k] == c[-1]:
            o[-1] += 1
        else:
            c.append(s[k])
            o.append(1)
        k += 1
    return list(zip(c, o))


def artcode_r(s):
    """retourne la liste de tuples selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    def f(rest, c, n):
        if not rest:
            return [(c, n)]
        if rest[0] == c:
            return f(rest[1:], c, n + 1)
        return [(c, n)] + f(rest[1:], rest[0], 1)

    return f(s[1:], s[0], 1)

    # cas de base
    # recherche nombre de caractères identiques au premier
    # appel récursif


#### Fonction principale


def main():
    ' appel aux fonctions secondaires'
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
