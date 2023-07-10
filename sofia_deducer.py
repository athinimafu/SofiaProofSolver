import sys


class LogicalStructure:
    opening     = '['
    closing     = ']'
    implication = ':'
    
    def __init__(self):
        self.assumptions = {} # hash map containing the assumption block number as key and [ assumption,(index of implication) ] 
        self.conclusions = {} # hash map containing the conclusion block number as key and [ conclusion ]  
       
    def get_block(self,theorem,start,end):
        if start < 0:
            print("theorem incorrect: missing  '[' ")
            return
        if end > len(theorem):
            print("theorem incorrect: missing   ']'")
            return

    def extract(self,theorem):
        block = 0
        start = 0
        prev_start = 0
        for i  in range(0,len(theorem)):
            ch = theorem[i]
        
            if ch == self.opening:
                if start != -1:
                    block += 1
                start = i 
                
            elif ch == self.closing:
                if block in self.assumptions:
                    concl_start  = self.assumptions[block][1]
                    self.conclusions[block] = theorem[concl_start+1:i+1]
                if start == -1:
                    block -= 1
                else:
                    prev_start = start
                start = -1

            elif ch == self.implication:

                self.assumptions[block] = [theorem[prev_start:i],i]


                
    def print_assumptions_and_conclusions(self):
        for block in self.assumptions:
            print("assumption: ",block," : ",self.assumptions[block])
        for block in self.conclusions:
            print("conclusion: ",block," : ",self.conclusions[block])


if __name__ == '__main__':
    lg = LogicalStructure()
    theorem = sys.argv[1]
    print("Theorem: ",theorem)
    lg.extract(theorem)
    lg.print_assumptions_and_conclusions()




