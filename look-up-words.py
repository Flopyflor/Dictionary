# -*- coding: latin-1 -*-

from bs4 import BeautifulSoup as bs4
import requests

SEP = "---------------------------"
FILE = "words.txt"

def look_up(word, DICT_URL="https://www.dictionary.com/browse/", DEF_CLASS="css-nnyc96"):
	#look up the dictionary entry
	r = requests.get(DICT_URL + word)
	html = r.text
	
	#is it empty?
	if r.status_code == 404:
		raise ValueError("the world you are looking for is not in the dictionary.")
	
	#identify the definitions
	soup = bs4(html, features="html.parser")
	defs = soup.find_all(class_=DEF_CLASS)
	
	return defs
	

if __name__ == "__main__":
	# Get words
	file = open(FILE, "r")
	words = file.readlines()
	file.close()
	
	# Greet
	print("Hello! Let's look up some words!")
	print()
	
	response = ""
	while response.upper()!= "Q" and words:
		print(SEP)
		
		# Word
		word = words.pop().strip()
		print(f"{word} definition:")
		print()
		
		try:
			# Look up and Show result
			defs = look_up(word)
			
			for i in defs:
				print(i.text)
		
		except ValueError:
			print("404: the word is not in the dictionary.")
			
		except requests.exceptions.ConnectionError:
			print("Sorry, but it seems you are having some connection issues.")
			
		# Next / exit
		print(SEP)
		response = input("Continue or Quit (Q): ")
		
	# Bye
	print(SEP)
	print("Have a nice day!")