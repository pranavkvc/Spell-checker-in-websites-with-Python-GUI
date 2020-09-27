import urllib.request 
import urllib.parse
import re
from tkinter import *
from spellchecker import SpellChecker
spell = SpellChecker()
import time
main = Tk()
main.title("PRANAV OWN CODE!")
main.geometry("700x500")
#function for text parsing
def parse():
    c=0
    url = inputbox.get()
    values={'s':'basics','submit':'search'}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url,data)
    resp = urllib.request.urlopen(req)
    Read = resp.read()
    content = re.findall(r'<p>(.*?)</p>',str(Read))   
    for i in content:
        mis = spell.unknown(i.split())
        for j in mis:
            if spell.correction(j):
                c+=1
                output.insert(END,j)

    output.insert(END,"\nTotal Mistakes found while parsing are [{}]".format(c))            


     
#taking input.
Titletext = Text(width=20,height=1,bg="light grey")
Titletext.grid(row=0,column=0,sticky=W)
Titletext.insert(END,"PASTE YOUR URL BELOW")
inputbox = Entry(main,width=20,bg="light grey")
inputbox.grid(row=1,column=0,sticky=W)
#Adding Buttons!
Button(main,width=20,text="EXECUTE AND PARSE",command=parse).grid(row=2,column=0,sticky=W)
#Here the output goes
output = Text(width=75,height=25,bg="light grey")
output.grid(row=3,column=0,sticky=W)


main.mainloop()