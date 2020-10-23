#!/usr/bin/env python3.7
import os, sys, re, requests
from bs4 import BeautifulSoup as bs

if(len(sys.argv) != 2):
    sys.stderr.write("{0} <path>\n".format(sys.argv[0]))
    sys.exit(1)
if not (os.path.isdir(sys.argv[1])):
    sys.stderr.write("<path> must be a directory\n")
    sys.exit(1)

allowed = [".avi", ".flv", ".mkv", ".mov", ".mp4", ".mpg", ".mpeg"]

pathdir = os.path.dirname(sys.argv[1])
files = [f for f in os.listdir(pathdir) if not f.startswith('.')]
ext = files[0].split(".")[::-1][0]

for f in files:
    pindex = re.search(r"[sS][0-9]+[eE][0-9]+", f)
    if(pindex != None):
        pathindex = pindex.group(0)
        pathseason = re.search(r"(?<=[sS])[0-9]+", pathindex).group(0)
    sname = re.search(r".+(?=.[sS][0-9]+[eE][0-9]+)", f)
    if(sname != None):
        sname = str(re.search(r".+(?=.[sS][0-9]+[eE][0-9]+)", f).group(0)).title()

url = 'https://www.thetvdb.com/series/' + (sname.lower()).replace(".", "-") + '/seasons/official/' + str(int(pathseason))
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

for f in files:
    f = pathdir + "/" + str(f)
    pindex = re.search(r"[sS][0-9]+[eE][0-9]+", f)
    if(pindex != None):
        pathindex = pindex.group(0).upper()
        pathseason = re.search(r"(?<=[sS])[0-9]+", f).group(0)
    newname = str(pathdir) + "/" + str(sname) + "." + str(pathindex) + "." + assoc[pathindex].replace(" ", ".") + "." + ext
    os.rename(f, newname)
