import math
import random
from symbolic_src.computation_manager import computation_manager
from symbolic_src.gene import gene
from symbolic_src.geneset import geneset


class chromosome:
    def __init__(self):
        self.genes = []
        self.computator = computation_manager()

    def generate_parent_chromosome(self, length : int):
        """ Generates a random chromosome """
        for i in range(0, length):
            self.genes.append(self.generate_gene())

    def clone(self):
        """ Returns a clone of this chromosome """
        clone = chromosome()
        for g in self.genes:
            clone.genes.append(gene(g.get_operation(), g.get_value()))
        return clone

    def generate_gene(self):
        """ Generates a gene """
        count = len(geneset)
        gene_value = (random.uniform(0, 1) * 2)
        gene_index = random.randint(0, count - 1)
        gene_operation = geneset(gene_index)

        return gene(gene_operation, gene_value)
    
    def mutate(self):
        """ Mutates this chromosome """
        idx = random.randint(0, len(self.genes) - 1)
        self.genes[idx] = self.generate_gene()

    def get_fitness(self, items: list[(float, float)]):
        """ Returns the fitness of this chromosome """
        fitness = 0.0

        for item in items:
            fitness -= abs(item[1] - self.computator.compute(self.genes, item[0]))
        
        return fitness

    def display(self):
        """ Displays this chromosome textual representation """
        result = ""
        prefix = ""
        for gene in self.genes:
            if gene.get_operation() == geneset.Add:
                result += "+" + str(gene.get_value())
            elif gene.get_operation() == geneset.Subtract:
                result += "-" + str(gene.get_value())
            elif gene.get_operation() == geneset.Multiply:
                prefix += "("
                result += ")*" + str(gene.get_value())
        
        return prefix + "0" + result