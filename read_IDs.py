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
    #print(id)
    counter+= 1
    
#print(counter) #prints out total number of articles at the end
#644 articles in combined_file; after removing duplicates, 472 total articles.

with open('no_duplicates.csv', 'w', newline='') as writeFile:
    fieldnames = ['type', 'id', 'author', 'editor', 'advisor', 'note', 'title', 'pages', 'article_no',
                  'num_pages', 'keywords', 'doi', 'journal', 'issue_date', 'volume', 'issue_no',
                  'description', 'month', 'year', 'issn', 'booktitle', 'acronym', 'edition', 'isbn',
                  'conf_loc', 'publisher', 'publisher_loc']
    writer = csv.DictWriter(writeFile, fieldnames = fieldnames)
    
    writer.writeheader()
    
    #Need to iterate through list_of_IDs, find the matching ID in combined_file.csv using the
    #reader, then write that to the no_duplicates.csv file.
    with open('combined_file.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        #go through each id in the list of non-duplicates and each row of the combined file
        for idnum in list_of_IDs:
            for row in reader:
             
                # if we found the record we are looking for
                if (idnum == row['id']):
                    
                    # write out the record
                    writer.writerow({'type': row['type'], 'id': row['id'], 'author': row['author'],
                                     'editor': row['editor'],'advisor': row['advisor'], 'note': row['note'],
                                     'title': row['title'], 'pages': row['pages'],'article_no': row['article_no'],
                                     'num_pages': row['num_pages'], 'keywords': row['keywords'],'doi': row['doi'],
                                     'journal': row['journal'], 'issue_date': row['issue_date'],'volume': row['volume'],
                                     'issue_no': row['issue_no'], 'description': row['description'],'month': row['month'],
                                     'year': row['year'], 'issn': row['issn'], 'booktitle': row['booktitle'],
                                     'acronym': row['acronym'], 'edition': row['edition'], 'isbn': row['isbn'],
                                     'conf_loc': row['conf_loc'], 'publisher': row['publisher'],
                                     'publisher_loc': row['publisher_loc']})
                    
                    # move on to the next ID
                    break


