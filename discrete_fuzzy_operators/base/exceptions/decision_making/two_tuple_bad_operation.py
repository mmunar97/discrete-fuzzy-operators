class TwoTupleBadOperation(Exception):
    """
    An Exception which indicates that the operation between two 2-tuples is bad defined due to missing parameters.
    """

    def __init__(self, message: str = "The operation being attempted is not well defined. Check the parameter limits "
                                      "and the definition of the operators."):
        super().__init__(message)
