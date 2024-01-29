def cash_on_hand_insights(file_name: str, output_file_path: str):
    with open(file_name, "r") as file:
        next(file)
        data_list = [line.strip().split(",") for line in file]
    value_list = [int(parts[1]) for parts in data_list]
    #read from file into the list.
    
    with open(output_file_path, "a") as output_file:
        if sorted(value_list, reverse=False) == value_list:
            max_increase = None
            for i in range(1, len(value_list)):
                increase = value_list[i] - value_list[i - 1]
                if max_increase is None or increase > max_increase:
                    max_increase = increase
                    #find the max increase in list.