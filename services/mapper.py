class Mapper:
    def _mapper(self, item):
        word, count = item
        result = [(word, 1)]

        return result

    def run(self, data):
        intermediate_data = []
        for item in data:
            intermediate_data.extend(self._mapper(item))

        return intermediate_data