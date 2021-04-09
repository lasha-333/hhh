car = {
    'model' : 'bmw',
    'mark' : 'g-class',
    "year": 2002}
car['year']= 2198 # mniSvnelobis gadaniWeba
car['fueltype'] = 'rompetrol' # elementis damateba

print(len(car ))
print(car.get('mark'))
print(car["mark"] ) # dabewdavs g class print(car.get(mark)) ერთი და იგივეა
print(car)
for key, value in car.items():
 print(key, value)


fruit={}        # დიქშენარი, დიქშშენარში ერთ ქეის შეესაბამე ერთი უნიკალური ვალიუ ანი ღირებულება
while True :
    if len(fruit)==0:   # სანამ ფრუიტის სიგრძე ნულია ანუ {} ცარიელი
        helper = {} # ახალი დიქშენარი
        name = input("enter friut name: ")
        kg= input("enter fruit weight :")
        price= input('enter price')
        helper["kg"]= kg   # ამ დიქშენარში შეინახოს კგ და ფასი
        helper['price']= price
        fruit[name]= helper # ამ დიქშენარიში  დაამატოს ქეი რომლის ვალიუ იქნება  ჰელპერ დიქშენარი
    else:
        print('this is your cart', fruit) # დაწეროს ,'', და ფრიუტ დიქშენარი
        question= input("add more? yes or no : ")
        if question== 'yes' : # აქ კეთდება უკვე ციკლი
            helper={}
            name = input("enter friut name: ")
            kg = input("enter fruit weight :")
            price= input(' sheitane Tanxa :')
            helper["kg"] = kg
            helper['price'] = price

            fruit[name] = helper
        else:
            break
    for f, s in fruit.items():  # fruit.items() თითოულ შემადგენელ ელემენტ ამოირებს ქეის და ვალუეს key sheitans keshi da values valueshi shecval SeiZlebamogvca apllee value mogvca 'kg': '12', 'price': '3'}
        kg= int(s['kg'])   # gvaintot
        price = int(s['price']) # გავაინტეჯეროთ რათა გადავამრავლოთ
        print(f, s ) # dabeWdavs fruit dicsheneris keys da values
        print('tqveni gadasaxadia' , kg*price)
#print('this is your cart', fruit, 'naxvamdis')
