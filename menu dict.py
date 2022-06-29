from menu_class import gerecht
vg = gerecht("Tomatensoep","Huisgemaakte tomatensoep met verse groenten",5)
hg = gerecht("Steak","Steak met frietjes/kroketten/pasta",22)
hg2 = gerecht("Ribbetjes","Ribbetjes met frietjes/kroketten/pasta",21)
dessert = gerecht("tiramisu","Huisgemaakte tiramisu",8)

menu = {"Voorgerecht":vg,"Hoofdgerecht":hg,"Dessert":dessert}
menu2 = {"Voorgerecht":vg,"Hoofdgerecht":hg2,"Dessert":dessert}
lijst_menus = [menu,menu2]

def toon_menu(menu:dict):
    for k,v in menu.items():
        print(k,v)

for x in lijst_menus:
    print("********Menu********")
    toon_menu(x)
    print("-----------------------------------------------")


