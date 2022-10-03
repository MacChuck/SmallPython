#variable names need reworked. Takes two CSVs of email addresses, searching the 2nd one for usernames from the first one. Outputs a new CSV with the emails from the first list, and any found results from the 2nd list in the same row.

import csv

usernames = []
emails = []

with open("./usernames.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    #un = row[0].split('@')[0]
    #usernames.append(un)
    usernames.append(row[0])

#print(usernames)

with open("./emails.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    emails.append(row[0])

#print(emails)

exportTable = []

for name in usernames:
  exportRow = []
  exportRow.append(name)
  un = name.split('@')[0]
  for email in emails:
    if email.find(un) != -1 and (email != name):
      print(un + " found in " + email)
      exportRow.append(email)
  exportTable.append(exportRow)

headerRow = ["email","subdomain accounts"]
with open('done.csv', 'w', encoding='UTF8', newline='') as f:
  writer = csv.writer(f)
  writer.writerow(headerRow)
  writer.writerows(exportTable)
