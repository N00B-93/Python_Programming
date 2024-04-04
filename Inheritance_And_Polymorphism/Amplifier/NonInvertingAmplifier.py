from Amplifier import Amplifier


class NonInvertingAmplifier(Amplifier):
    """
    A class representing a Non Inverting Amplifier.

    Attributes:
        vo: (float) The output voltage.

        vi: (float) The input voltage.

        R1: (float) The first resistance.

        R2: (float) The second resistance.
    """
    def __init__(self, vo, vi, R1, R2):
        super().__init__(vo, vi)
        self.R1 = R1
        self.R2 = R2

    def getDescription(self):
        """
        This returns a String identifying the Non Inverting Amplifier.

        :return: (str) A String identifying the Non Inverting Amplifier.
        """
        return "Type: Non Inverting Amplifier"

    def getGain(self):
        """
        This returns the gain of the Non Inverting Amplifier.

        :return: (float) The gain of the Non Inverting Amplifier.
        """
        return 1 + (self.R2 / self.R1)
