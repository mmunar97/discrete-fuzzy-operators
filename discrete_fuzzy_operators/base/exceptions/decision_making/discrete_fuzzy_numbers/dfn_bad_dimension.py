class DiscreteFuzzyNumberBadDimension(Exception):
    """
    An Exception which indicates that the dimension of the discrete fuzzy number and the dimension of the discrete
    aggregation functions do not match.
    """

    def __init__(self, message: str = "The dimensions of the discrete fuzzy numbers and the discrete aggregation "
                                      "functions must match. "):
        super().__init__(message)
