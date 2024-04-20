# Sample data
data = [
    ("apple", 1),
    ("banana", 1),
    ("apple", 1),
    ("banana", 1),
    ("apple", 1),
    ("banana", 1),
    ("apple", 1),
]

# Map function
def mapper(item):
    word, count = item
    result = [(word, 1)]
    return result

# Map phase
intermediate_data = []
for item in data:
    intermediate_data.extend(mapper(item))
print("mapper result ", intermediate_data)

# Reduce function
def reducer(key, values):
    return key, sum(values)

# Shuffle and Sort
sorted_intermediate_data = sorted(intermediate_data, key=lambda x: x[0])
print("Sorted result  : ", sorted_intermediate_data)

# Reduce phase
final_output = {}
for word, count in intermediate_data:
    if word not in final_output:
        final_output[word] = []
    final_output[word].append(count)
print("reducer result : ", final_output)

result = [(key, reducer(key, values)) for key, values in final_output.items()]
print(result)
