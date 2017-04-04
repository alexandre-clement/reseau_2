#!/usr/bin/python

import sys
import os

web = "<!DOCTYPE html><HTML>\
       <HEAD>\
       <TITLE>Doc. Produit par un CGI</TITLE>\
       </HEAD>\
       <BODY>\
       <H1>{}\
       !<H1>\
       </BODY>\
       </HTML>"

variables_envi = {key: value for (key, value) in [arg.split("=") for arg in os.environ["QUERY_STRING"].split("&")]}

open("tmp", "w").write(web.format("Welcome %s !" % variables_envi["pseudo"]))