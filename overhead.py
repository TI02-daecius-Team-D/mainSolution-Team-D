def get_second_element(item): #to get the second element (which is overhead)
    return item [1]
def find_highest_overhead(
    file_name: str,
    output_file_path: str,
#to indicate where it should reas and write for output  
):
    extracted_data =  [] #store items into list (in this case its the overhead)
    with open (file_name, "r") as file: #r = read. 
        next (file)
        for line in file: #loops the lines in a file
             line_parts = line.split(",") #split data into 2 parts (split cat and overhead)
             parts = [] # store content from the file after splitting the data (ref: line 12)
             for part in line_parts: # loops the line part
                     parts.append(part.strip()) #format the data from csv file so easier to extract highest overhead value in cat 
             category, overhead = parts[0][1:-1], float(parts[1])
             extracted_data.append([category, overhead])
        max_cat, max_float_value = max(extracted_data) #max is to take out the different cat's max value
        #write in the summary report txt
        result = (f"[HIGHEST OVERHEAD] {max_cat}: {max_float_value}")
        with open(output_file_path, 'w') as output_file: #use "W" to write instead of "a" so we will not regenerate the same thing
             output_file.write(str(result))
                           

