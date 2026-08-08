from chaine import ListeChainer

montrain = ListeChainer()
montrain.insérer_au_début(1)
montrain.insérer_au_début(2)
montrain.insérer_au_début(3)
montrain.insérer_à_la_fin(80)
if not montrain.est_vide():
    print(montrain)

