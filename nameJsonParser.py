from json import dump

names = """
Wade Mercer
Sariah Hampton
Marilyn Miranda
Jessie Leach
Gracie Malone
Lexie Hardy
Madden Perry
Adrienne Bush
Aydin Vargas
Russell Johns
Nataly Morse
Yahir Mendoza
Lara Bonilla
Deborah Mason
Angelique Jennings
Rodrigo Newton
Giselle Zamora
Akira Munoz
Mollie Mccormick
Kimberly Pope
"""
jsonFile = open("names.json","w")
data = []
for name in names.split("\n")[1:-1]:
    data.append(name.split())
dump(data,jsonFile)

import os
# print(os.pardir)
os.system("git add .");
os.system('git commit -m "updated"');
os.system("git push");