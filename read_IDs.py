import csv

counter = 0 #will keep track of the total number of articles
list_of_IDs = []

with open('combined_file.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        list_of_IDs.append((row['id'])) #appends the ID number of the article

#set_of_IDs = set(list_of_IDs) #sets contain no duplicates, so this will remove duplicates
        
list_of_IDs = list(dict.fromkeys(list_of_IDs))
#dictionaries cannot have duplicate keys, so this line removes duplicates and returns it as a list.

for id in list_of_IDs:
    print(id)
    counter+= 1
    
print(counter) #prints out total number of articles at the end
#8123 articles in combined_file; after removing duplicates, 6079 total articles.

with open('no_duplicates.csv', newline='') as csvfile:
    fieldnames = ['type', 'id', 'author', 'editor', 'advisor', 'note', 'title', 'pages', 'article_no',
                  'num_pages', 'keywords', 'doi', 'journal', 'issue_date', 'volume', 'issue_no',
                  'description', 'month', 'year', 'issn', 'booktitle', 'acronym', 'edition', 'isbn',
                  'conf_loc', 'publisher', 'publisher_loc']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    
    #writer.writeheader()
    
    #somehow, need to iterate through list_of_IDs, find the matching ID in combined_file.csv using the
    #reader,then write that to the no_duplicates.csv file. (Maybe I can do this without a second file?!)
    
    #writer.writerow({'type', 'id', 'author', 'editor', 'advisor', 'note', 'title', 'pages', 'article_no',
    #             'num_pages', 'keywords', 'doi', 'journal', 'issue_date', 'volume', 'issue_no',
    #            'description', 'month', 'year', 'issn', 'booktitle', 'acronym', 'edition', 'isbn',
    #           'conf_loc', 'publisher', 'publisher_loc'})


