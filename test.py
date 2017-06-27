import function
 
assert function.reculer(200) == 8  # test reculer dans cadre
assert function.reculer(2000) == 0  # test reculer hors cadre

assert function.avancer(200) == -8  # test avancer dans cadre
assert function.avancer(-100) == 0  # test avancer hors cadre

assert function.gauche(-3) == -8  # test gauche dans cadre
assert function.gauche(100) == -8  # test gauche dans cadre
assert function.gauche(-22) == 0  # test gauche hors cadre

assert function.droite(250) == 8  # test droite dans cadre
assert function.droite(2000) == 0  # test droite hors cadre

assert function.isDead(100,100,120,120,1,1) == True  # jeu demarré, bombe explose, bombe proche joueur
assert function.isDead(100,100,200,200,1,1) == False # jeu demarré, bombe explose, bombe loin joueur
assert function.isDead(100,100,120,120,0,1) == False # jeu demarré, bombe explose pas, bombe proche joueur
assert function.isDead(100,100,120,120,1,0) == False # jeu pas demarré, bombe explose, bombe proche joueur
assert function.isDead(100,100,120,120,1,1) == True

