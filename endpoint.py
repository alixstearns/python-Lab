import requests


def urlcheck(url):
    isUp=True
    try:
        resp = requests.get(url)
    except: 
        print('please double check your url')

        status = resp.status_code

        if status ==200:
            isUp
        else:
            isUp=False
    return isUp


'''
try:
    resp = requests.get('http://google.com')

    status = resp.status_code

    if status ==200:
        print('site is up')
    else:
        print('site is down')
except: 
    print('please double check your url')

#print(dir(resp))

#from jenkins_api import list_jobs
'''
