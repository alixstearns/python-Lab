import os


def hello():
    print("hello alix")
    print("how are you")

def hello1(name):
    print(f'hello{name}')
    print("how are you?")
    hello1('ellys')

def Command(cmd):
    os.system(cmd)

#Command('ls')

def list_files(dir_path):

    _DIR= dir_path # the directory # _DIR="/var/log"

    for item in os.listdir(dir_path):
            path= os.path.join(dir_path, item)
            if os.path.isfile(path):
                            print(f"{path}   is a file")
            else:
                            print(f"{path}   is a directory")



def add(a,b):
      return a+b

var_=add(2,4)
print(var_)

