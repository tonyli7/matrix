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
    if not len(m1) == len(m2[0]):
        print "Error: length of matrix-1 does not match height of matrix-2\n"
        return -1
    new=new_matrix(len(m1),len(m2[0]))
    ctr=0
   
    for i in range(len(m1)):
        t=0
        while t < len(m1):
            for j in range(len(m2)):
                new[ctr][t]+=m1[i][j]*m2[j][t]
                #print str(m1[i][j])+" * "+str(m2[j][t]) , ctr, t
            t+=1
        ctr+=1
    return new
    pass

