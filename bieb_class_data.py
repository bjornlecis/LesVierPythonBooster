from persoon_class import persoon
from boek_class import boek
from uitlening_class import uitlening

p = persoon("p1","Bart","M")
p2 = persoon("p2","Marleen","V")
p3 = persoon("p3","Veerle","V")

b = boek("b1","Boek 1","a1")
b2 = boek("b2","Boek 2","a2")
b3 = boek("b3","Boek 3","a1")

u = uitlening("u1",b,p)
u2 = uitlening("u2",b3,p2)
u3 = uitlening("u3",b,p2)
u4 = uitlening("u4",b2,p3)
u5 = uitlening("u6",b2,p)

lijst_personen = [p,p2,p3]
lijst_boeken = [b,b2,b3]
lijst_uitleningen = [u,u2,u3,u4,u5]

