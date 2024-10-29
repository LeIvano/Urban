def calculate_structure_sum(args):
    summary = 0
    if isinstance(args, (list,tuple,set)):
        for item in args:
            summary += calculate_structure_sum(item)
    elif isinstance(args, dict):
        for key,value in args.items():
            summary += calculate_structure_sum(key)
            summary += calculate_structure_sum(value)
    elif isinstance(args, int):
        return int(args)
    elif isinstance(args, str):
        return len(args)
    else:
        print(f'Unknown class: {type(args)}')
        exit()
    return summary



data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)