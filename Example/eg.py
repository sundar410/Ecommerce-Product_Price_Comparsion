# Working With Beautifulsoup Library 

import requests
from bs4 import BeautifulSoup
URL = "https://realpython.github.io/fake-jobs/"
r = requests.get(URL)
soup = BeautifulSoup(r.content, "html.parser")
results = soup.find(id="ResultsContainer")
print(results.prettify())
job_elements = results.find_all("div", class_="card-content")
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print("Title: ",title_element.text.strip())
    print("Company Name: ",company_element.text.strip())
    print("Location: ",location_element.text.strip(), "\n")
    
