def multiplicateur(*args):
    result = 1
    for val in args:
        result *= val 
    return result
    
def maximum(*args):
    maxi = args[1]
    for val in args:
        if val >= maxi:
            maxi = val
    return maxi
    
    
def fun(a, b, c, d): 
    print(a, b, c, d)
my_list = [1, 2, 3, 4] 
fun(*my_list)


def liste_ch(*arg):
    liste = None
    for val in reversed(arg):
        liste = (val, liste) 
    return liste

def queue(lst):
    queue_lst = None
    for i in range(1, len(lst)):
        queue_lst = (val, queue_lst)

def tete(lst):
    return lst[0]

def ajouter(lst, ajout):
    for element in lst:
        if element is None:
            element = ajout
    return lst

def element_n(lst, num):
    val = lst[0]
    while num > 0 and lst is not None:
        val = lst[1]
        num -= 1

def renverser(lst):
    nouvelle_lst = None
    for val in lst:
        nouvelle_lst = (val, lst)
    
def longueur(lst):
    l = 0
    for element in lst:
        if element is None:
            return l
        else:
            l += 1
    
maliste = liste_ch(2, 8, 3, 5, 4)
print(longueur(maliste))




