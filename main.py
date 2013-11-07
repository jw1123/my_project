#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conversion import Conversion
from extraction import Extraction
from distance import Distance



if __name__ == "__main__":
    
    y = None
    
    while (y != "q"):
        
        message = "What do you want to do? File conversion (c), feature extraction (e) or distance calculation (d)? : "
        y = raw_input(message)
        
        if y == "c":
            c = Conversion()
        elif y == "e":
            e = Extraction()
        elif y == "d":
            d = Distance()
        elif y == "q":
            print "Goodbye!"
        else:
            print "There is no %r option, please try again." %(y)
