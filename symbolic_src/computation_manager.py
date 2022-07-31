import math
from symbolic_src.gene import gene
from symbolic_src.geneset import geneset


class computation_manager:
    def compute(self, genes : list[gene], x : float):
        """ Computes the result of the geneset on the given x """
        result = 0.0
        for gene in genes:
            if gene.get_operation() == geneset.Add:
                result += gene.get_value()
            elif gene.get_operation() == geneset.Subtract:
                result -= gene.get_value()
            elif gene.get_operation() == geneset.Multiply:
                result *= gene.get_value()
            elif gene.get_operation() == geneset.Pow:
                result += x**gene.get_value()
            elif gene.get_operation() == geneset.Sin:
                result += math.sin((x * gene.get_value()))
            elif gene.get_operation() == geneset.Cos:
                result += math.cos((x * gene.get_value()))
            elif gene.get_operation() == geneset.Inv:
                result += 1.0 / gene.get_value()
            elif gene.get_operation() == geneset.Sqrt:
                result += math.sqrt((x * gene.get_value()))
            elif gene.get_operation() == geneset.Pow3:
                result += gene.get_value()**3

        return result