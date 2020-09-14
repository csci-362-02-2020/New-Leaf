#!/usr/bin/env python3

#
# myList.py
# myList
#
# New-Leaf
# lukem1, chris-m-taylor, cafeheart
# 12 September 2020
#

from datetime import datetime
import os
from subprocess import run
import webbrowser

startTime = datetime.now()
startDir = os.getcwd()

htmlHead = """
<head>
<title>Current Directory</title>
  <style>
  
	body {   
		background-color: rgb(150, 108, 39);
	}
    
	h1 {
		display: flex;
		justify-content: center;
		color: rgb(255, 200, 53);
	}
    
	.scripts {
		display: flex;
		justify-content: center;
		color: rgb(243, 242, 236);
	}
    
	p {
		display: flex;
		text-align: left;
		justify-content: center;
	}
    
    .button
	{
		border: none;
		border-radius: 12px;
		color: white;
		padding: 8px 16px;
		text-align: center;
		text-decoration: none;
		display: inline-block;
		font-size: 12px;
	}

	.button:hover
	{
		box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24),0 17px 50px 0 rgba(0,0,0,0.19);
	}
	.wrapper
	{
		padding-bottom: 10px;
		text-align: center;
		justify-content: center;
	}

    
  </style>

</head>
"""

button = """
<form action="file://%s" style="display: inline-block;">
	<button class="button" type="submit" style="background-color: #ff4015">Go</button>
</form>
"""
# Build the html file from command output, store in /tmp, and open in web browser
def buildHTML(lsOut, treeOut):
	tmpFile = "/tmp/newleaf-myList.html"
	
	print("Generating html at %s..." % tmpFile)
	
	with open(tmpFile, "w+") as file:
		file.write(htmlHead)
		file.write("<body>\n<h1>%s</h1>" % startDir)
		#file.write("<div class='scripts'>")
		#TODO: Parse lsOut and create tags for text, buttons
		ls = lsOut.split("\n")[1:-1]
		for f in ls:
			path = "%s/%s" % (startDir, f.split(" ")[-1])
			file.write("<div class='wrapper'><p style='display: inline-block;'>%s</p>" % f)
			file.write(button % path)
			file.write("</div>")
			
		file.write("<p style='color: rgb(255, 200, 53);'>Directory Tree</p>")
		file.write("<p>%s</p>" % treeOut.replace("\n", "<br>"))
		file.write("</body>")
		
		
	print("Opening %s..." % tmpFile)
	webbrowser.open(tmpFile)
	
	
def main():
	print("myList by New-Leaf (python version)")
	
	# Run ls command and capture output
	ls = run(["ls", "-la"], capture_output=True, text=True)

	# Run tree command if available and capture output
	treeOut = "Install tree for even more information!"
	try:
		tree = run(["nmap"], capture_output=True, text=True)
		treeOut = tree.stdout
	except FileNotFoundError:
		print("tree not found, install with: sudo apt install tree")

	buildHTML(ls.stdout, treeOut)
	
	print("Done.")

	
if __name__ == "__main__":
	main()

