# -*- coding: utf-8 -*-
"""
Created on Wed May 18 09:12:43 2016

@author: silver
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


class Organism:
    
    def __init__(self, grid=10, x, y):
        
        self.grid = grid
        self.x = x
        self.y = y
        if self.x ==0 and self.y ==0:
            self.neighbor = {0:[0,1],1:[1,1],2:[1,0]}
        elif self.x==0 and self.y !=0 and self.y != self.grid:
            self.neighbor = {0:[0,1],1:[1,1],2:[1,0],3:[1,-1],4:[0,-1]}
        elif self.x ==0 and self.y ==self.grid:
            self.neighbor = {0:[1,0],1:[1,-1],2:[0,-1]}
        elif self.x !=0 and self.x !=self.grid and self.y ==9:
            self.neighbor = {0:[1,0],1:[1,-1],2:[0,-1],3:[-1,-1],4:[-1,0]}
        elif self.x ==9 and self.y ==9:
            self.neighbor = {0:[0,-1],1:[-1,-1],2:[-1,0]}
        
class Animal(Organism):
    '''
    class for general animal
    '''
    
    def __init__(self, size=10.0, walk=2.0, run=10.0, \
    energyTotal=100.0, energy = 100.0, walkEn=0.2, runEn=1.0, \
    lifespan=500, life= 500, x=0, y=0, grid = 10, inHeat=False):
        
        Organism.__init__(self,grid,x,y)
        
        self.size = np.random.normal(size) #How large it is
        self.walk = np.random.normal(walk) #How fast is can walk
        self.run = np.random.normal(run) #How fast it can run
        self.energyTotal = np.random.normal(energyTotal) #How much total energy it can have
        self.energy = np.random.normal(energyTotal) #how much energy is currently has
        self.walkEn = np.random.normal(walkEn) #How much energy it takes to walk one step
        self.runEn = np.random.normal(runEn) #How much energy is takes to run one step
        self.lifespan = np.random.normal(lifespan) #How long it will live
        self.life = np.random.normal(life) #How many time steps it has
        self.inHeat = inHeat #if it is in heat and willing to breed
    
    def move(self, x=0, y=0, isRunning = False):
        '''
        one step in a direction, sl
        '''
        
        if isRunning == False:
            self.x += x*self.walk
            self.y += y*self.walk
            
        elif isRunning == True:
            self.x += x*self.run
            self.y += y*self.run
            
    def breed(self, other):
        '''
        breeds two animals, generating child with random traits based on
        normal distrobution with average of parent's traits (allows for mutations)
        '''
        baby = type(self)()
        baby.size = np.random.normal(loc=(self.size+ other.size)/2)
        baby.walk = np.random.normal((self.walk+other.walk)/2)
        baby.run = np.random.normal((self.run+other.run)/2)
        baby.energyTotal = np.random.normal((self.energyTotal+other.energyTotal)/2)
        baby.energy = baby.energyTotal
        baby.walkEn = np.random.normal((self.walkEn+other.walkEn)/2)
        baby.runEn = np.random.nomral((self.runEn+other.runEn)/2)
        baby.lifespan = np.random.normal((self.lifespan+other.lifespan)/2)
        baby.life = baby.lifespan
        
        return baby
        
        
    def eat(self,food):
        self.energy += (food.life/food.lifetime)*food.size
        self.energy = np.min(self.energy, self.energyTotal)
        
        
        
class Plant(Organism):
    '''
    class for general plant 
    '''
    
    def __init__(self, maxSize=5.0, size=5.0, lifetime=100, life=100, x=0, y=0):
        
        self.maxSize = np.random.normal(maxSize) #How large the plant can be        
        self.size = np.random.normal(size) #How large the plant is
        self.lifetime = np.random.normal(lifetime) #How many time steps the plant can live
        self.life = np.random.normal(life) #how many time steps the plant has left
        self.x = x #Its x-axis position
        self.y = y #Its y-axis position
        
    def grow(self):
        if self.size < self.maxSize:
            self.size += np.random.random()
            self.size = np.min(self.size, self.maxSize)
                
    def spread(self):
        newPlant = type(self)()
        newPlant.size = np.random.normal(self.size)
        newPlant.maxSize = np.random.normal(self.maxSize)
        newPlant.lifetime = np.random.normal(self.lifetime)
        newPlant.life = newPlant.lifetime
        newPlant.x = self.x
        newPlant.y = self.y
        if bool(random.getrandbits(1)) == True:
            newPlant.x +=1
        else:
            newPlant.x -=1
        if bool(random.getrandbits(1)) == True:
            newPlant.y +=1
        else:
            newPlant.y -=1
        return newPlant
            
        
class Ecosystem:
    '''
    Class for entire ecosystem of plants, herbivores, and carnivores
    '''
    
    def __init__(self, fig, sPlants=0, lPlants=0, sHerb=0, lHerb=0, sCarn=0, lCarn=0, size=10):
        
        self.sPlants = []
        #self.lPlants = []
        #self.sHerb = []
        #self.lHerb = []
        #self.sCarn = []
        #self.lCarn = []
        
        for i in range(sPlants):
            self.sPlants.append(Plant(x=np.random.randint(0,size), y=np.random.randint(0,size)))
        
        self.fig = fig

        
    def __getitem__(self,index):
        return self.sPlants[index]
        
    def plot(self):
        for i in range(len(self.sPlants)):
            plt.plot(self.sPlants[i].x, self.sPlants[i].y, color='g')
        
    
    def timeStep(self):
        for i in range(len(self.sPlants)):
            self.sPlants[i].grow()
            if np.random.random_sample() < 0.3:
                self.sPlants.append(self.sPlants[i].spread())
            self.sPlants[i].life -=1
        #self.show()
                
    def init(self):
        #fig = plt.figure(figsize=(10,8))
        self.plot()
            
        #plt.show()
    
    def animate(self,i):
        self.timeStep()
        self.plot()
        #plt.show()
    
    def display(self, frames):
        ani = animation.FuncAnimation(self.fig, self.animate, frames, init_func=self.init())
        plt.show()
        
    
        
        
    
figure = plt.figure(figsize=(10,8))
newEco = Ecosystem(sPlants = 5, fig=figure)
newEco.display(50)
#plt.show()

    
