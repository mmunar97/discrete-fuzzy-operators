class DiscreteFuzzyNumberMembershipOutOfBounds(Exception):
    """
    An Exception which indicates that the membership values entered are not between 0 and 1.
    """

    def __init__(self, message: str = "The membership functions of the labels as well as the alpha-cuts thresholds "
                                      "must be between 0 and 1."):
        super().__init__(message)
