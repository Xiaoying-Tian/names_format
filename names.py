"""
names.py
Date: 2013-12-20
Author: Xiaoying Tian
"""

from __future__ import division
import sys
import re
import doctest

'''
To Do: Add attributes like gender and race to the object
'''

prefix = {'Ms':'Adult female', 'Miss':'Unmarried female', 'Mr':'Adult male',
        'Ms.':'Adult female', 'Mr.':'Adult male', 'Mrs.':'Married female', 
        'Mrs': 'Married female', 'Master':'Male child', 'Rev.':'Reverend', 
        'Fr.':'Father', 'Dr.':'Doctor', 'Atty.':'Attorney', 'Prof.':'Professor',
        'Hon.':'Honorable', 'Pres.':'President', 'Gov.':'Governor', 'Sen.':'Senator',
        'Rep.':'Representative', 'Amb.':'Ambassador', 'Treas.':'Treasurer',
        'Sec.':'Secretary', 'Pvt.':'Private', 'Cpl.':'Corporal', 'Sgt.':'Sargent',
        'Adm.':'Administrative', 'Maj.':'Major', 'Capt.':'Captain', 'Cmdr.':'Commander',
        'Lt.':'Lieutenant', 'Lt Col.':'Lieutenant Colonel', 'Col.':'Colonel',
        'Gen.':'General'} 

suffix = {'PhD':'PhD', 'Ph.D.':'PhD', 'JD.':'JD', 'MD.':'MD',
        'J.D.':'JD', 'M.D.':'MD', 'JD':'JD', 'MD':'MD', 'Jr':'Junior', 
        'Sr':'Senior', 'BA':'BA', 'B.A.':'BA', 'MBA':'MBA', 
        'M.B.A':'MBA', 'BS':'BS', 'B.S.':'BS',
        'MA':'MA', 'M.A.':'MA', 'MS':'MS', 'M.S.':'MS'}


class names():
    """
    Use like this:

    >>> from names import names
    >>> xiaoying = names("Xiaoying Tian")
    >>> xiaoying.name["first_name"] == "Xiaoying"
    True

    """
    def __init__(self, namestr):
        self.name = {}
        self.prefix  = []
        self.suffix = []
        #strip the name string of the prefix and the suffix
        tokens = re.split('\s+', namestr)        
        for token in tokens:
            if token.strip(',') in prefix:
                namestr = re.sub(token, '', namestr)
                self.prefix.append(prefix[token.strip(',')])
                print 'here'
            elif token.strip(',') in suffix:
                namestr = re.sub(token, '', namestr)
                self.suffix.append(suffix[token.strip(',')])
                print 'here'
        m = re.match(r'[ ]*(\w(?:\.|\w+))?[ ]*(,)?[ ]*(\w(?:\.|\w+)[ ]+)*(\w(?:\.|\w+))',namestr)
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
                self.name['first_name'] = names[0]
                if len(names) == 2:
                    self.name['last_name'] = names[1]
                elif len(names) == 3:
                    self.name['middle_name'] = names[1]
                    self.name['last_name'] = names[2]
        else:
            raise ValueError('Could not parse')

         


    def __str__(self):
        return("First name: " + self.name['first_name'] + '\n'
            + "Last name: " + self.name['last_name'])

def main():
    """
    xiaoying = names('Miss X.     Tian, Ph.D., J.D.')
    print xiaoying
    print xiaoying.prefix
    print xiaoying.suffix
    """


if __name__ == "__main__":
    doctest.testmod()
    main()
