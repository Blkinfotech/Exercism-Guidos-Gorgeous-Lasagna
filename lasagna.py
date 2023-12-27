"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


# lasagna.py

# Define the 'EXPECTED_BAKE_TIME' constant
EXPECTED_BAKE_TIME = 40  # Update the value to 40

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    remaining_time = EXPECTED_BAKE_TIME - elapsed_bake_time
    return max(0, remaining_time)

def preparation_time_in_minutes(layers):
    """Return the preparation time in minutes.

    :param layers: int - the number of layers.
    :return: int - preparation time in minutes.
    
    Function that returns the total preparation time for making lasagna based on the number of layers.
    """
    # Assuming a simple formula: double the number of layers
    return 2 * layers

def elapsed_time_in_minutes(layers, time):
    """Calculate the elapsed time in minutes.

    :param layers: int - the number of layers.
    :param time: int - baking time already elapsed.
    :return: int - total elapsed time (in minutes).

    Function that takes the actual minutes the lasagna has been in the oven and the number of layers as
    arguments and returns the total elapsed time.
    """
    total_elapsed_time = time + preparation_time_in_minutes(layers)
    return max(0, total_elapsed_time)
