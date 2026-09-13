def mix_args(a,*names):
    print("a=",a)
    print("names=",names)

mix_args(10,"ali","ahmed","anas")

def mix_args2(b,**accesories):
    print ("b=",b)
    print(accesories)

mix_args2(2,cpu=2500,monitor=2000,mouse=500)

def mix_args3(c,*names,**fruits):
    print("c=",c)
    print("names=",names)

mix_args3(10,"ali","ahmed","anas",apple=120,banana=40,Mango=250)

def mix_args4(a,*names,b=400):
    print("a=",a)
    print("names=",names)
    print("b=",b)

mix_args4(20,"ahmed","rahul","hamid")
