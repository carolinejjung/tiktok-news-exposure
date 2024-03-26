import csv
def getArticleHeadline(csvFilePath):
    #headlineList = []
    with open(csvFilePath, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            #headline = row['headline']['main']
            print(row['headline'])
        #headline=[row['headline']for row in csv_reader]
        #headlineList.append(headline) #headline at row[2], populating headlineList here
        #print(headline)
    #return headline
    #return headlineList #returning a list of all headlines in specified csv

getArticleHeadline("articles_2024-02-21.csv")