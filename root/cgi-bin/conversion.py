import socket
import os
import re

request = u'POST /webservicesserver/numberconversion.wso HTTP/1.1\r\n\
Host: www.dataaccess.com\n\
Content-Type: text/xml; charset=utf-8\n\
Content-Length: {}\n'

body = u'\n\
<?xml version="1.0" encoding="utf-8"?>\n\
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">\n\
<soap:Body>\r\n\
<NumberToWords xmlns="http://www.dataaccess.com/webservicesserver/">\n\
<ubiNum>{}</ubiNum>\n\
</NumberToWords>\n\
</soap:Body>\n\
</soap:Envelope>'

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

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(("52.4.66.53", 80))
socket.send(request.format(len(body)) + body.format(variables_envi["ubiNum"]))

while True:
    msg = socket.recv(1024)
    if len(msg) != 0:
        m = re.search("<m:NumberToWordsResult>([^<]*)</m:NumberToWordsResult>", msg)
        open("tmp", "w").write(web.format("Your number is : %s !!!" % m.group(0)))
        break

print "Close"
socket.close()