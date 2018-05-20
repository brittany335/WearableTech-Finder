#!/usr/bin/env python

from flask import Flask, send_from_directory, render_template
from ast import literal_eval # used when we are opening our textfile
import os

#https://stackoverflow.com/questions/32019733/getting-value-from-select-tag-using-flask

# reference to code is from https://pythonprogramming.net/jquery-flask-tutorial/
# and from https://www.blog.pythonlibrary.org/2017/12/13/flask-101-how-to-add-a-search-form/
app = Flask(__name__)

@app.route("/")
def gallery():
	#going into the image folder for the screenshots of the urls
	image_names = os.listdir('./images')

	# opening our textfile as a list and not as a string of a list
	with open('company_info.txt') as f:
	    mainlist = [list(literal_eval(line)) for line in f]

	# gathers everything from the lists of lists and makes them into one big list of comapny information that contains a list of dictionarys  https://stackoverflow.com/questions/952914/making-a-flat-list-out-of-list-of-lists-in-python
	flat_list = [item for sublist in mainlist for item in sublist]

	#most recent order of things added, I want my url to have the most recent companies scraped at the top of the pages
	# so I need to reverse the order of the flat_list
	reversed_order=(flat_list[::-1])
	size=len(image_names)

	return render_template("gallery17.html", image_names=image_names, reversed_order=reversed_order,size=size)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

if __name__=='__main__':
    app.run(host='127.0.0.1', port=6039, debug=True)
