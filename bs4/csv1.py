import csv

#https://docs.python.org/3/library/csv.html

#csvFile = open('test.csv', 'w+')
#try:
#    writer = csv.writer(csvFile)
#    writer.writerow(('number', 'number plus 2', 'number times 2'))
#    for i in range(10):
#        writer.writerow( (i, i+2, i*2))
        
#finally:
#    csvFile.close()

with open('datacsv/test.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter = '-')
    writer.writerow(('number', 'number plus 2', 'number times 2'))
    for i in range(10):
        writer.writerow( (i, i+2, i*2))


#with open('test.csv', 'w', newline='') as csvfile:
#    spamwriter = csv.writer(csvfile, delimiter=' ',
#                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
#    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

#with open('test.csv', 'r') as csvfile:
#    reader = csv.reader(csvfile)

#with open('mew_test.csv', 'w') as newcsvf:
#    writer = csv.writer(newcsvf, delimiter = '-')
#    for line in reader:
#        writer.writerow(line)

    #next(reader)
    #for line in reader:
    #    print(line)