class Vertex:
    #Lightweight vertex structure for a graph.”””
    __slots__ = '_element'
    
    def __init__(self,x):
        self._element = x
        
    def element(self):
        return self._element
    
    def __hash__(self):
        return hash(id(self))

class Edge:
    __slots__ = '_origin','_destination','_element'
    
    def __init__(self,u,v,x):
        self._origin = u
        self._destination = v
        self._element = x
    
    def opposite(self,v): #”””Return the vertex that is opposite v on this edge.””
        return self._destination if v is self._origin else  self._origin
    
    def element(self,x):
        return self._element
    
    def hash(self):
        return hash(self._origin,self._destination) # will allow edge to be a map/set key