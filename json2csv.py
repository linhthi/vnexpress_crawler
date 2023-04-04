import json
import csv

categories = ['giao-duc', 'khoa-hoc', 'the-thao', 'kinh-doanh', 'suc-khoe', 'the-gioi', 
'giai-tri', 'du-lich', 'so-hoa', 'thoi-su', 'phap-luat']

for item in categories:
    # Open the JSON file and load its contents
    with open('./dataset_vnexpress/{0}.json'.format(item), "r") as json_file:
        data = json.load(json_file)

    # Open the CSV file for writing
    with open('./dataset_vnexpress_csv/{0}.csv'.format(item), "w", newline='') as csv_file:
        # Create a CSV writer
        writer = csv.writer(csv_file)

        # Write the header row
        writer.writerow(data[0].keys())

        # Write the data rows
        for row in data:
            writer.writerow(row.values())





