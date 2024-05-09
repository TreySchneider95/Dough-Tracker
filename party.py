import csv
import pandas as pd

def read_parties():
    parties = []
    with open('party.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        for row in reader:
            if not row:
                continue
            if len(row) != 3:
                continue
            party_name, dough_name, quantity = row
            party_exists = False
            for party in parties:
                if party['party_name'] == party_name:
                    party_exists = True
                    party['doughs'].append({'name': dough_name, 'quantity': quantity})
                    break
            if not party_exists:
                parties.append({'party_name': party_name, 'doughs': [{'name': dough_name, 'quantity': quantity}]})
    return parties

def write_party(data):
    with open('party.csv', 'a+', newline='') as csvfile:
        doughs = data.pop('doughs', [])  # Extract doughs from data
        writer = csv.DictWriter(csvfile, fieldnames=data.keys())
        if csvfile.tell() == 0:
            writer.writeheader()
        writer.writerow(data)
        dough_writer = csv.DictWriter(csvfile, fieldnames=['party_name', 'dough_name', 'quantity'])
        for dough in doughs:
            dough_writer.writerow({'party_name': data['party_name'], 'dough_name': dough['name'], 'quantity': dough['quantity']})

def write_party_to_excel(party_name, party_data):
    filename = f"{party_name}.xlsx"
    df = pd.DataFrame(party_data)
    df.to_excel(filename, index=False)
    return filename

def remove_party(party_name):
    parties = read_parties()
    filtered_parties = [party for party in parties if party['party_name'] != party_name]
    the_party = [party for party in parties if party['party_name'] == party_name][0]
    print(filtered_parties)
    f = open('party.csv', "w+")
    f.close()
    for x in filtered_parties:
        write_party(x)




