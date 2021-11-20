import csv

data = []

with open("cleaned_star_data.csv", 'r') as f:
    csv_reader = csv.reader(f)

    for i in csv_reader:
        data.append(i)

headers = data[0]
star_data = data[1:]

for i in star_data:
    i[0] = i[0].lower()

star_data.sort(key = lambda star_data:star_data[1])

with open("merged_data_sorted.csv", "a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(star_data)
