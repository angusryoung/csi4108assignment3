from Crypto.Util.number import *
import Crypto


#256 prime -> 491 
p = 491
# find a and b
a,b = 1,1

#base point
x= 0
y=1

print("the order of E491(1,1) with generator (0,1) is 252 out of 504 possible points")
print("h is 2 which meets h< 4 criteria")



#y2
# y^2 mod p = (x^3 + ax + b) mod p
#let x = 3, y=6

# rightside = ((x**3) + (x*a) + b) % 491
# leftside = ((y**2)%491)
# print( "right side = "+ str(rightside))
# print("left side = "+ str(leftside))


def check_point_on_curve(x,y,ca,cb,m):
    rightside = ((x**3) + (ca*x) + cb) % m
    leftside = ((y**2)%m)
    print( "right side = "+ str(rightside))
    print("left side = "+ str(leftside))

def point_addition(x1,y1,x2,y2,m):
    dy = y2 -y1 
    dx = x2 -x1
    # print (dy)
    # print(dx)

    if (dy < 0):
        dy = dy% m
    dx = Crypto.Util.number.inverse(dx,m)

    delta = (dx*dy)%m

    if ((x1,y1) == (x2,y2)):
        delta = (3 * x1**2 + a) * Crypto.Util.number.inverse(2 * y1,m)
    
    newx = ((delta**2)-x1-x2)% m
    newy = ((delta*(x1-newx))-y1 )%m

    return newx,newy

def point_multiplication(num , x1,y1, m):
    a, b = x1 , y1
    for i in range(num-1):
        a, b = point_addition(a,b,x1,y1,m)
        # print(a,b)
    return a,b


#alice choose na < n , compute Pa = na G
#na is private value
#Pa is public value

#lets say Alice chooses 69 as na
# na = 69
na = 69
Pax , Pay = point_multiplication(na, 0,1,p)
# print(Pax , Pay)

#Lets say Bob chooses 169 as nb
nb = 25
Pbx, Pby = point_multiplication(nb, 0,1,p)
# print(Pbx , Pby)

#Alice computes na * Pb
Key1 = point_multiplication(na, Pbx,Pby,p)

#Bob computes nb * Pa
Key2 =  point_multiplication(nb, Pax,Pay,p)

print ("as you can see Alice and bob both got the same value")
print(Key1 , Key2)

# print(point_addition(72,120,72,120,p))