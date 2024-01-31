
def get_second_element(item):
    return item [1]
def profit_loss_insights(
        file_name: str,
        output_file_path:str,
):
    with open(file_name, 'r') as file:
        data_list = []
        next (file)
        for line in file:
            data = line.strip().split(",")
            data_list.append(data)
    value_list = [int (parts[4]) for parts in data_list]
    with open (output_file_path, "a") as output_file:
        if sorted(value_list, reverse= False) == value_list:
            max_increase = None
            for i in range(1, len(value_list)):
                increase= value_list[i] - value_list[i-1]
        # caluculate the difference between everyday value 
                if max_increase is None or increase > max_increase:
                    max_increase = increase 
                output_file.write ("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n")
                output_file.write (f"[HIGHEST NET PROFIT SURPLUS] DAY: {data_list[i][0]}, Amount: SGD{max_increase}\n")
        #analyze net profit data and keeps track of the highest increase in net profit 
        #contains information about the net profit surplus to an output file, including the day with the highest surplus and the corresponding amount
        


    