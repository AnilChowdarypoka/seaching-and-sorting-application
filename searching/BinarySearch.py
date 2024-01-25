class BinarySearch:

    def __init__(self, data):
        self.data = data

    def search_element(self, element):
        low, mid = 0, 0
        high = len(self.data) - 1

        while low <= high:
            mid = (high + low) // 2

            if self.data[mid] < element:
                low = mid + 1

            elif self.data[mid] > element:
                high = mid - 1

            else:
                return True

        return False

