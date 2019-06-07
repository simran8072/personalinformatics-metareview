import csv
import pprint

list_of_IDs2 = []
#for some reason, final list of paper had duplicates after running through. Getting rid of these                
with open('still_has_duplicates.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        list_of_IDs2.append((row['id'])) #appends the ID number of the article

#set_of_IDs = set(list_of_IDs) #sets contain no duplicates, so this will remove duplicates
        
list_of_IDs2 = list(dict.fromkeys(list_of_IDs2))
#dictionaries cannot have duplicate keys, so this line removes duplicates and returns it as a list.

#now, write the info into the list_of_papers csv file
with open('final_list_of_papers.csv', 'w', newline='') as writeFile:
    fieldnames = ['id', 'URL', 'author', 'title', 'keywords', 'doi', 'year','publication_venue']
    writer = csv.DictWriter(writeFile, fieldnames = fieldnames)
    
    writer.writeheader()
    with open('still_has_duplicates.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        #go through each id in the list of non-duplicates and each row of the combined file
        for idnum in list_of_IDs2:
            for row in reader:
             
                # if we found the record we are looking for
                if (idnum == row['id']):
                    writer.writerow({'id': row['id'], 'URL': "https://dl.acm.org/citation.cfm?id=" + row['id'], 'author': row['author'],
                                     'title': row['title'], 'keywords': row['keywords'],'doi': row['doi'],
                                     'year': row['year'], 'publication_venue': row['publication_venue']})
                    
                    # move on to the next ID
                    break
                
list_of_keywords = []
count = 0

with open('final_list_of_papers.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #temp_string will contain the keywords for the certain article, separated by commas
        temp_string = row['keywords'].lower()
        #put these in a temporary list
        temp_list = temp_string.split(", ")
        #and append the words in the temporary list to the list of keywords
        for word in temp_list:
            list_of_keywords.append(word)

#because 1300+ keywords is way too much to deal with, I decided to narrow down the keywords we examine
#to those that show up 5 or more times throughout all the articles.
narrowed_list = []
for word in list_of_keywords:
    #taking away those keywords that show up less than 5 times
    if ((list_of_keywords.count(word)) > 4):
        #blank space was showing up as keyword for whatever reason, so just get rid of that
        if word == "":
            continue
        narrowed_list.append(word)

narrowed_list = list(dict.fromkeys(narrowed_list))

#for word in narrowed_list:
#    count += 1
#count is 53    
#print(count)

#print(list_of_keywords.count('self-tracking'))
#print(narrowed_list)

# 53 rows for 53 keywords to be examined
r = 53
# 10 columns for the years 2010-2019
c = 10
#first, set everything to 0
array_of_stats = [[0] * c for i in range(r)]



keyword_count = 0
#go through each of the 53 keywords
for keyword in narrowed_list:
    #each time, open the final list of papers file and go through searching for the keyword
    with open('final_list_of_papers.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        #if the keyword is in the row, increment the correct year element by one
        for row in reader:
            if keyword in row['keywords']:
                temp_year = int(row['year'], 10)
                if (temp_year > 2009):
                    array_of_stats[keyword_count][temp_year - 2010] += 1
        
        keyword_count += 1      
                

#make it print out nicely
#pp = pprint.PrettyPrinter()
#pp.pprint(array_of_stats)


#write this 2D array to an excel file
with open('keyword_stats.csv', 'w', newline='') as writeFile:
    fieldnames = ['keywords', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
    writer = csv.DictWriter(writeFile, fieldnames = fieldnames)
    writer.writeheader()
    keyword_count = 0
    for keyword in narrowed_list:
        writer.writerow({'keywords': keyword, '2010': array_of_stats[keyword_count][0],
                         '2011': array_of_stats[keyword_count][1], '2012':array_of_stats[keyword_count][2],
                         '2013': array_of_stats[keyword_count][3], '2014':array_of_stats[keyword_count][4],
                         '2015': array_of_stats[keyword_count][5], '2016': array_of_stats[keyword_count][6],
                         '2017': array_of_stats[keyword_count][7], '2018': array_of_stats[keyword_count][8],
                         '2019': array_of_stats[keyword_count][9]})
        keyword_count += 1
        
        
        