#1
tup=("Pizza","Burger","Lasagne","Biryani","Tacos")
print("-----MENU----")
for food in tup:
    print(food)
lst=list(tup)
lst[2]="Pizza Fries"
lst[3]="Mayo Roll"
tuple=tuple(lst)
print("---NEW MENU---")
for food in tuple:
    print(food)




#2
dic={"Pakistan":"islamabad","Japan":"tokyo","India":"new dehli"}
count=0
for key,value in dic.items():
    Q=input(f"guess the capital of {key} ")
    if Q==value:
        print("Correct")
        count+=1
    else:
        print("Incorrect")
print("coreect answers:",count)





#3
fav_places={
            "Alishba":("Hunza","Swat","Quetta"),
            "Sana":("Paris","Miracle Garden","Oman"),
            "Alia":("Holland","Switzerland","Norway")
            }
for key,value in fav_places.items():
    print(key,"likes the following places:")
    print(value[0])
    print(value[1])
    print(value[2])
    print("----------------")




    

#or
fav_places={
            "Alishba":("Hunza","Swat","Quetta"),
            "Sana":("Paris","Miracle Garden","Oman"),
            "Alia":("Holland","Switzerland","Norway")
            }
for key,value in fav_places.items():
    print(key,"likes the following places:")
    for places in value:
        print(places)
    print("----------------")