from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

mat=new_matrix()
print_matrix( mat)
ident(mat)
print_matrix( mat)
scalar_mult(mat, 3)
print_matrix( mat)
m1=new_matrix(3,2)
m2=new_matrix(2,3)
m1=[[1,2,3], [4,5,6]]
m2=[[10,40],[20,50],[30,60]]
print_matrix( matrix_mult(m1,m2))

display(screen)
