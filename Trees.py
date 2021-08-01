class Tree:
    """Abstract base class representing a tree structure"""
    class Position:
        """An abstraction representing the location of a single element"""
        def element(self):
            #Return the element stored at the position
            raise NotImplementedError("Must be implemented by sub class")
        
        def __equal__(self,other):
            #return true if same as other position
            raise NotImplementedError("Must be implemented by sub class")
        
        def __Notequal__(self,other):
            #Return True if other does not represent the same location
            return not(self == other)
        #Abstract methods that concrete must support
        def root(self):
            #return position of of the root
            raise NotImplementedError("must be implemented by concrete class")
        def parent(self,p):
            #return position representing Parent position or or none of Parent is root
            raise NotImplementedError("Must be implemented by concrete class")
        def number_of_children(self,p):
            #return the number of children position P has
            raise NotImplementedError("Must be implemented by concrete class")
        def num_children(self,p):
            #return number of children position P has
            raise NotImplementedError("Must be implemented by concrete class")
        def children(self,p):
            #define an iteration representing the position of P's children
            raise NotImplementedError("Must be implemented by concrete class")
        def __len__(self):
            #return total number of elements in the tree
            raise NotImplementedError("Must be implemented by concrete class")
        #####concrete class
        
        def _is_root(self,p):
            #return true if p is the root
            return (self.root == p)
        def _is_leaf(self,p):
            #return true if P is the leaf
            return (self.num_children == 0)
        def _is_empty(self):
            #return true if tree is empty
            return len(self) == 0
        
        ##########################################
        
        def depth(self,p):
            #find depth of a tree
            if self._is_root:
                return 0
            else:
                return 1 + self.depth(parent(p))
        
        def _height1(self):
            return max(self.depth(p)) for p in self.positions() is self._is_leaf(p)
        def _height_2(self,p):
            if self._is_leaf(p):
                return 0
            else:
                return 1+ max(self._height_2(c)) for c in self.children(p)
          ##########################################
          #concrete methods
          
        
                    
        