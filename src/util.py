

def log(message, filename):
    with open(str(filename)+".log", "a") as myfile:
        myfile.write(str(message)+'\n')
