def trie_create(filename):
    with open(filename, "r", encoding="utf-8") as f :
        indice = False
        liste = []
        chaine = ""
        for line in f:
            if ";" in line and indice == True:
                chaine = chaine + line
                indice = False
                liste.append(chaine)
                chaine = ""

            elif indice == True:
                chaine = chaine + line

            elif "CREATE TABLE" in line:
                chaine = chaine + line
                indice = True
        return [s.replace('\n', '') for s in liste]

def trie_alter(filename):
    with open(filename, "r", encoding="utf-8") as f :
        indice = False
        liste = []
        chaine = ""
        for line in f:
            if ";" in line and indice == True:
                chaine = chaine + line
                indice = False
                liste.append(chaine)
                chaine = ""

            elif indice == True:
                chaine = chaine + line

            elif "ALTER TABLE" in line:
                chaine = chaine + line
                indice = True
        return [s.replace('\n', '') for s in liste]
