array = [3 , 4 ,2,2,2, 7777777  , 7 , 3]  # მასივებსაც გააჩნიატ ინექსაცია ნულიდან  და სულ ასეთ ფრიჩხილებშია
print(array)                   # მასივძში შეიძლება ჩაწერი სტრინგი  ინტი ათწილადი ტრუ ან ფალსე floats= 4,5 boolean= false an true
array.append(5)              # print(string.title) upper lower  დაწერს დიდ პირველ ასოს ან ყველას დიდი ასოებით
#array.insert(0, 20)

#array.insert(0,2)
print(array)
array.reverse()               # შეატრიალებს მასივს
print(array)                    #array.append(5)  დამატებს ბოლოში  array.insert(0, 20) დაამატებს მონაცემს 0 ინდექსზე
print(array.count(7))              #  dabewdavs ramdeni 7 nia masivShi
print(len(array))

print(array.index(3))          # gvibrunebs 3 romel indeqszea
array.pop(3) ##amowris am indeqsze mdgom elemnts
print(array)
array.sort()# dasortirebs
print(array)
array.remove(2)
print(array)            # მიცემ ობიექტს და ამიღებს ორიანებს yvelas unda igebdes mara aq ar qna
array[1]= 100 # 7 ჩარზე ინდექსე მდგომ ელემენტს შეცვლის შესსაბამისად
print(array)
for element in array: # arais elementebs Seitans elemntSi da dabeWdavs for element in range(len(array)):araishi elemntebis indeqsebs dawers
    print(element**2)

'''x= int(input("enter first number"))
y = int(input("enter secon number"))
if x==y :            # if x==y თუ ტოლია ისე თუ არაა ტოლი ასე== ლოგიკური ოპერატორი, ნიშნავს ან უდრის ან არ უდრის თუ უდრის მიბრუნებს ტრუს თუ არ უდრის ფალსე
 print("tolia")     #####ესეიგი ასე იკითხება თუ იქსი უდრის იგრეკს დაწერე ტოლია ელიფი ანუ სხვა ყველაშემტხვევაში იქსი ნაკლებია იგრეკზე მაშინ ეს დაწერე თუ
elif x<y :          ##### თუ ასეც არაა მაშინ არაა ტოლია დაწერე !!! ელიფის ნაცვალდ შეიძლება იფიც მაგრამ მას პროგრამა აღიქვამს ცალკე იფად ანუ შეამოწმებს თუ
                    # პიველი პირობა სრულდება მაინც ,ხ=ყს და შეამოწმებს კიდევ (if x==y if x<y : ამ შემთხვევაში ამოსმებს ორივეს ,if x==y elif x<y : ამ დროს
                      # თუ პირველი პირობა სრულდება მეორეს აგარ შეამოწმებს პროგრამა არარ გადაიტვირტება
    print("ragaca")
else:
 print("araa toli")'''

x= int(input("enter first number"))
y = int(input("enter secon number"))
if x>y:       # ამოცანაში გვინდა დაწერეოს ხ და ყ მდე ლუწი რიცხვები მაგრამ თუ პირველი ხ ნაკლებია ყ მაშინ ციკლი არ დაიწყება ამიტომ ჭირდება გადანიჭება
     x,y=y,x

ls=[]          #რაღაც ცარიელი მასივს ავირებთ
while x<y:
    ls.append(x)       # იქს წერს ბოლოში
    if x % 2 == 0 :
     x+=2
    else:
     x=x+1
     x+=2
print(ls)
