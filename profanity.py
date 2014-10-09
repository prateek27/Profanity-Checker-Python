import urllib

def read_text():
    file = open("C:\Users\Prateek\Desktop\PythonPrograms\ProfanityChecker\incorrect.txt")
    contents = file.read()
    print(contents)
    checkProfanity(contents)
    file.close()

def checkProfanity(myText):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+myText)
    result = connection.read()
    if "true" in result:
        print("Alert!Something vulgar in your text!")
    elif "false" in result:
        print("Go Ahead ! Nothing wrong :) ")
    connection.close()
        
read_text()
