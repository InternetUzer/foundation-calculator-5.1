import json
import os

PROJECTS_DIR = 'projects'

def save_design(name, params, results):
    design_id = str(len(os.listdir(PROJECTS_DIR)) + 1)
    design_data = {
        'id': design_id,
        'name': name,
        'params': params,
        'results': results
    }
    os.makedirs(PROJECTS_DIR, exist_ok=True)
    with open(os.path.join(PROJECTS_DIR, f"{design_id}.json"), 'w') as f:
        json.dump(design_data, f)
    return design_id

def get_all_designs():
    designs = []
    for filename in os.listdir(PROJECTS_DIR):
        if filename.endswith(".json"):
            with open(os.path.join(PROJECTS_DIR, filename), 'r') as f:
                designs.append(json.load(f))
    return designs

def get_design_by_id(design_id):
    try:
        with open(os.path.join(PROJECTS_DIR, f"{design_id}.json"), 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def delete_design(design_id):
    os.remove(os.path.join(PROJECTS_DIR, f"{design_id}.json"))

def get_regional_pricing():
    # Here you can return mock data or connect to a pricing API
    return [{"region_name": "Region 1"}, {"region_name": "Region 2"}]

def get_pricing_by_region(region_name):
    return {
        'concrete_price': 5000.0,
        'steel_price': 55.0,
        'formwork_price': 350.0
    }
