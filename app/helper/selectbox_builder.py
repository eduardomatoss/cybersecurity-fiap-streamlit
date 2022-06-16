def data_selectbox_builder(data : list):

    select_box_data = []

    for detail in data:
        select_box_data.append(f"{detail.get('id')} - {detail.get('name')}")
    
    return select_box_data