class FuzzyOperatorSizeException(Exception):
    """
    An Exception which indicates that the associated matrix of the operator has invalid shape.
    """

    def __init__(self, message: str = "Only squared matrices are valid to represent a fuzzy operator."):
        super().__init__(message)
