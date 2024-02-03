from time import time


class StopWatch:
    """
    A class representing a stopwatch.

    Attributes:

    startTime (float): The start time of the stopwatch

    endTime (float): The end time of the stopwatch
    """

    def __init__(self, startTime):
        self.__startTime = startTime
        self.__endTime = None

    def start(self):
        """
        Sets the start time of the stopwatch to the current time.

        :return: None.
        """
        self.__startTime = time()

    def stop(self):
        """
        Sets the end time of the stopwatch to the current time.

        :return: None.
        """
        self.__endTime = time()

    def getElapsedTime(self):
        """
        Returns the elapsed time between the start and end time.

        :return: (float) The elapsed time in seconds.
        """
        return self.__endTime - self.__startTime


def main():
    # Creates a StopWatch Object.
    stopwatch = StopWatch(time())

    # Starts the stopwatch.
    stopwatch.start()

    # Counts from 1 to 1000000
    for i in range(1, 1000001):
        pass

    # Stops the stopwatch.
    stopwatch.stop()

    # Displays the result.
    print(f"\nTime taken to count from 1 - 1000000 = {stopwatch.getElapsedTime()}")


if __name__ == "__main__":
    main()
