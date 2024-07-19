import csv
import pandas as pd

def read_csv(file_path):
    return pd.read_csv(file_path)

def allocate_rooms(groups, hostels):
    allocation = []
    group_rooms = {}

    for index, group in groups.iterrows():
        group_id = group['Group ID']
        members = group['Members']
        gender = group['Gender']
        
        if group_id not in group_rooms:
            group_rooms[group_id] = []
        
        allocated = False
        for index, hostel in hostels.iterrows():
            if hostel['Capacity'] >= members and hostel['Gender'].lower() == gender.lower():
                group_rooms[group_id].append({
                    'Hostel Name': hostel['Hostel Name'],
                    'Room Number': hostel['Room Number'],
                    'Members Allocated': members
                })
                hostels.at[index, 'Capacity'] -= members
                allocated = True
                break
        
        if not allocated:
            raise Exception(f"Unable to allocate room for Group ID {group_id}")

    for group_id, rooms in group_rooms.items():
        for room in rooms:
            allocation.append({
                'Group ID': group_id,
                **room
            })

    return allocation

def save_allocation_to_csv(allocation, file_path):
    keys = allocation[0].keys()
    with open(file_path, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(allocation)
