#!/usr/bin/python
import sys

post = dict(item for item in [arg.split("=") for arg in sys.stdin.read().split("&")])

web_page = """<!DOCTYPE html><HTML>
       <HEAD>
       <TITLE>Doc. Produit par un CGI</TITLE>
       </HEAD>
       <BODY>
       <H1>{}<H1>
       <p>{}<p>
       </BODY>
       </HTML>"""

print web_page.format("POST : %s" % post["message"], "By %s" % post["author"])

