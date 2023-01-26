"""
Rayna Sillini
TP4
Introduction à la programmation OO
"""

from math import pi
from random import randint
from dataclasses import dataclass

"""EXERCICE 1"""


class StringFoo:

    def __init__(self):
        self.message = ""

    def set_string(self, msg):
        self.message = msg

    def print_string(self):
        print(f'{self.message.upper()}')


composer_message = StringFoo()
composer_message.set_string("foo")
composer_message.print_string()


"""EXERCICE 2"""


class Rectangle:

    def __init__(self):
        self.longueur = 0
        self.largeur = 0
        self.aire = 0

    def calcul_aire(self):
        self.aire = self.longueur * self.largeur

    def afficher_infos(self):
        print(f"la longueur est {self.longueur}, la largeur est {self.largeur} et l'aire est {self.aire}")


resultat = Rectangle()
resultat.longueur = 10
resultat.largeur = 2
resultat.calcul_aire()
resultat.afficher_infos()


"""EXERCICE 3"""


class Cercle:

    def __init__(self):
        self.rayon = 0
        self.aire = 0
        self.circonference = 0

    def calcul_aire(self):
        self.aire = pi * self.rayon ** 2

    def calcul_circonference(self):
        self.circonference = pi * self.rayon * 2

    def afficher_infos(self):
        print(f"le rayon est {self.rayon}, l'aire est {self.aire} et la circonférence est {self.circonference}")


resultat = Cercle()
resultat.rayon = 11
resultat.calcul_aire()
resultat.calcul_circonference()
resultat.afficher_infos()

"""EXERCICE 4 + 5 + 6"""


class Hero:
    def __init__(self, nom):
        self.force_attaquer = randint(1, 6)
        self.nmbr_de_vies = randint(1, 10) + randint(1, 10)
        self.force_defense = randint(1, 6)
        self.nom = nom
        self.stats_du_joueur = PlayerStats()

    def attaque(self):
        return randint(1, 6) + self.force_attaquer

    def recevoir_attaque(self):
        self.nmbr_de_vies -= randint(1, 6) - self.force_defense
        return self.nmbr_de_vies

    def est_vivant(self):
        return self.nmbr_de_vies > 0


@dataclass
class PlayerStats:
    force: int = randint(1, 20)
    dex: int = randint(1, 20)
    con: int = randint(1, 20)
    intelligence: int = randint(1, 20)
    wis: int = randint(1, 20)
    cha: int = randint(1, 20)
