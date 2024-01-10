import csv

with open("/home/ubuntu/ieee.documents.csv", newline='') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    rows = iter(csv_data)
    next(rows)
    for i in range(3):
        row = next(rows)
        cols = iter(row)
        id = next(cols)
        authors = []
        for j in range(18):
            author = next(cols)
            if(author!=''): 
                authors.append(author)
        title = next(cols)
        doi = next(cols)
        year = next(cols)
        issue = next(cols)
        abstract = next(cols)
        keywords = []
        for j in range(27):
            keyword = next(cols)
            if(keyword!=''):
                keywords.append(keyword)
        
        paper = {
            'id':id,
            'authors':authors,
            'title':title,
            'doi':doi,
            'year':year,
            'issue':issue,
            'abstract':abstract,
            'keywords':keywords
        }
        
        print(paper, end="\n\n")    
# with open("/home/ubuntu/ieee.documents_test.txt", 'w') as out_file:
#     for row in csv_data:
#         out_file.write(f'{row}\n\n')