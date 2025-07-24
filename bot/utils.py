import re

def extract_item_ids(item_list):
    return [int(''.join(re.findall(r'\d+', item['ItemLink']))) for item in item_list]

def item_names(item_list):
    return ', '.join(item['Name'] for item in item_list)

def calculate_total_value(item_ids, value_data):
    return sum(value_data[str(i)][0] for i in item_ids if str(i) in value_data)
