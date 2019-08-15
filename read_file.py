serverList = {}


def ReadFile(fileName):
    try:
        f = open(fileName, "r")
    except Exception as e:
        print("Could not open File " + fileName)
        print(e.args)
        return False
    else:
        try:
            for lines in f.readlines():
                hostName, passWord = lines.strip('\n').split(",")
                serverList[hostName] = passWord
        except Exception as e:
            print("Check the file format")
            print(e.args)
            return False
    return True


if (ReadFile('C:/Users/Anish/Projects/py/file.txt')):
    for server in serverList.keys():
        print(server + " : " + serverList[server])
