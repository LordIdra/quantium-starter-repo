import csv
from this import d

paths_in = ["data/daily_sales_data_0.csv", "data/daily_sales_data_1.csv", "data/daily_sales_data_2.csv"]


def filter_pink(data_in):
    data_out = []
    for row in data_in:
        if row[0][0:4] == "pink":
            data_out.append(row)
    return data_out


def remove_first_column(data_in):
    data_out = []
    for row in data_in:
        data_out.append([row[1], row[2], row[3], row[4]])
    return data_out


def merge_to_sales(data_in):
    data_out = []
    for row in data_in:
        price = float(row[0][1:len(row[0])])
        quantity = float(row[1])
        sales = price * quantity
        data_out.append([str(sales), row[2], row[3]])
    return data_out


def read_and_filter(file):
    data = csv.reader(file, delimiter=',')
    data = filter_pink(data)
    data = remove_first_column(data)
    return merge_to_sales(data)


def write_output(path, data):
    with open(path, mode='w') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(data)


final_data = []

for path in paths_in:
    with open(path, newline='') as file:
        final_data += read_and_filter(file)

write_output("data.csv", final_data)