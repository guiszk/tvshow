#!/usr/bin/env python3.7
import os, sys, re, requests
from bs4 import BeautifulSoup as bs

if(len(sys.argv) < 3):
    sys.stderr.write("{0} <name> <path> <*name>\n".format(sys.argv[0]))
    sys.exit(1)
path = os.path.abspath(sys.argv[2])
pathdir = os.path.dirname(sys.argv[2])
if not (os.path.isfile(sys.argv[2])):
    sys.stderr.write("<path> must be a file\n")
    sys.exit(1)
ext = path.split(".")[::-1][0]
pathindex = re.search(r"[sS][0-9]+[eE][0-9]+", path)
if(pathindex != None):
    pathindex = pathindex.group(0)
    pathseason = re.search(r"(?<=[sS])[0-9]+", path).group(0)
else:
    sys.stderr.write("Season/episode name not found.\n")
    exit(1)
#url = 'https://www.thetvdb.com/series/regular-show/seasons/official/3'
url = 'https://www.thetvdb.com/series/' + sys.argv[1] + '/seasons/official/' + str(int(pathseason))
page = requests.get(url)
soup = bs(page.text, 'html.parser')
table = soup.find(class_='table table-condensed table-bordered')
eptable = table.find_all('tr')
nametable = table.find_all('a')

index = []
name = []
assoc = {}

n=0
for i in eptable:
    s = re.search(r"[sS][0-9]+[eE][0-9]+", str(i).strip())
    if(s != None):
        index.append(s.group(0))
n = 0
for i in nametable:
    name.append(i.contents[0].strip())

for i,j in zip(index,name):
    assoc[i] = j

if(len(sys.argv) > 3):
    sname = sys.argv[::-1][0]
else:
    sname = input("Enter series name: ")
newname = pathdir + "/" + str(sname) + "." + pathindex.upper() + "." + assoc[pathindex.upper()].replace(" ", ".") + "." + ext
os.rename(path, newname)
