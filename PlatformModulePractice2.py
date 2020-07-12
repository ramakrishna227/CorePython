import platform

#def is to define function. we go with indentation in python insted of peranthesis and semicolons
def main():
    printPythonVersion()

def printPythonVersion():
    print('Python version is {}'.format(platform.python_version()))

if __name__=='__main__':main()