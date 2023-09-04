def combination(items, max_weight):
    possible_items = []
    for item, weight in items.items():
        if weight <= max_weight:
            possible_items.append(item)
            max_weight -= weight
    return possible_items

items = {"вилка": 10,
         "ложка": 10,
         "вода": 3000,
         "ботинки": 1500,
         "куртка": 500,
         "чайник": 300,
         "палатка": 3000,
         "еда": 2000,
         "штаны": 400,
         "кружка": 26,
         }

max_weight = 1280
print(combination(items, max_weight))