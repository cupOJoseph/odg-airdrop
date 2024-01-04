import csv

# Input and output file paths
input_csv_path = 'input.csv'
output_csv_path = 'output.csv'

# Dictionary to store points for each unique id
points_dict = {}

# Read the input CSV file
with open(input_csv_path, 'r') as input_file:
    reader = csv.reader(input_file)
    
    # Loop through each row in the CSV
    for row in reader:
        # Extract id and points from the row
        unique_id, points = row[0], int(row[1])
        
        # Aggregate points for each unique id
        if unique_id in points_dict:
            points_dict[unique_id] += points
        else:
            points_dict[unique_id] = points

# Write the aggregated data to a new CSV file
with open(output_csv_path, 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    
    # Write header
    writer.writerow(['id', 'points'])
    
    # Write aggregated data
    for unique_id, total_points in points_dict.items():
        writer.writerow([unique_id, total_points])

print(f"Aggregated data saved to {output_csv_path}")
