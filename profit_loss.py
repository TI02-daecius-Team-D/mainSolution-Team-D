
def get_second_element(item):
    return item [1]
def profit_loss_insights(
        file_name: str,
        output_file_path:str,
):
#Read data from the input file
    with open(file_name, 'r') as file:  
        data_list = []
        next (file) 
        for line in file:
            data = line.strip().split(",")
            data_list.append(data)
#Extract net profit values and store them in a list
    value_list = [int (parts[4]) for parts in data_list] #to keep the net profit info in value list
#Open the output file in append mode
    with open (output_file_path, "a") as output_file:
#Check if the net profit values are sorted in ascending order
        if sorted(value_list, reverse= False) == value_list:
#Find the highest net profit surplus
            max_increase = None
            for i in range(1, len(value_list)):
                increase= value_list[i] - value_list[i-1] # caluculate/find the difference between everyday value 
        
                if max_increase is None or increase > max_increase:
                    max_increase = increase
#Write the highest net profit surplus information to the output file
                output_file.write ("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n")
                output_file.write (f"[HIGHEST NET PROFIT SURPLUS] DAY: {data_list[i][0]}, Amount: SGD{max_increase}\n")
        #analyze net profit data and keeps track of the highest increase in net profit 
        #contains information about the net profit surplus to an output file, including the day with the highest surplus and the corresponding amount
        elif sorted(value_list, reverse = True) == value_list:
#Find the highest net profit deficit
            max_decrease_index = None
            max_decrease = None
            for i in range(1, len(value_list)):
                decrease = value_list[i] - value_list [i - 1]
                if max_decrease is None or decrease < max_decrease:
                    max_decrease = decrease
                    max_decrease_index = i
 #Write the highest net profit deficit information to the output file
                output_file.write("[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN PREVIOUS DAY\n")
        else:
#Find the top 3 net profit deficits
            decrease = None
            max_decrease = None
            decrease_list = []
            deficit_data = []
            deficit_days = set()
            for i in range(1, len(value_list)):
                decrease = value_list[i]-value_list[i-1] # caluculate/find the difference between everyday value 
                if max_decrease is None or decrease < max_decrease:
                    if decrease < 0:
                        decrease_list.append(decrease)
                        deficit_days.add(data_list[i][0])
                        deficit_data.append((decrease, data_list[i][0]))
            top_3_deficits = sorted(deficit_data, reverse = False)[:3]
            #write in the summary report txt
            highest_str = ["HIGHEST NET PROFIT DEFICIT", "2ND HIGHEST NET PROFIT DEFICIT", "3RD HIGHEST NET PROFIT DEFICIT"]
            count = 0
            for amount, day in deficit_data:
                output_file.write(f"\n[NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD{abs(amount)}") #abs used to make sure the value has a positive output
            for amount, day in top_3_deficits:
                output_file.write(f"\n[{highest_str[count]}]  DAY: {day}, AMOUNT: SGD{abs(amount)}")
                count += 1
                        

        


    