#!/bin/python3

import json

# Importing the HTML file.

with open('search-history.html', 'r') as html_file:
    data = html_file.read()
html_file.close()

# Find :'Searched for' until '\">' and from the '\">' until </a>.
# That is where the search lives.

# Variables
sf = "Searched for"
first = data.find(sf, 0)
last = data.rfind(sf, 0)
selected = 0

searches = {}

# While loop(We don't know how many searches there are).
# That is why we loop from first hit to the last one.

while selected != last:
    i = len(searches)
    between = data.find("\">", first)
    voor = (data.find("</a>", between) + 8)
    datum = data[voor:data.find("</div>", between)]

    searches[i] = {}
    searches[i]["search: "] = data[(between + 2):(data.find("</a>", between))]
    searches[i]["date: "] = datum
    selected = first
    first = data.find(sf, (first + 1))

print("klaar")

# Dump to json file.

with open('search.json', 'w') as f:
    json.dump(searches, f, indent=2)
f.close()
