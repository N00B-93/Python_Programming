from Inheritance_And_Polymorphism.ResonantCircuit.ResonantCircuit import ResonantCircuit


class ParallelResonantCircuit(ResonantCircuit):
    """
    A class representing a parallel resonant circuit.

    Attributes:
        w0 (float): The resonant frequency.

        k (float): The gain at Resonant Frequency.

        B (float): The band width.

        R (float): The resistance of the circuit.

        L (float): The inductance of the circuit.

        C (float): The capacitance of the circuit.
    """
    def __int__(self, w0, k, B):
        super.__init__(w0, k, B)

    def designCircuit(self):
        """
        This determines the values of the resistance, inductance and the capacitance to attain the resonant frequency.

        :return: (tuple) A tuple containing the resistance, capacitance and inductance of the parallel resonant circuit.
        """
        R = self.getGainAtResonance()

        C = 1 / (self.getResonantFrequency() * R)

        L = 1 / (pow(self.getResonantFrequency(), 2) * C)

        return R, L, C

    def display(self):
        """
        This displays the parameters of the parallel resonant circuit.

        :return: None
        """
        print("\n\t\tParallel Resonant Circuit:")

        super().display()

        R, L, C = self.designCircuit()

        print(f"Resistance: {R:.4e} Ohms\nInductance: {L:.4e} H\nCapacitance: {C:.4e} C")
