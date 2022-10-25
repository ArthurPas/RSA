from email import message
def expmod(a,e,n):
    result = 1
    while(e!=0):
        if (e%2!=0):
            result = (result*a)%n
        a = (a**2)%n
        e = e//2
    return result

def test_premier(n):
    if ( (expmod(2,n-1,n)==1) and
    (expmod(3,n-1,n)==1) and
    (expmod(5,n-1,n)==1) and
    (expmod(7,n-1,n)==1) and
    (expmod(11,n-1,n)==1) and
    (expmod(13,n-1,n)==1) ):
        return True; 
    return False

def pgcd( u, v):
    while (v):
        t = u
        u = v
        v = t % v
    if u<0:
        return -u 
    else:
        return u

def bezout(a,b):
    if (a,b) == (1,0):
        return 1,0
    else:
        (l1,l2) = bezout(b,a%b)
        return l2,l1-(a//b)*l2

def genere_cle(p,q):
    phi = (p-1)*(q-1)
    e = 967
    while(pgcd(e,phi)!=1):
        e=e+1
    d = bezout(phi,e)[1]
    while(d<2):
        d=d+phi
    return e,d

def chiffrer(m,e,n):
    return expmod(m,e,n)

def dechiffrer(c,d,n):
    return expmod(c,d,n)

def creerEmpreinte(message, taille):
    empreinte= message << 1
    return empreinte % taille

def concatMessageEmpreinte(message, empreinte,taille):
    return (message * taille) + empreinte