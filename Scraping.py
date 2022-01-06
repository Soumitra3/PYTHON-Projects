from bs4 import BeautifulSoup
import requests
import time

print('Enter skills not familiar with!')
unfam_skill = input('>')
print(f'Filtering out {unfam_skill}')

def find_jobs():
 html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
 soup = BeautifulSoup(html_text, 'lxml')
 jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
 for index, job in enumerate(jobs):
    comp_name = job.find('h3', class_ ='joblist-comp-name').text.replace(' ','')
    skills = job.find('span', class_ ='srp-skills').text.replace(' ','')
    more_info = job.header.h2.a['href']
   
    if unfam_skill not in skills: 
       print(f"Comapny Name: {comp_name.strip()}")
       print(f"Skills Required: {skills.strip()}")
       print(f"More Info: {more_info}")
       print('')

if __name__ == '__main__':
   while True:
      find_jobs()
      time_wait = 10
      print(f'Waiting for {time_wait} seconds...')
      time.sleep(time_wait * 6)
      