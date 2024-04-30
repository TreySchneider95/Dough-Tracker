import csv

def get_dd():
    try:
        with open('dd.csv', "r+", newline='') as f:
            reader = csv.reader(f)
            data = list(reader)[0]
        return data
    except Exception as e:
        print(e)

def write_dd(data):
    with open('dd.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)



