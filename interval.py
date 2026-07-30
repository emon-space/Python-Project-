# interval.py

class Interval:
    """ A class to represent intervals of real numbers.

        attributes:
        - inf, sup: the endpoints of the interval;
                    the object represents the numbers X = {x | inf <= x <= sup}

        methods:
        - merge(): the union of intervals
        - subtract(): the set difference of intervals
        - includes(): point inclusion
        - is_empty(): test if the interval is empty
        - load(): execute operations listed in a text file
                  in the following format:
                    creation:       "C <inf> <sup>"
                    merge:          "M <inf> <sup>"
                    subtract:       "S <inf> <sup>"
                    inclusion test: "I <number>"
                    emptiness test: "E"
    """

    def __init__(self, inf=None, sup=None, filename=None):
        """
        Initialize an Interval.
        - inf and sup: the endpoints of the interval.
        - filename: path of a text file with the list of the
                    operations (see load() docstring for the format)
        The parameters are evaluated in this sequence:
          - first, inf and sup are assigned (as float), if not None;
          - then, filename (if any) is read and the instructions are executed;
            if inf and sup are None, the first instruction must be
            an initialization ('C' command).
        """
        pass
    
    def __str__(self):
        """
        Textual description of Interval.
        Interval(a, b) should be printed as '[a, b]'.
        An empty set is printed '[]'.
        """
        pass
    
    def merge(self, other):
        """
            Add the points of other that extend the given interval.
            other can be an Interval or a sequence of two numbers.
        """
        pass
    
    def subtract(self, other):
        """
            Remove the points of other that overlap the given interval.
            other can be an Interval or a sequence of two numbers.
            As a special case, the endpoints of a set to be subtracted
            are preserved in the resulting interval.
        """
        pass

    def includes(self, x):
        """
            Returns True if x is in the given interval.
        """
        pass

    def is_empty(self):
        """
            Returns True if the interval is empty (i.e., if sup > inf)
        """
        # Note: also the None cases for inf and sup should be checked 
        pass

    def load(self, fin):
        """
            Read the instruction to manipulate the Interval from fin.
            fin: text file with the manipulation instructions
                    in the following format:
                    - one instruction per line
                    creation:       "C <inf> <sup>"
                    merge:          "M <inf> <sup>"
                    subtract:       "S <inf> <sup>"
                    inclusion test: "I <number>"
                    emptiness test: "E"
                    
            After the execution of each instruction, the current status
            is printed:
            - creation, merge, and subtraction: print the current Interval
            - inclusion and emptiness: print the value of the test  
        """
        pass
        
###  TEST
if __name__ == '__main__':
    if True:
        #t = Interval(filename='interval_test1.txt')
        t = Interval(filename='interval_test2.txt')
        #t = Interval(filename='interval_test3.txt')
    else:
        t = Interval(3, 5)
        print(t)
        t.merge([4, 7])
        print(t)
        t.merge([8 , 9])
        print(t)
        t.merge([1 , 9])
        print(t)
        t.subtract([0, 5])
        print(t)
        t.subtract([8, 9])
        print(t)
        t.subtract([6, 7])
        print(t)
        print(t.includes(3))
        print(t.includes(6))
        t.subtract([3, 9])
        print(t)
    
    
