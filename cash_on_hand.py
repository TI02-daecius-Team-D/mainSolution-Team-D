def get_second_element (item):
    return item [1]
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
            output_file.write("[CASH SURPLUS] CASH ON EACH DAY IS HIHGER THAN THE PREVIOUS DAY\n")
            output_file.write(f"[HIGHEST CASH USRPLUS] DAY: {data_list[i][0]}, AMOUNT: SGD{max_increase}\n")
        elif sorted(value_list, reverse=True) == value_list
                max_decrease_index = None
                max_decrease = None
                for i in range(1, len(value_list)):
                     decrease = value_list[i] - value_list[i - 1]
                     #This line calculates the difference between the current and previous cash surplus values.
                     if max_decrease is None or decrease < max_decrease:
                     #check if previous max or current max is smaller
                          max_decrease = decrease
                          max_decrease_index = i
                output_file.write("[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY\n")
                output_file.write(f"[HIGHEST CASH DEFICIT] DAY: {data_list[max_decrease_index][0]}, AMPUNT: SGD {abs(max_decrease)}\n")
                
                                  

