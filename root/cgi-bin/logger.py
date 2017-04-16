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

tmp = open("tmp").read()
variables_envi = {key: value for (key, value) in [arg.split("=") for arg in tmp.split("&")]}

open("tmp", "w").write(web.format("Welcome %s !" % variables_envi["pseudo"]))