"""
    This is a program that prompts the user to enter the radii of curvature R1 and R2 of a lens and the thickness d, of
    the lens and then calculates and displays the focal length f, of the lens using the relation;
                    (1 / f) = (n - 1)[(1 / R1) - (1 / R2) + ((n - 1)d) / nR1R2)]
"""


def getFocalLength(refractiveIndex: float, r1: float, r2: float, thickness: float) -> float:
    """
    This returns the focal length of a lens.

    :param refractiveIndex: (float) The refractive index of the lens.

    :param r1: (float) The radius of curvature of the first face of the lens.

    :param r2: (float) The radius of curvature of the second face of the lens.

    :param thickness: (float) The thickness of the lens.

    :return: (float) The focal length of the lens.
    """
    inverseFocalLength: float = (refractiveIndex - 1) * ((1 / r1) - (1 / r2) + (refractiveIndex - 1) *
                                                         thickness / (refractiveIndex * r1 * r2))

    return 1 / inverseFocalLength


def main() -> None:
    # Reads in the refractive index of the lens.
    refractiveIndex = float(input("\nEnter the refractive index, n of the lens(0 < n <= 4.05): "))

    # Displays an error message and terminates the program if lens refractive index is negative.
    if refractiveIndex < 0:
        print("\nRefractive index cannot be < 0!")
        exit(1)

    # Reads in the radius of curvature of the first face of the lens.
    r1 = float(input("\nEnter the radius of curvature of the first face of the lens in cm: "))

    # Reads in the radius of curvature of the second face of the lens.
    r2 = float(input("\nEnter the radius of curvature of the second face of the lens in cm: "))

    # Reads in the thickness of the lens.
    thicknessOfLens = float(input("\nEnter the thickness of the lens in cm: "))

    # Displays an error message and terminates the program if lens thickness is negative.
    if thicknessOfLens < 0:
        print("\nThickness cannot be < 0!")
        exit(1)

    # determines the focal length of the lens.
    focalLength: float = getFocalLength(refractiveIndex, r1, r2, thicknessOfLens)

    # Displays the focal length of the lens.
    print(f"\nThe focal length of the lens is: {focalLength:.2f}cm")


if __name__ == "__main__":
    main()
