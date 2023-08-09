# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"Eu84100","system":"readv2"},{"code":"110478.0","system":"med"},{"code":"1276.0","system":"med"},{"code":"22098.0","system":"med"},{"code":"24044.0","system":"med"},{"code":"2950.0","system":"med"},{"code":"34174.0","system":"med"},{"code":"3637.0","system":"med"},{"code":"36662.0","system":"med"},{"code":"42941.0","system":"med"},{"code":"43444.0","system":"med"},{"code":"50337.0","system":"med"},{"code":"51375.0","system":"med"},{"code":"63251.0","system":"med"},{"code":"69016.0","system":"med"},{"code":"7302.0","system":"med"},{"code":"9982.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('autism-and-asperger's-syndrome-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["autism-and-asperger's-syndrome---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["autism-and-asperger's-syndrome---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["autism-and-asperger's-syndrome---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
