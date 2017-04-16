#!/usr/bin/python
import sys
import os


if "QUERY_STRING" in os.environ:
    method = "GET"
    var = dict(item for item in [arg.split("=") for arg in os.environ["QUERY_STRING"].split("&")])
else:
    method = "POST"
    var = dict(item for item in [arg.split("=") for arg in sys.stdin.read().split("&")])

web_page = """<!DOCTYPE html><HTML>
       <HEAD>
       <TITLE>Doc. Produit par un CGI</TITLE>
       </HEAD>
       <BODY>
       <H1>{}<H1>
       <p>{}<p>
       </BODY>
       </HTML>"""

print web_page.format("%s : %s" % (method, var["message"]), "By %s" % var["author"])