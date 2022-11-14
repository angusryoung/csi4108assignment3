import random
from math import pow



def get_k_and_q(n):
    n_minus = n-1
    k = 0
    while(n_minus%2 ==0):
        n_minus /= 2
        k+=1
    q = n_minus
    #by default q is type float. it need to be in type int to avoid errors in calculation
    return int(q),int(k)


def test(n,t):
    #Find integers k, q, with k> 0 , q odd, so that (n-1 = (2^k)*q);
    
    #k > 0
    #q needs to be odd
    q,k = get_k_and_q(n)
    # print("q is :"+ str(q))
    # print("k is :" + str(k))
    if (k<1):
        # print("k too small")
        return False
    if (q%2 == 0):
        # print("q not odd")
        return False

    status = "composite"
    
    for i in range(t):
        # print(i)
        
        a = random.randint(1, n-1)
        # print("random int: " +str(a))
        #if (a^q)mod n = 1 return incinclusive 
        # print("a: "+str(a))
        # print("q: "+str(q))
        big1 = a**q
        if (big1%n == 1):

            status = "inconlusive"
        for j in range(k-1):
            if ((a**(q*(2**j)))%n== n-1):
                status = "inconlusive"
    if (status == "composite"):
        return False
    return True





 
# Driver code
def main():
    start = 8192 # 2^13
    end = 16383  # 2^14-1
    
    #choose a number between the start and end as that is a 14 bit integer
    #n = random.randint(start, end)
    # test with a known prime n= 9239
    current_n = 8192
    #current_n = 9239
    while current_n < 16393:
    #while current_n < 9240:
        #print(current_n)

        # print("the chosen random int is "+ str(n))

        isvalid = test(current_n,5)
        if (isvalid):
            print (str(current_n) + " is a probable prime")
            break
        # else:
        #     print (str(n) + " is not a probable prime")
        current_n+=1

 
if __name__ == '__main__':
    main()