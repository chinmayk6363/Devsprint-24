import re
from pdfminer.high_level import extract_pages,extract_text
import pyclamd
# cd = pyclamd.ClamdAgnostic()
# cd.ping()

data = extract_text("")

web_technologies = [
    "HTML5", "CSS3", "JavaScript",
    "React.js", "Angular", "Vue.js",
    "Python", "Django", "Flask",
    "Node.js", "Express.js",
    "Ruby on Rails", "Java", "Spring Boot",
    "PHP", "Laravel",
    "SQL", "MySQL", "PostgreSQL", "SQLite",
    "NoSQL", "MongoDB", "Cassandra", "CouchDB",
    "Git", "RESTful APIs", "GraphQL",
    "Docker", "Kubernetes",
    "Nginx", "Apache",
    "AWS", "Amazon Web Services",
    "Azure", "Google Cloud Platform", "GCP",
    "Jenkins", "Travis CI", "CircleCI",
    "Unit testing", "pytest", "unittest",
    "Integration testing",
    "HTTPS", "Cross-Site Scripting", "XSS prevention", "Cross-Site Request Forgery", "CSRF prevention"
]

l=[]
# if cd.scan_file("res.pdf") is None:
#     print(" file is clean")

for i in web_technologies:
    if i in data:
        l.append(i)

print("My skills: ")
print(l)