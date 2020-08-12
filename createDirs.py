#!/usr/bin/env pypy3

#This is script is meant to create directories in your current working directory. 
#It very convenietly creates directories from my notes on filmographies or bibliographies of a director.
#The script also gives you an option of creating directories based on your copy and paste notes of 
#a YouTube playlist. 
#In every directory of such playlist the script creates an empty file "timing.html.pmd" for your future notes

import os, re

count = 0

file = input("Give me the name of the file that is meant to give the names of the directories that I'm going to create.\n")

#spaceLowerCase = re.compile(r" [a-z]") #to be replaced with CamelCase

markup_chars = ("#", "@", "[", "(", ">", '"')
otherNonStarters = ("\n", "\t", "\r", "  ") 


numberedOrNot = input("Would you like me to number the directories I'm going to create?(Y/n?)\n")

if numberedOrNot == "N" or numberedOrNot == "n" or numberedOrNot == "NO" or numberedOrNot == "No" or numberedOrNot == "no":
    whateverGraphy = input("By any chance, are you creating directories of a bibliography/filmography?\n") #This has to ba asked now in order for ot not be asked with each line

if numberedOrNot == "Y" or numberedOrNot == "y" or numberedOrNot == "YES" or numberedOrNot == "Yes" or numberedOrNot == "yes":
    whateverYT = input("By any chance, are you creating directories of a YouTube playlist\n") #This has to ba asked now in order for ot not be asked with each line
    if whateverYT == "Y" or whateverYT == "y" or whateverYT == "YES" or whateverYT == "Yes" or whateverYT == "yes":
        name = input("What's the name of the YouTube channel?\n")
    else:
                print("I've not yet written any code for any other numbered list than a YouTube playlist.")


#otherLines = input("Any other?")

with open(file) as f:
    for line in f:
        if numberedOrNot == "Y" or numberedOrNot == "y" or numberedOrNot == "YES" or numberedOrNot == "Yes" or numberedOrNot == "yes":
            if whateverYT == "Y" or whateverYT == "y" or whateverYT == "YES" or whateverYT == "Yes" or whateverYT == "yes":
                line = line.replace("NOW PLAYING", "") 
                line = line.replace(name, "")
                numberOnly = re.compile(r"^\d{1,3}\n")
                length = re.compile(r"^\d{1,2}:\d{1,2}.{0,}")
                match = re.match(numberOnly, line)
                if match:
                    line = re.sub(numberOnly, "", line)
                match = re.match(length, line)
                if match:
                    line = re.sub(length, "", line)    
                line = line.replace(",", " ").replace(":", " ").replace("/", " ").replace(" ", "_").replace("\n", "")
                line = line.replace("__", "_")
                line = line.replace("__", "_")
                if line == "" or line == " " or line.startswith(markup_chars) or line.startswith(otherNonStarters): #It does not work without checking line == ""
                    pass
                else:
                    count += 1
                    path = f"{count}.{line}"
                    print(line)
                    os.mkdir(path)
                    timingFile = f"./{path}/timing.html.pmd"
                    with open(timingFile, "w"):
                        pass
        if numberedOrNot == "N" or numberedOrNot == "n" or numberedOrNot == "NO" or numberedOrNot == "No" or numberedOrNot == "no":
            if whateverGraphy == "Y" or whateverGraphy == "y" or whateverGraphy == "YES" or whateverGraphy == "Yes" or whateverGraphy == "yes":
                date = re.compile(r"^\d{4,4}")
                match = re.match(date, line)
                if match:
                    parenthesesAfterTheTitle = re.compile(r"\(.{1,}")
                    line = re.sub(parenthesesAfterTheTitle, "", line)
                    path = f"{line}"
                    print(line)
                    os.mkdir(path)
                    review = f"./{path}/review.html.pmd"
                    with open(review, "w"):
                        pass
            if whateverGraphy == "N" or whateverGraphy == "n" or whateverGraphy == "NO" or whateverGraphy == "No" or whateverGraphy == "no":
                if line == "" or line == " " or line.startswith(markup_chars) or line.startswith(otherNonStarters): #It does not work without checking line == ""
                    pass
                else:
                    path = f"{line}"
                    print(line)
                    os.mkdir(path)
                
        
#https://blog.finxter.com/regex-startswith-python/
#When practising, use rm -r */ to conveniently remove directories that you created
