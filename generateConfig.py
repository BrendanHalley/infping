import urllib.request
import re

regex = r"(\[.*\].*\[(.*)\])"

url = 'https://raw.githubusercontent.com/jlu5/netmeter.club/confv2/Targets-Shared'
response = urllib.request.urlopen(url)
data = response.read()
text = data.decode('utf-8')

matches = re.finditer(regex, text, re.MULTILINE)
for matchNum, match in enumerate(matches, start=1):

    print("[hosts."+match.groups()[1].replace(".", "_")+"]")
    print("ip = \""+match.groups()[1]+"\"")
    print("description = \""+match.groups()[0]+"\"")
    print()
