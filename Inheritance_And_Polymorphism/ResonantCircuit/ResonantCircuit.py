class ResonantCircuit:
    """
    A class representing Resonant Circuits.

    Attributes:
        w0 (float): The resonant frequency.

        k (float): The gain at Resonant Frequency.

        B (float): The band width.
    """
    def __init__(self, w0, k, B):
        self._w0 = w0
        self._k = k
        self._B = B

    def getResonantFrequency(self):
        """
        This returns the resonant frequency of the resonant circuit.

        :return: (float) The resonant frequency.
        """
        return self._w0

    def setResonantFrequency(self, w0):
        """
        This sets the resonant frequency of the circuit to the given value.

        :param w0: (float) The resonant frequency.

        :return: None.
        """
        self._w0 = w0

    def getGainAtResonance(self):
        """
        This returns the gain at the resonant frequency.

        :return: (float) The gain at the resonant frequency.
        """
        return self._k

    def setGainAtResonance(self, k):
        """
        This set the gain at the resonant frequency to the given value.

        :param k: (float) The gain at the resonance frequency.

        :return: None.
        """
        self._k = k

    def getBandWidth(self):
        """
        The returns the bandwidth of the resonant circuit.

        :return: (float) The bandwidth of the resonant circuit.
        """
        return self._B

    def setBandWidth(self, B):
        """
        This sets the bandwidth of the resonant circuit to the given value.

        :param B: (float) The bandwidth of the resonant circuit.

        :return: None
        """
        self._B = B

    def display(self):
        """
        This displays the resonant circuit's resonant frequency, gain at resonance and the bandwidth.

        :return: None
        """
        print(f"Resonant Frequency: {self._w0: .2f}\nGain At Resonance: {self._k: .2f}\nBandWidth: {self._B: .2f}")
