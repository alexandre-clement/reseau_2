#!/usr/bin/python

import sys
import os

variables_args = {key: value for (key, value) in [arg.split("=") for arg in sys.argv[1:]]}
variables_envi = {key: value for (key, value) in [arg.split("=") for arg in os.environ["QUERY_STRING"].split("&")]}

web = "<!DOCTYPE html><HTML>\
       <HEAD>\
       <TITLE>Doc. Produit par un CGI</TITLE>\
       </HEAD>\
       <BODY>\
       <H1>{}\
       !<H1>\
       </BODY>\
       </HTML>"

open("tmp", "w").write(web.format("incr : %s" % variables_args["val"]))