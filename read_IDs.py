import csv
counter = 0 #will keep track of the total number of articles
with open('personal_informatics.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['id']) #prints the ID number of the article
        counter+= 1
        
print(counter) #prints out total number of articles at the end
