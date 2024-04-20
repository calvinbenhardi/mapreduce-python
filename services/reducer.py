class Reducer:
    def _reducer(self, key, values):
        return key, sum(values)

    def _shuffle_and_short(self, data):
        return sorted(data, key=lambda x: x[0])

    def run(self, data):
        sorted_data = self._shuffle_and_short(data)
        print(sorted_data)
        output = {}
        for word, count in sorted_data:
            if word not in output:
                output[word] = []

            output[word].append(count)

        return [(key, self._reducer(key, values)) for key, values in output.items()]
