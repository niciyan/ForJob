import sys
import csv
if len(sys.argv) < 3:
    print("Usage: csvToTable.py csv_file html_file")
    exit(1)

reader = csv.reader(open(sys.argv[1]))
htmlfile = open(sys.argv[2],"w")

htmlfile.write('<link rel="stylesheet" href="bootstrap.min.css">')

htmlfile.write('<div class="container">')
htmlfile.write('<h1 class="text-primary">' + sys.argv[1] + '</h1>')

rownum = 0
htmlfile.write('<table class="table">')
for row in reader:
    if rownum == 0:
        htmlfile.write('<tr class="bg-warning">')
        for column in row:
            htmlfile.write('<th>' + column + '</th>')
        htmlfile.write('</tr>')
    else:
        htmlfile.write('<tr>')
        for column in row:
            htmlfile.write('<td>' + column + '</td>')
        htmlfile.write('</tr>')

htmlfile.write('</div>')
        

