class OwaBadLength(Exception):
    """
    An Exception which indicates that the list of weight has a bad dimension.
    """

    def __init__(self, message: str = "The length of the weight list does not match the length of the 2-tuple set."):
        super().__init__(message)
