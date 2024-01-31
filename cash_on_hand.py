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
                # [i] is to find the differnece in value inbetween the values within the list
                if max_increase is None or increase > max_increase:
                    max_increase = increase
                    #find the max increase in list.
            output_file.write("[CASH SURPLUS] CASH ON EACH DAY IS HIHGER THAN THE PREVIOUS DAY\n")
            output_file.write(f"[HIGHEST CASH USRPLUS] DAY: {data_list[i][0]}, AMOUNT: SGD{max_increase}\n")
        elif sorted(value_list, reverse=True) == value_list:
                #to check if the values within the value list is sorted in a descending order
                max_decrease_index = None
                max_decrease = None
                # none is used as a variable to define
                for i in range(1, len(value_list)):
                     decrease = value_list[i] - value_list[i - 1]
                     #This line calculates the difference between the current and previous cash surplus values.
                     if max_decrease is None or decrease < max_decrease:
                     #check if previous max or current max is smaller
                          max_decrease = decrease
                          max_decrease_index = i
                output_file.write("[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY\n")
                output_file.write(f"[HIGHEST CASH DEFICIT] DAY: {data_list[max_decrease_index][0]}, AMPUNT: SGD {abs(max_decrease)}\n")
        else:  #if not in descending order.
             decrease = None
             max_decrease = None
             decrease_list = [] #all decrease data will be in this list
             deficit_data = [] 
             deficit_days = set() #days deficit happened
             for i in range(1, len(value_list)):
                  decrease= value_list[i] - value_list[i - 1]
                  if max_decrease is None or decrease< max_decrease:
                       if decrease < 0:
                            decrease_list.append(decrease) #add all decrease values into this list)
                            deficit_days.add(data_list[i][0]) #to get the number of day whr decreased happened
                            deficit_data.append((data_list[i][0], decrease)) #appending the day corresponding deficit values into list
             top_3_deficits = sorted(deficit_data, key=get_second_element)[:3]
             highest_str = ["HIGHEST CASH DEFICT" , "2ND HIGHEST CASH DEFICIT", "3RD HIGHEST CASH DEFICIT"]
             count = 0

             for day, amount in deficit_data:
                  output_file.write(f"\n[{highest_str[count]}]) DAY: {day} , {day}, AMOUNT: SGD{abs(amount)}")
                #output



                                  

