import math

def make_translate( x, y, z ):
    pass

def make_scale( x, y, z ):
    pass
    
def make_rotX( theta ):   
    pass

def make_rotY( theta ):
    pass

def make_rotZ( theta ):
    pass

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

def print_matrix( matrix ):
    for i in matrix:
        print i
    pass

def ident( matrix ):
    if not len(matrix)==len(matrix[0]):
        print "Not a square"
        return -1
    ctr=0
    for i in matrix:
        j=0
        while j<len(matrix):
            i[j]=0
            i[ctr]=1
            j+=1
        ctr+=1
            
    pass

def scalar_mult( matrix, x ):
    for i in range(len(matrix)):
        for j in range (len(matrix[0])):
            matrix[i][j]*=x
    pass

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    pass

