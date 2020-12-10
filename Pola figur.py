import math
def circle(r):
    if r>0:
        return(4*math.pi*math.pow(r,2))
    else:
        print("Podano nie poprawny promień koła")
def triangle(a,h):
    if a>0 and h>0:
        return(a*h*0.5)
    else:
        print("Któryś z podanych wymiarów jest równy 0 lub mniejszy od 0")
def rectangle(a,b):
    if a>0 and b>0:
        return(a*b)
    else:
        print("Któryś z podanych wymiarów jest równy 0 lub mniejszy od 0")
figura=["koło","trójkąt", "prostokąt"]
print(figura)
f=input("Wybiesz figurę z powyższej listy, której chcesz obliczyć pole. Jeśli chcesz obliczyć pole koła to wpisz 1, jeśli pole trójkąta to wpisz 2, jeśli pole prostokąta to wpisz 3\n ")
if not f.isnumeric():
    print("Nie poprawnie wybrano figurę")
else:
    f=float(f)
    if f==1:
        r=input("Podaj promień koła: ")
        if not r.isnumeric():
            print("Błędnie podano wymiar! ")
        else:
            r=float(r)
            print("Pole figury %s o podanych wartościach wynosi %.2f " %(figura[0],circle(r)))
    elif f==2:
        a=input("Podaj długośc podstawy trójkąta: ")
        h=input("Podaj wysokość trójkąta: ")
        if not a.isnumeric() and h.isnumeric():
            print("Błędnie podano wymiary! ")
        else:
            a=float(a)
            h=float(h)
            print("Pole figury %s o podanych wartościach wynosi %.2f " %(figura[1],triangle(a,h)))
    elif f==3:
        b=input("Podaj długość jednego boku prostokata: ")
        c=input("Podaj długość drugiego boku trójkąta: ")
        if not b.isnumeric() and c.isnumeric():
            print("Błędnie podano wymiary! ")
        else:
            b=float(b)
            c=float(c)
            print("Pole figury %s o podanych wartościach wynosi %.2f " %(figura[2],rectangle(b,c)))
    else:
        print("Wpisano niepoprawną cyfrę! ")

