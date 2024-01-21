'''
Python web scraping project

You will use the Beautiful Soup 4 and requests module to web scrape a job site to get salary information. 

The site you will be scraping is reed.co.uk and will be allowing the user to select the job title and location they desire for their job.

Your objective is to get the following data points as floats:
-Highest salary
-Lowest salary
-Average salary
-Total salaries reported
'''

import requests as rq
from bs4 import BeautifulSoup

job = input('Please provide a job for the search: ')
job.replace(' ', '-')
place = input('Please provide a place for the search: ')
place.replace(' ', '-')


URL = f'https://www.reed.co.uk/average-salary/average-{job}-salary-in-{place}'

session = rq.Session() # ex. list to remind the alzheimers patient to take his meds, take a walk , etc.
#session.headers.update({}) #just in case website don't like this program existing :)

content = session.get(URL).content
parser = BeautifulSoup(content, 'html.parser')

#print(parser)

taglist = parser.select('.salary-chart-limit .salary-value')[:2] #highest and lowest
taglist.extend(parser.select('.salary-title-value')) #average
taglist.extend(parser.select('.salary-info-title')[1]) #total reported jobs
textlist = []

for _ in range(len(taglist)):
    textlist.append(taglist[_].text)

    str(textlist[_])
    textlist[_] = textlist[_].replace('£', '')
    textlist[_] = textlist[_].replace(',', '.')
    float(textlist[_])

print(f'Average {job} salary in {place}: £{textlist[2]},\nHighest salary: £{textlist[1]},\nLowest salary: £{textlist[0]},\nTotal salaries reported: {textlist[3]}')

# requests -> HTTP requests
# bs4 (Beautiful soup) -> HTML parser

# HTTP request -> Get HTML document -> Parse HTML document -> Extract values via tags and attributes