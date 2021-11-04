import webbrowser
## This represents how many times you want to open spam the webpage
times = 100#Deafult
for x in range(0, times):
    with open('website.txt') as f:
        contents = f.read()
        webbrowser.open(contents)



## DO NOT Test this on your own computer the result will be multiple crashes
## Only for educational Purposes
