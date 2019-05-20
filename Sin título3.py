# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 11:35:21 2019

@author: INF-322
"""


import array
import random
import math
import numpy

from deap import algorithms
from deap import base
from deap import creator
from deap import tools

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
#creator.create("Individual", array.array, typecode='b', fitness=creator.FitnessMax)
creator.create("Individual", array.array, typecode='d', fitness=creator.FitnessMax)

toolbox = base.Toolbox()

# Attribute generator
#toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("attr_bool", random.randint, 0, 10)

# Structure initializers
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, 8)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def cuadrado(individual):
    y = [256,128,64,32,16,8,4,2,1]
    posicion=len(individual)-1
    suma = 0
    for i in range(len(individual)):
        suma = suma + (individual[posicion]*y[posicion])
        posicion=posicion-1
    suma=suma**2
    return suma,

def mayor(individual):
    return max(individual),


def cxTwoPoint2(ind1, ind2):
    """Executes a two-point crossover on the input :term:`sequence`
    individuals. The two individuals are modified in place and both keep
    their original length.

    :param ind1: The first individual participating in the crossover.
    :param ind2: The second individual participating in the crossover.
    :returns: A tuple of two individuals.

    This function uses the :func:`~random.randint` function from the Python
    base :mod:`random` module.
    """
    size = min(len(ind1), len(ind2))
#    cxpoint1 = random.randint(1, size)
#    cxpoint2 = random.randint(1, size - 1)
    cxpoint1 = 5
    cxpoint2 = 6
    if cxpoint2 >= cxpoint1:
        cxpoint2 += 1
    else: # Swap the two cx points
        cxpoint1, cxpoint2 = cxpoint2, cxpoint1

    ind1[cxpoint1:cxpoint2], ind2[cxpoint1:cxpoint2] \
        = ind2[cxpoint1:cxpoint2], ind1[cxpoint1:cxpoint2]

    return ind1, ind2

def mutFlipBit2(individual):
    """Flip the value of the attributes of the input individual and return the
    mutant. The *individual* is expected to be a :term:`sequence` and the values of the
    attributes shall stay valid after the ``not`` operator is called on them.
    The *indpb* argument is the probability of each attribute to be
    flipped. This mutation is usually applied on boolean individuals.

    :param individual: Individual to be mutated.
    :param indpb: Independent probability for each attribute to be flipped.
    :returns: A tuple of one individual.

    This function uses the :func:`~random.random` function from the python base
    :mod:`random` module.
    """
    for i in range(len(individual)):
        individual[i] = type(individual[i])(not individual[i])

    return individual,

toolbox.register("evaluate", mayor)
toolbox.register("mate", cxTwoPoint2)
toolbox.register("mutate", mutFlipBit2)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    random.seed(64)
    
    pop = toolbox.population(n=300)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)
    
    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=3, 
                                   stats=stats, halloffame=hof, verbose=True)
    
    return pop, log, hof

if __name__ == "__main__":
    pop, log, hof = main()
    print(hof)

    