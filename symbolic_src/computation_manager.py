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

        return result