from random import random


def fisher_yates_shuffle(arr):
    for i in range(len(arr) - 1, 0, -1):
        # Generate a random index between 0 and i (inclusive)
        j = random.randint(0, i)

        # Swap the elements at positions i and j
        arr[i], arr[j] = arr[j], arr[i]


# Example usage
my_list = [1, 2, 3, 4, 5]
fisher_yates_shuffle(my_list)
print(my_list)  # The elements of my_list are now shuffled randomly.