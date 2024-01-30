def find_highest_overhead(
    file: str,
    output_file_path: str,
#to indicate where it should write its results    
):
    extracted_data =  []
    with open (".csv_reports/overheads-day-90.csv", "r") as file:
        next (file)
        for line in file:
            parts = [part.strip() for part in line.split(",")]
            category, overhead = parts[0][1:-1], float(parts[1])
            extracted_data.append([category, overhead])
#create a list to add to "extracted_data"                     