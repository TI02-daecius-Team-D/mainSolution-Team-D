def cash_on_hand_insights(file_name: str, output_file_path: str):
    with open(file_name, "r") as file:
        next(file)
        data_list = [line.strip().split(",") for line in file]
    value_list = [int(parts[1]) for parts in data_list]