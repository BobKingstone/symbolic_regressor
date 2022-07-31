

from tokenize import Double

from symbolic_src.geneset import geneset


class gene:
    def __init__(self, operation : geneset, value: float):
        self.operation = operation
        self.value = value
    
    def get_operation(self):
        """ Returns the operation of this gene """
        return self.operation

    def set_operation(self, operation: geneset):
        """ Sets the operation of this gene """
        self.operation = operation
    
    def get_operation_str(self):
        """ Returns the operation of this gene as a string """
        if self.operation == geneset.Add:
            return "+"
        elif self.operation == geneset.Subtract:
            return "-"
        elif self.operation == geneset.Multiply:
            return "*"
        elif self.operation == geneset.Pow:
            return "^"
        elif self.operation == geneset.Sin:
            return "sin"
        elif self.operation == geneset.Cos:
            return "cos"
        elif self.operation == geneset.Inv:
            return "inv"
        elif self.operation == geneset.Sqrt:
            return "sqrt"
        elif self.operation == geneset.Pow3:
            return "pow3"
        else:
            return ""

    def get_value(self):
        """ Returns the value of this gene """
        return self.value

    def set_value(self, value: float):
        """ Sets the value of this gene """
        self.value = value