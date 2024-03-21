import os
import jenkins
import csv
server = jenkins.Jenkins('http://3.88.7.61:8080', 'alixstearns', 'Jules@1974')

jobs= server.get_all_jobs()

#for job in jobs:
    
    #print("Job name is:", job['name'])
    #print("Job URL is:", job['url'])


with open("jobs22.csv", 'w') as f: 
    pen = csv.writer(f) # object to be use to write the file pen or curseur
    header = ["Job_name", "url"]
    pen.writerow(header)
    
jenkins_csv_file('http://3.88.7.61:8080', 'alixstearns', 'Jules@1974')


    
    for job in jobs:
        job_name = job['name']
        job_url = job['url']
        pen.writerow([job_name, job_url])

print("Data written to jobs.csv successfully.")


j.close