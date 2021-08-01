class MapBase:
    
    class _item:
        #Lightweight composite to store key-value pairs as map items.”””
        __slots__ = '_key','_value'
        
        def __init__(self,k,v):
            self._key = k
            self._value = v
        
        def __eq__(self,other):
            return self._key == other._key
        
        def __ne__(self,other):
            return not (self._key == other)
        
        def __it__(self,other):
            return self._key < other._key
        
class unsortedTableMap(MapBase):
    def __init__(self):
        self._table = []
    
    def __getItem__(self,k):
        for item in self._table:
            if k == MapBase._item._key:
                return MapBase._item._value
        raise KeyError('Keyerror: ')
    
    def __setItem__(self,k,v):
        for item in self._table:
            if k == MapBase._item._key: # Found a match:
                item._value = v # reassign value
                return      # and quit
        self._table.append(self._item(k,v)) # did not find match for key
        
    def __delitem__(self,k):
        for j in range(len(self._table)):
            if k == self._table[j]:
                self._table.pop[j]
                return
        raise KeyError("Key eeror")
    
    def __len__(self):
        return len(self._table)
    
    def __iter__(self):
        for item in self._table:
            yield MapBase._item._key