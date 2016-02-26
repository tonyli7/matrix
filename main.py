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
display(screen)
