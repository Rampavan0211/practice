def filter_items(items, key, threshold):
    """
    Filters a list of dictionaries to only include items where the value of a specific key is above a given threshold.
    
    Args:
        items (list of dict): The list of dictionaries to filter.
        key (str): The key to check the value of.
        threshold (int or float): The threshold value.
    
    Returns:
        list of dict: The filtered list of dictionaries.
    """
    return [item for item in items if item.get(key, 0) > threshold]
