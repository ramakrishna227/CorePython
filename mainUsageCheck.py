def printThisStatement(stmt):
    print(stmt)

def main():
    print('stmt from main')
    printThisStatement('statement passed fom main')

# if I call main directly then the above main function is being invoked when I import this module to another module with out calling explicitly
# main()

if __name__=='__main__':main()