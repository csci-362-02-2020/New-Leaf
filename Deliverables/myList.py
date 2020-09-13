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
    }
    
  </style>

</head>
"""

# Build the html file from command output, store in /tmp, and open in web browser
def buildHTML(lsOut, treeOut):
	tmpFile = "/tmp/newleaf-myList.html"
	
	print("Generating html at %s..." % tmpFile)
	
	with open(tmpFile, "w+") as file:
		file.write(htmlHead)
		file.write("<body>\n<h1>%s</h1>" % startDir)
		file.write("<div class='scripts'>")
		#TODO: Parse lsOut and create tags for text, buttons
		file.write("<p>%s</p>" % treeOut.replace("\n", "<br>"))
		file.write("</div>\n</body>")
		
		
	print("Opening %s..." % tmpFile)
	webbrowser.open(tmpFile)
	
	
def main():
	print("myList by New-Leaf (python version)")
	
	# Run ls command and capture output
	ls = run(["ls", "-la"], capture_output=True, text=True)

	# Run tree command if available and capture output
	treeOut = "Install tree for even more information!"
	try:
		tree = run(["tree"], capture_output=True, text=True)
		treeOut = tree.stdout
	except FileNotFoundError:
		print("tree not found, install with: sudo apt install tree")

	buildHTML(ls.stdout, treeOut)
	
	print("Done.")

	
if __name__ == "__main__":
	main()

