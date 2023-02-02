class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        LENGTH = len ( words );
        precedence = defaultdict( int );
        
        for i in range( len ( order ) ):
            char = order [ i ];
            precedence [ char ] = i;
            
        for i in range( 1, LENGTH ):
            if not self.validOrder( words[ i - 1 ], words[ i ], precedence ):
                return False;
            
        return True;
        
    def validOrder( self, first, second, order ):
        
        first_length = len ( first );
        second_length = len ( second );
        
        for i in range( min ( first_length, second_length ) ):
            first_letter = first[ i ];
            second_letter = second[ i ];
            
            first_order = order[ first_letter ];
            second_order = order[ second_letter ];
            
            if first_order < second_order:
                return True;
            elif first_order == second_order:
                continue;
            else:
                return False;
        
        if first_length > second_length:
            return False;
        else:
            return True;