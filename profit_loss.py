def write_to_txt(output_file_path: str, result: str):
    with open(output_file_path, 'w') as output_file:
        output_file.write(str(result))
#converting it to string 

def profit_loss_insights(
        file_name: str,
        output_file_path:str,
):
    with open(file_name, 'r') as file:
        next (file)
        data_list = [line.strip().split(',') for line in file ]
    value_list = [int (parts[4]) for parts in data_list]
    with open (output_file_path, "a") as output_file:
        if sorted(value_list, reverse= False) == value_list:
            max_increase = None
            for i in range(1, len(value_list)):
                increase= value_list[i] - value_list[i-1]
    # caluculate the difference between everyday value 

    