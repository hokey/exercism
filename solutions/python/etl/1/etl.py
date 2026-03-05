def transform(legacy_data):
    new_data = {}
    for point in legacy_data.keys():
        for letter in legacy_data[point]:
            new_data[letter.lower()] = point
    return new_data
