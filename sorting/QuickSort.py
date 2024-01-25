import random
import sys

sys.setrecursionlimit(10 ** 7)


class QuickSort:

    def sort_data(self, data):
        if len(data) <= 1:
            return data
        indexes = random.sample(range(len(data)), min(3, len(data)))
        values = [data[i] for i in indexes]
        pivot_value = sorted(values)[1]

        left_array, right_array = self.recursive_method(data, pivot_value)
        return self.sort_data(left_array) + [pivot_value] * data.count(
            pivot_value) + self.sort_data(right_array)

    def recursive_method(self, data, pivot_value):
        left_array = []
        right_array = []
        for i in range(len(data)):
            if data[i] < pivot_value:
                left_array.append(data[i])
            elif data[i] > pivot_value:
                right_array.append(data[i])
        return left_array, right_array

