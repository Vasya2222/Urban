data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def counting_all_numbers_and_strings(data) -> int:
    all_data = list()
    
    for items in data:
        if isinstance(items, (list, set, tuple)):
            all_data.extend(counting_all_numbers_and_strings(items))
        elif isinstance(items, (str, int)):
            all_data.append(items)
        elif isinstance(items, dict):
            for key, value in items.items():
                all_data.append(key)
                all_data.append(value)
    
    return [sum([i if isinstance(i, int) else len(i) for i in all_data ])]

print(*counting_all_numbers_and_strings(data_structure))