from enum import Enum

class Signal(Enum):
    DOT = 1
    DASH = 3

    def __str__(self):
        if self.value==1:
            return 'Dot'
        return 'Dash'
    
    