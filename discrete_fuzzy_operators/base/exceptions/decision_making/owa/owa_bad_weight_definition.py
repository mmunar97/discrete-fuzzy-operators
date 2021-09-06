class OwaBadDefinition(Exception):
    """
    An Exception which indicates that the list of weight is not well-defined. The sum of the entries must be a value
    between 0 and 1, the sum of all entries must be 1 and the vector must be increasing.
    """

    def __init__(self, message: str = "The weight vector is not well-defined. "):
        super().__init__(message)
