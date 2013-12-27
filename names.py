"""
names.py
Date: 2013-12-20
Author: Xiaoying Tian
"""

from __future__ import division
import re

class names():
    def __init__(self, namestr):
        self.name = {}
        m = re.match(r'[ ]*(\w(?:\.|\w+))?[ ]*(,)?[ ]*(\w(?:\.|\w+)[ ]+)*(\w(?:\.|\w+))', namestr)
        if m:
            names = m.groups()
            #deals with the case 'lastname, firstname (middlename)'
            if ',' in names: 
                names = [name.strip() for name in list(names) if name != None and name != ',']
                self.name['last_name'] = names[0]
                self.name['first_name'] = names[1]
                if len(names) == 3:
                    self.name['middle_name'] = names[2]
            #deals with the case 'firstname (middlename) lastname'
            else:
                names = [name.strip() for name in list(names) if name != None]
                print(names)
                self.name['first_name'] = names[0]
                if len(names) == 2:
                    self.name['last_name'] = names[1]
                elif len(names) == 3:
                    self.name['middle_name'] = names[1]
                    self.name['last_name'] = names[2]

    ''' to do:
    handle single name (indicate first name) and
    single last name
    '''

    def __str__(self):
        return("First name: " + self.name['first_name'] + '\n'  
            + "Last name: " + self.name['last_name'])

def main():
    xiaoying = names(' Xiaoying     Tian')
#    m = re.match(r'[ ]*(\w+) (\w+)', 'Xiaoying Tian')
#    if m:
#        print(m.groups())

    print xiaoying
#    print(xiaoying.name)
    pass

if __name__ == "__main__":
    main()
