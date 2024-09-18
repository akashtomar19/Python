from collections import defaultdict

# Create a nested defaultdict directly
main_dict = defaultdict(lambda: defaultdict(dict))

# Example usage with tuple keys derived from sets
key_set = {'a', 'b', 'c'}

tuple_key = tuple(sorted(key_set))  # Convert set to tuple (sorted to ensure consistency)

# Adding data directly to the nested dictionary
main_dict[tuple_key]['inner_key1']['sub_key1'] = 'value1'
main_dict[tuple_key]['inner_key2']['sub_key2'] = 'value2'

# Accessing the data
print(main_dict[tuple_key]['inner_key1'])  # Output: {'sub_key1': 'value1'}
print(main_dict[tuple_key]['inner_key2'])  # Output: {'sub_key2': 'value2'}
