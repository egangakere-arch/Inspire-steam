# Name : Gabriel Egan Gakere
# Date : 23/02/2026
# A program to show inheritance in python

from turtle import color


class Animal(self, species, weight, diet):
    def __init__(self, species, weight, diet):
        self.species = species
        self.weight = weight
        self.diet = diet

    def grow(self,weight, diet):
        weight = 1.1 * weight
        diet = "more " + diet
        print(f"{self.species} is growing and now weighs {weight} and eats {diet}")



    def eat(self, diet):
        print(f"{self.species} is eating {diet}")





class Dog(Animal):
    def __init__(self, weight, diet, sound):
        super().__init__(species, weight, diet)
        self.weight = weight
        self.diet = diet
        self.color = color
        self.sound = sound

    def Barks(self):
        weight = 1.1 * weight
        diet = "more " + diet
        sound = "barks"
        print(f"The dog {sound} and weighs {weight} and eats {diet}")



    def eat(self, diet):
        print(f"{self.species} is eating {diet}")




class Horse(Animal):
    def __init__(self, species, weight, diet):
        self.species = species
        self.weight = weight
        self.diet = diet

    def grow(self,weight, diet):
        weight = 1.1 * weight
        diet = "more " + diet
        print(f"{self.species} is growing and now weighs {weight} and eats {diet}")



    def eat(self, diet):
        print(f"{self.species} is eating {diet}")