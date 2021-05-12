class FuzzyOperatorBadDefinition(Exception):
    """
    An Exception which indicates that the operator is bad defined due to missing parameters.
    """

    def __init__(self, message: str = "To define the operator, its matrix expression or its analytical expression in "
                                      "callable function format must be provided."):
        super().__init__(message)