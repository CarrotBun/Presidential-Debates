import csv

with open('debate.csv', 'rt') as f, open('text.csv', 'wt') as g:
    reader = csv.reader(f)
    writer = csv.writer(g)
    for i, speaker, text, time in reader:
        row = text.split(' ')
        row.insert(0, speaker)
        writer.writerow(row)


