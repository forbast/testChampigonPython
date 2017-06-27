def reculer(ordonne):
        if ordonne < 380:
                return 8
        return 0

def avancer(ordonne):
        if ordonne > 0:
                return -8
        return 0


def droite(abscisse):
        if abscisse < 550:
                return 8
        return 0


def gauche(abscisse):
        if abscisse > -5:
                return -8
        return 0


def isDead(ordBombe,absBombe,ordonne,abscisse,bombeE,debut):
                if int(ordBombe)-100 < int(ordonne)+30 and int(ordBombe)+50 > int(ordonne)-30 and int(absBombe)-50 < int(abscisse)+30 and int(absBombe)+50 > int(abscisse)-30 and bombeE == 1 and debut == 1:
                         return True
                return False
