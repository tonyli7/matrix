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
square=[
    [0,50],
    [0,0],
    [0,0],
    [1,1]
]

add_edge(square, 50,0,0,50,50,0)
add_edge(square, 50,50,0,0,50,0)
add_edge(square, 0,50,0,0,0,0)

square=matrix_mult(make_translate(200,200,0),square)


for i in range(360):
    square=scalar_mult(matrix_mult(make_rotZ(i),square),.99)
    draw_lines(square,screen,[i%255,(i*i)%255,(i+i)%255])

triangle=[
    [450,410],
    [0,70],
    [0,0],
    [1,1]
]
add_edge(triangle,410,70,0,490,70,0)
add_edge(triangle,490,70,0,450,0,0)

for i in range(360)[::-1]:
    triangle=scalar_mult(matrix_mult(make_rotZ(i),triangle),.99)
    draw_lines(triangle,screen,[(-1*i)%255,(i*i)%255,(-(i+i))%255])
    
display(screen)
