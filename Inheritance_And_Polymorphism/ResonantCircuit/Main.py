from ParallelResonantCircuit import ParallelResonantCircuit
from SeriesResonantCircuit import SeriesResonantCircuit

"""
    This is a program that creates an Object of the ParallelResonantCircuit class and an Object of the
    SeriesResonantCircuit class, and then displays the parameters of each Object.
"""


def main() -> None:
    # Create a Parallel Resonant Circuit
    parallelCircuit = ParallelResonantCircuit(1000, 200, 10)

    # Create a Series Resonant Circuit
    seriesCircuit = SeriesResonantCircuit(1200, 150, 8)

    # Displays the parameters of each Circuit.
    parallelCircuit.display()
    print()
    seriesCircuit.display()


if __name__ == "__main__":
    main()
