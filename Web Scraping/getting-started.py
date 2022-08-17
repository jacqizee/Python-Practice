from platform import python_branch
import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
# print(results.prettify())

job_elements = results.find_all("div", class_="card-content")
# for job_element in job_elements:
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print(title_element.text.strip(), company_element.text.strip(), location_element.text.strip(), sep='\n', end='\n'*2)

python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())
for job in python_jobs:
    print(job.text)

# Get Third-Level Parent Elements and Down
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

# Print All Links
for element in python_job_elements:
    links = element.find_all('a')
    for link in links:
        link_url = link['href']
        print("Apply Here:", link_url)

# Only Print Second Link
for element in python_job_elements:
    second_link = element.find_all('a')[1]
    print("Apply Here:", second_link['href'])