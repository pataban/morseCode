from Signal import *

class EncodingChart():
    def __class_getitem__(cls,key):
        if key.islower():
            key=key.upper()
        if(key=="A"):    return [Signal.DOT,Signal.DASH]
        if(key=="B"):    return [Signal.DASH,Signal.DOT,Signal.DOT,Signal.DOT]
        if(key=="C"):    return [Signal.DASH,Signal.DOT,Signal.DASH,Signal.DOT]
        if(key=="D"):    return [Signal.DASH,Signal.DOT,Signal.DOT]
        if(key=="E"):    return [Signal.DOT]
        if(key=="F"):    return [Signal.DOT,Signal.DOT,Signal.DASH,Signal.DOT]
        if(key=="G"):    return [Signal.DASH,Signal.DASH,Signal.DOT]
        if(key=="H"):    return [Signal.DOT,Signal.DOT,Signal.DOT,Signal.DOT]
        if(key=="I"):    return [Signal.DOT,Signal.DOT]
        if(key=="J"):    return [Signal.DOT,Signal.DASH,Signal.DASH,Signal.DASH]
        if(key=="K"):    return [Signal.DASH,Signal.DOT,Signal.DASH]
        if(key=="L"):    return [Signal.DOT,Signal.DASH,Signal.DOT,Signal.DOT]
        if(key=="M"):    return [Signal.DASH,Signal.DASH]
        if(key=="N"):    return [Signal.DASH,Signal.DOT]
        if(key=="O"):    return [Signal.DASH,Signal.DASH,Signal.DASH]
        if(key=="P"):    return [Signal.DOT,Signal.DASH,Signal.DASH,Signal.DOT]
        if(key=="Q"):    return [Signal.DASH,Signal.DASH,Signal.DOT,Signal.DASH]
        if(key=="R"):    return [Signal.DOT,Signal.DASH,Signal.DOT]
        if(key=="S"):    return [Signal.DOT,Signal.DOT,Signal.DOT]
        if(key=="T"):    return [Signal.DASH]
        if(key=="U"):    return [Signal.DOT,Signal.DOT,Signal.DASH]
        if(key=="V"):    return [Signal.DOT,Signal.DOT,Signal.DOT,Signal.DASH]
        if(key=="W"):    return [Signal.DOT,Signal.DASH,Signal.DASH]
        if(key=="X"):    return [Signal.DASH,Signal.DOT,Signal.DOT,Signal.DASH]
        if(key=="Y"):    return [Signal.DASH,Signal.DOT,Signal.DASH,Signal.DASH]
        if(key=="Z"):    return [Signal.DASH,Signal.DASH,Signal.DOT,Signal.DOT]
        
    
