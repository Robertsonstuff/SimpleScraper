from urllib import request
import re

html = request.urlopen("https://yourwebsite.com")
text = html.read()
CleanUp = text.decode('utf8')
SearchFor = re.findall(r"yourtag/", CleanUp)

# SearchFor = re.findall(r"yourtag/\w{3,50}", CleanUp)Using Regex, this will search for your tag followed by 3 - 50 alphanumeric characters. 

print(SearchFor)
