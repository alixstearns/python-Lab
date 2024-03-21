                        
import jenkins
import csv


def list_jobs(jenkins_url,jenkins_user,jenkins_pass):
    server = jenkins.Jenkins(jenkins_url, username=jenkins_user, password=jenkins_pass)
    Jobs=server.get_jobs()
    list_of_jobs=[]
    for i in Jobs:
        list_of_jobs.append([i['name'], i['url'], i.get('color')])
    return list_of_jobs

def startJobs():
    pass
    

#list_jobs('http://54.172.51.138:8080','devops','devops')

def jenkins_csv_file(my_list):
    with open("jenkins_inventory.csv", 'w',newline='') as j:
        pen = csv.writer(j)
        header=['JOBS_NAME', 'JOB_URL', 'JOB_LAST_BUILD_STATUS']
        pen.writerow(header)
        for item in my_list:
            pen.writerow(item)
    j.close
            
#jenkins_csv_file(list_jobs('http://54.172.51.138:8080','devops','devops'))
jenkins_jobs =list_jobs('http://54.172.51.138:8080','devops','devops')
jenkins_csv_file(jenkins_jobs)



'''
import jenkins
import csv

def jenkins_csv_file(my_list):
    with open("jenkins_inventory.csv", 'w',newline='') as j:
        pen = csv.writer(j)
        header=['JOBS_NAME', 'JOB_URL', 'JOB_LAST_BUILD_STATUS']
        pen.writerow(header)
        for item in my_list:
            pen.writerow(item)
    j.close
            
#jenkins_csv_file(list_jobs('http://3.88.7.61:8080', 'alixstearns', 'Jules@1974'))
jenkins_jobs =list_jobs('http://3.88.7.61:8080', 'alixstearns', 'Jules@1974')
jenkins_csv_file(jenkins_jobs)






def list_jobs(jenkins_url, jenkins_user, jenkins_pass):
    server = jenkins.Jenkins(jenkins_url, jenkins_user, jenkins_pass)
    jobs=server.get_jobs()
    #print(jobs)
    list_of_jobs=[]
    for i in jobs:
        list_of_jobs.append([i['name'], i['url'], i.get('color')])
        return list_of_jobs

def startJobs():
     pass

#a=list_jobs('http://3.88.7.61:8080', 'alixstearns', 'Jules@1974')
#print(a)

def jenkins_csv_file(my_list):
    with open("jenkins_inventory.csv", 'w', newline='') as j: 
        pen = csv.writer(j) # object to be use to write the file pen or curseur
        header = ["JOBS_NAME", "JOB_URL", 'JOB_LAST_BUILD_STATUS']
        pen.writerow(header)
        
        for item in my_list:
            pen.writerow(item)

server = jenkins.Jenkins('http://3.88.7.61:8080', 'alixstearns', 'Jules@1974')

jenkins_csv_file('http://3.88.7.61:8080', 'alixstearns', 'Jules@1974')

j.close



with open("jobs22.csv", 'w') as f: 
    pen = csv.writer(f) # object to be use to write the file pen or curseur
    header = ["Job_name", "url"]
    pen.writerow(header)
    
jenkins_csv_file('http://3.88.7.61:8080', 'alixstearns', 'Jules@1974')




#a= list_jobs()
#print(a)



#import os
#server = jenkins.Jenkins('http://3.88.7.61:8080', username='alixstearns', password='Jules@1974')
#jobs=server.get_jobs()
#print(jobs)
#list_of_jobs=[]
#for i in jobs:
   # list_of_jobs.append([i['name'], i['url'], i.get('color')])
    #print(list_of_jobs)

    #list_jobs()

    #print("************************************************")
    #print(i['name'], i['url'], i.get('color'))


#user = server.get_whoami()
#version = server.get_version()
#print(user['id'], version)


os.system('clear')

print(dir(server))
job_number= server.jobs_count()

node_list= server.get_nodes()
jobs= server.get_all_jobs()
#print(job_number)
#print(node_list)
#print(jobs)

#for job in jobs:
#       print("*****************************************************************")
#       print(job)
 #      print(f"job name is:" {['name']}, "job url is:"{['url']})

for job in jobs:
    print("*****************************************************************")
    print("Job name is:", job['name'])
    print("Job URL is:", job['url'])
    '''