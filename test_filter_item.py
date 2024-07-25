import pytest

from filter_item import filter_items  # Import the function from the appropriate module

def test_filter_items():
    items = [
        {"name": "item1", "value": 10},
        {"name": "item2", "value": 5},
        {"name": "item3", "value": 15},
        {"name": "item4", "value": 3}
    ]
    key = "value"
    threshold = 7
    
    expected_output = [
        {"name": "item1", "value": 10},
        {"name": "item3", "value": 15}
    ]
    
    result = filter_items(items, key, threshold)
    assert result == expected_output

def test_filter_items_empty_list():
    items = []
    key = "value"
    threshold = 7
    
    expected_output = []
    
    result = filter_items(items, key, threshold)
    assert result == expected_output

def test_filter_items_no_items_above_threshold():
    items = [
        {"name": "item1", "value": 1},
        {"name": "item2", "value": 2},
        {"name": "item3", "value": 3}
    ]
    key = "value"
    threshold = 5
    
    expected_output = []
    
    result = filter_items(items, key, threshold)
    assert result == expected_output

def test_filter_items_missing_key():
    items = [
        {"name": "item1", "value": 10},
        {"name": "item2", "other_value": 20},
        {"name": "item3", "value": 15}
    ]
    key = "value"
    threshold = 7
    
    expected_output = [
        {"name": "item1", "value": 10},
        {"name": "item3", "value": 15}
    ]
    
    result = filter_items(items, key, threshold)
    assert result == expected_output
