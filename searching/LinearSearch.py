class LinearSearch:

    def __init__(self, data):
        self.data = data

    def search_element(self, element):
        for i in self.data:
            if i == element:
                return True
        return False


