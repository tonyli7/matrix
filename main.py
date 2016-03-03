from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
"""
mat=new_matrix()
print_matrix( mat)
ident(mat)
print_matrix( mat)
scalar_mult(mat, 3)
print_matrix( mat)

m1=new_matrix(3,2)
m2=new_matrix(2,3)
m1=[[1,2,3], [4,5,6], [7,8,9]]
m2=[[10,40,20],[20,50,30],[30,60,40]]
print "m1"
print_matrix(m1)
print "m2"
print_matrix(m2)
print "m1*m2"
print_matrix( matrix_mult(m1,m2))
print_matrix(make_translate(1,2,3))
print_matrix(make_scale(3,2,1))

m1=[[1,2,3,4], [4,5,6,7], [7,8,9,10],[1,1,1,1]]
rotZ=make_rotZ(360)
print_matrix(matrix_mult(rotZ,m1))
add_edge(m1,5,8,11,6,9,12)
print_matrix(m1)
"""
m=[
    [0,100],
    [0,0],
    [0,0],
    [1,1]
]

add_edge(m, 100,0,0,100,100,0)
add_edge(m, 100,100,0,0,100,0)
add_edge(m, 0,100,0,0,0,0)

rotZ45=make_rotZ(45)
T100100=make_translate(100,100,0)


fm=matrix_mult(rotZ45,m)
print_matrix(fm)
#fm=matrix_mult(T100100,fm)
draw_lines(fm,screen,color)

display(screen)
