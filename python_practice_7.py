# Assuming that we have some email addresses in the "username@companyname.com"
# format, write a program to print the company name of a given email address. Both user
# names and company names are composed of letters only.

import re

txt = "username@companyname.com"
x = re.search("(?<=@)\w*(?=.)", txt)

if (x):
  print("Company Name : ",x.group())
else:
  print("No match")


