#!/usr/bin/python
import os

get = dict(item for item in [arg.split("=") for arg in os.environ["QUERY_STRING"].split("&")])

web_page = """<!DOCTYPE html><HTML>
       <HEAD>
       <TITLE>Doc. Produit par un CGI</TITLE>
       </HEAD>
       <BODY>
       <H1>{}<H1>
       <p>{}<p>
       </BODY>
       </HTML>"""

print web_page.format("GET : %s" % get["message"], "By %s" % get["author"])
