import sys

with open(sys.argv[1], "r+") as file:
	old = file.read()
	file.seek(0)
	file.truncate()
	file.write(old.replace("align=middle", "align=\"middle\"").replace("width=\"", "width=").replace("width=", "width=\"").replace("pt height=", "pt\" height=\"").replace("pt/>", "pt\"/>"))
