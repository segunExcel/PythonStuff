# Return Sublist from either dict or list
def return_sublist_total_from_either_dictionary_or_2D_list(data_table: list | dict, key: str) -> float | None:
    sublist = return_sublist_from_either_dictionary_or_2D_list(data_table, key)
    if sublist is None:  # If key not found
        return None

    sublist_total = 0
    for item in sublist:
        try:
            sublist_total += float(item)  # Convert to float and add
        except ValueError:
            return None  # Return None if any value can't be converted to a number

    return sublist_total

# Sublist Total
def return_sublist_total_from_either_dictionary_or_2D_list(data_table: list | dict, key: str) -> float | None:
    sublist = return_sublist_from_either_dictionary_or_2D_list(data_table, key)
    if sublist is None:  # If key not found
        return None

    sublist_total = 0
    for item in sublist:
        try:
            sublist_total += float(item)  # Convert to float and add
        except ValueError:
            return None  # Return None if any value can't be converted to a number

    return sublist_total

# Sublist Mean
def return_sublist_mean_from_either_dictionary_or_2D_list(data_table: list | dict, key: str) -> float | None:
    sublist = return_sublist_from_either_dictionary_or_2D_list(data_table, key)
    if sublist is None or len(sublist) == 0:  # If key not found or sublist is empty
        return None

    total = 0
    count = 0
    for item in sublist:
        try:
            total += float(item)
            count += 1
        except ValueError:
            return None  # Return None if any value can't be converted to a number

        sublist_mean = total / count

    return sublist_mean  # Calculate mean

# Sublist Median
def return_sublist_median_from_either_dictionary_or_2D_list(data_table: list | dict, key: str) -> float | None:
    sublist = return_sublist_from_either_dictionary_or_2D_list(data_table, key)
    if sublist is None or len(sublist) == 0:  # If key not found or sublist is empty
        return None

    try:
        numeric_values = sorted(float(item) for item in sublist)  # Convert to float and sort
    except ValueError:
        return None  # Return None if any value can't be converted to a number

    length = len(numeric_values)
    mid = length // 2

    if length % 2 == 1:  # Odd number of elements
        return numeric_values[mid]
    else:  # Even number of elements
        return (numeric_values[mid - 1] + numeric_values[mid]) / 2

# Total Value From Dictionary or list
def return_total_value_from_either_dictionary_or_2D_list(data_table: list | dict) -> float | None:
    total = 0
    if isinstance(data_table, dict):
        for key in data_table:
            total = return_sublist_total_from_either_dictionary_or_2D_list(data_table, key)
            if total is None:
                return None  # If any sublist can't be processed
            total += total
    elif isinstance(data_table, list):
        for sublist in data_table:
            if len(sublist) > 0:
                key = sublist[0]
                sublist_total = return_sublist_total_from_either_dictionary_or_2D_list(data_table, key)
                if sublist_total is None:
                    return None
                total += sublist_total
    else:
        return None  # Invalid data structure

    return total
