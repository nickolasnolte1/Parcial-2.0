from flask import Flask, render_template, request, url_for, redirect
from jinja2 import Template, Environment, FileSystemLoader
from typing import Dict, Text


file_loader=FileSystemLoader('templates')
env=Environment(loader=file_loader)

app=Flask(__name__)


def invertir(x):
  return x[::-1]


def largo(str): 
    contador = 0    
    for i in str: 
        contador += 1
    return contador 


def contar_vocales(cad):
    voc = 0
    for c in cad:
        if c == 'a' or c == 'e' or c == 'i' or c =='o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c =='O' or c == 'U':
            voc=voc+1
    return voc

def upper(string): 
print("") 
print(text.upper()) 


def updown(string:str)->str:
    palabranew=" "
    for i in range(len(string)):
        if i%2==0:
            palabranew+=string[i].upper()
        else:
            palabranew+=string[i].lower()
    return palabranew

def naive(string:str)->str:
    newstr=" "
    newstr = string.replace("a", "@").replace("e", "3").replace("i", "!").replace("o", "ø").replace("u", "µ")
    return newstr


def ejecutar(string: str) -> Dict:
    strings = {}
    if string== "":
        return strings
    strings["Invertido"] = string[::-1]
    strings["Largo"] = len(string)
    strings["Upper"] = string.upper()
    strings["Lower"] = string.lower()
    strings["Vocales"]=vocales(string)
    strings"updown"] = updown(string)
    strings["naive"] = naive(string)
    return strings


if __name__ == "__main__":
    debug = False
    if environment == "development" or environment == "local":
        debug = True
    app.run(host="0.0.0.0", debug=debug, port=5000)