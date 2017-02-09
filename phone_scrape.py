
# Scrape IP Phone Web Page at given IP address and return a dictionary with all of the information
# listed in phone_info_headers

import sys
import urllib.request
from bs4 import BeautifulSoup


# 7841
phoneIP = '10.88.72.84'

# 8851
phoneIP = '10.88.72.77'

# 7971
#phoneIP = '10.99.62.36'

#with open('iplist.txt', 'r') as f:
#    iplist = [line.strip() for line in f]
#    iplist = f.read().splitlines()

#print (iplist)
#print (type(iplist))
#print (len(iplist))

# http://10.88.72.84/CGI/Java/Serviceability?adapter=device.statistics.device

def get_phone_info(phoneIP):

    #list of phone information that will be gleaned from web page
    phone_info_headers = ['MAC Address', 'Host Name', 'Phone DN', 'App Load ID', 'Boot Load ID', 'Version',
                  'Expansion Module 1','Expansion Module 2', 'Hardware Revision','Serial Number','Model Number',
                  'Message Waiting', 'UDI']
    
    phone_info = {}

    url = 'http://' + phoneIP + '/CGI/Java/Serviceability?adapter=device.statistics.device'
    print (url)

    fhand = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(fhand, "html.parser")


    table_data = [[cell.text.strip() for cell in row("td")]
                             for row in soup("tr")]

    for row in table_data:

        if row[0].upper() in [x.upper() for x in phone_info_headers]:
            phone_info[row[0]] = row[2]

    return phone_info;


print(get_phone_info(phoneIP))



