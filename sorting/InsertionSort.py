
class InsertionSort:

    def sort_data(self, data):
        for i in range(1, len(data)):
            current_value = data[i]
            iterator = i - 1
            while iterator >= 0 and current_value < data[iterator]:
                data[iterator + 1] = data[iterator]
                iterator = iterator - 1
            data[iterator + 1] = current_value
        return data





