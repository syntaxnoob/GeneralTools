# ToJson

A python3 script that I used to transfer my youtube search data(google takeout) from an HTML file to a Json file.

### Method

The script reads the html file to a string.
The first and last 'Searched for' items in the string will be found.
A while loop will extract the 'search' and 'date' form the string.
All the results well be saved to a search.json file

### Requirements

1. python3
2. your google takeout data(html)
3. JSON lib

### install json lib

go to your operating system's terminal/commandline and type in: `pep3 install json`.

### Usage

1. Clone the project.
2. Locate your html file and place the script in the same directory.
3. Open your commandline/terminal and type: `python3 ToJson.py` .
4. A search.json file can be found in that directory.

If you use this script, please give credit to syntaxnoob.
