import requests
from bs4 import BeautifulSoup as bs
import pandas

states = ['New-York', 'New-Jersey', 'Connecticut']
URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=New-York&stpage=1&page=2'

page = requests.get(URL)

soup = bs(page.content, 'html.parser')

results = soup.find('div', id='ResultsContainer')
jobs = results.find_all('section', class_='card-content')

job_list=[]

for job in jobs:
    title = job.find('h2', class_='title')
    company = job.find('div', class_='company')
    location = job.find('div', class_='location')
    if None in (title, company, location):
        continue
    a_tag = title.find('a')
    link = a_tag['href']
    details = requests.get(link)
    detail_soup = bs(details.content, 'html.parser')
    money_divs = detail_soup.find_all(
        'div', class_='col-md-12 col-8 ta-md-l ta-r font-semibold')
    money_div = None
    salary=None
    for div in money_divs:
        if div['name'] == 'value_salary':
            money_div = div
            salary = money_div.text.strip()
    job_list.append([title.text.strip(), company.text.strip(), location.text.strip(), salary, link])
    print(title.text.strip())
    # print(company.text.strip())
    # print(location.text.strip())
    # print(salary)
    # print(link)
    # print()


jobs_df = pandas.DataFrame(columns=['Title', 'Company', 'Location', 'Salary', 'Link'], data=job_list)
print(jobs_df)
jobs_df.to_csv("jobs.xlsx") 