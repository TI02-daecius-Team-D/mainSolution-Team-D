def get_second_element(item):
    return item [1]
def find_highest_overhead(
    file: str,
    output_file_path: str,
#to indicate where it should write its results    
):
    extracted_data =  []
    with open (".csv_reports/overheads-day-90.csv", "r") as file:
        next (file)
        for line in file:
             line_parts = line.split(",") 
        parts = [] 
        for part in line_parts: 
                parts.append(part.strip()) 
        category, overhead = parts[0][1:-1], float(parts[1])
        extracted_data.append([category, overhead])
    max_cat, max_float_value = max(extracted_data, key = get_second_element)
    result = (f"[HIGHEST OVERHEAD] {max_cat}: {max_float_value}")
    with open(output_file_path, 'w') as output_file:
        output_file.write(str(result))
                           

