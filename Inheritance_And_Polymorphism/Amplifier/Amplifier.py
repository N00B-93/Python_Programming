class Amplifier:
    """
    A class representing an Amplifier.

    Attributes:
        vo: (float) The output voltage.

        vi: (float) The input voltage.
    """
    def __init__(self, vo, vi):
        self.vo = vo
        self.vi = vi

    @property
    def getGain(self):
        raise NotImplementedError("This method should be Overridden in the sub class.")

    @property
    def getDescription(self):
        """
        This returns a String identifying the Amplifier.

        :return: (str) A String identifying the Amplifier.
        """
        return "\nType: Amplifier"
