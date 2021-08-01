import collections

print collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
print collections.Counter({'a':2, 'b':3, 'c':1})
print collections.Counter(a=2, b=3, c=1)

class Solution:
    def __init__(self,names):
        self.names = names
    
    def __hash__(self):
        return hash(frozenset(self.names))
    
    def __other__(self,other):
        return set(self.names) == set(other.names)
    
def intersect_two_sorted_arrays(A, B):
def is_present(k):
    i = bisect.



