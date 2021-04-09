'''number = input("enter number:")
result=0                                   # sheitan rixcxvs da getyvis mis cifrebis jams
for i in range(len(number)):
    result= result+int(number[i])
print(result)
'''

y=input("dawere kvadratuli gantoleba   am formatshi a*x**2+b*x+c=0 :" )

X0= -int(y[7])/2*int(y[0])

                                             #0123456789101112     1*x**2+5*x+6=0
D=int(y[7])**2 - 4*int(y[0])*int(y[11])
x1= (-int(y[7])-D**0.5)/2*int(y[0])
x2=(-int(y[7])+D**0.5)/2*int(y[0])        #y=input("chawere gantoleba:")



print("xo=",X0,"\t","d=", D, "\t","x1=",x1,"\t","x2=",x2,"\t")