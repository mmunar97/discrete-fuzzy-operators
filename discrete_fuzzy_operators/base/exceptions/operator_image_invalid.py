class FuzzyOperatorImageRangeException(Exception):
    """
    An Exception which indicates that the associated matrix of the operator has invalid values.
    """

    def __init__(self, message: str = "The introduced matrix contains entries whose values are out of L"):
        super().__init__(message)
