from VoltageDividerAmplifier import VoltageDividerAmplifier
from InvertingAmplifier import InvertingAmplifier
from NonInvertingAmplifier import NonInvertingAmplifier

"""
    This is a program that creates Objects of an InvertingAmplifier class, a NonInvertingAmplifier class, and a
    VoltageDividerAmplifier class, and then adds them to a list and then displays their description and their gains 
    respectively.
"""


def main() -> None:
    # Creates an Object of an InvertingAmplifier.
    invertingAmplifier = InvertingAmplifier(12.2, 17.6, 20, 44.6)

    # Creates an Object of an NonInvertingAmplifier.
    nonInvertingAmplifier = NonInvertingAmplifier(25.0, 16.4, 40.5, 52.13)

    # Creates an Object of an VoltageDividerAmplifier.
    voltageDividerAmplifier = VoltageDividerAmplifier(21.0, 10.5, 56.2, 28.1)

    # Creates an empty list and add the Amplifiers to it.
    amplifiers = [invertingAmplifier, nonInvertingAmplifier, voltageDividerAmplifier]

    # Displays the type and the gain of each amplifier in the amplifier list.
    for amplifier in amplifiers:
        print(amplifier.getDescription())
        print(f"Gain: {amplifier.getGain():.2f}\n")


if __name__ == "__main__":
    main()
