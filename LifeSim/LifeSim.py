# -*- coding: utf-8 -*-
"""
Created on Wed May 18 09:12:43 2016

@author: silver
"""
import numpy as np
import matplotlib.pyplot as plt


class sHerb:
    '''
    class for a small herbivore (rabbit)
    '''
    
    def __init__(self, size=10.0, walk=2.0, run=10.0, \
    energyTotal=100.0, energy = 100.0, walkEn=0.2, runEn=1.0, \
    lifespan=500, life= 500, x=0, y=0, mate=False):
        
        self.size = size #How large it is
        self.walk = walk #How fast is can walk
        self.run = run #How fast it can run
        self.energyTotal = energyTotal #How much total energy it can have
        self.energy = energyTotal #how much energy is currently has
        self.walkEn = walkEn #How much energy it takes to walk one step
        self.runEn = runEn #How much energy is takes to run one step
        self.lifespan = lifespan
        self.life = life #How many time steps it will live
        self.x = x #It's x axis position
        self.y = y #It's y axis position
    
    def move(self, n, m, speed ='walk'):
        '''
        one step in a direction
        '''
        
        if speed == 'walk':
            self.x += n*self.walk
            self.y += m*self.walk
            
        elif speed == 'run':
            self.x += n*self.run
            self.y += m*self.run
            
    def breed(self, other):
        '''
        breeds two animals, generating child with random traits based on
        normal distrobution with average of parent's traits
        '''
        baby = sHerb()
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
        
        
        
        
class lHerb:
    '''
    Class for a large herbivore (deer)
    '''
    
    def __init__(self, size=100.0, walk=3.0, run=15.0, \
    energyTotal=500.0, energy = 500.0, walkEn=0.4, runEn=2.0,\
    lifespan=5000, life=5000, x=0, y=l0, mate=False):
        
        self.size = size #How large it is
        self.walk = walk #How fast it walks
        self.run = run #How fast it runs
        self.energy = energy #How much total energy it can have
        self.walkEn = walkEn #How much energy it takes to walk one step
        self.runEn = runEn # How much energy it takes to run one step
        self.lifespan = lifespan #How many time steps it will live
        self.life = lifespan #How much life it currently has
        self.x = x #Its x-axis position
        self.y = y #Its y-axis position
        
    def move(self, n, m, speed = 'walk'):
        
        if speed == 'walk':
            self.x += n*self.walk
            self.y += m*self.walk
            
        elif speed == 'run':
            self.x += n*self.run
            self.y += m*self.run
            
    def breed(self, other):
       '''
       breeds two animals, generating child with random traits based on
       normal distrobution with average of parent's traits
       '''
       baby = lHerb()
       baby.size = np.random.normal(loc=(self.size+ other.size)/2)
       baby.walk = np.random.normal((self.walk+other.walk)/2)
       baby.run = np.random.normal((self.run+other.run)/2)
       baby.energyTotal = np.random.normal((self.energy+other.energy)/2)
       baby.energy=baby.energyTotal
       baby.walkEn = np.random.normal((self.walkEn+other.walkEn)/2)
       baby.runEn = np.random.nomral((self.runEn+other.runEn)/2)
       baby.lifespan = np.random.normal((self.lifespan+other.lifespan)/2)
       baby.life = baby.lifespan
       
       return baby
       
      
    def eat(self,food):
        self.energy += (food.life/food.lifetime)*food.size
        if self.energy > self.energyTotal:
            self.energy = self.energyTotal
        
        
        
class sPlant:
    '''
    class for a small plant (dandelion)
    '''
    
    def __init__(self, maxSize=5.0, size=5.0, lifetime=100, life=100, x=0, y=0):
        
        self.maxSize = maxSize #How large the plant can be        
        self.size = size #How large the plant is
        self.lifetime = lifetime #How many time steps the plant can live
        self.life = life #how many time steps the plant has left
        self.x = x #Its x-axis position
        self.y = y #Its y-axis position
        
    def grow(self):
        if self.size < self.maxSize:
            self.size += np.random.random()
            if self.size > self.maxSize:
                self.size = self.maxSize
                
        
        
        
        
class lPlant:
    '''
    class for a large plant (bush/tree)
    '''
    
    def __init__(self, size=50.0, lifetime = 10000, life=10000, x=0, y=0):
        
        self.size = size #How large the plant is
        self.lifetime = lifetime #How many time steps the plant will live
        self.life = life #how many time steps the plant has left
        self.x = x #Its x-axis position
        self.y = y #Its y-axis position
        