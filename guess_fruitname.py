import random
fruits=["Apple","Banana","Orange","Water Melon","Straw Berry","Musk Melon","Kivy","Dragon","Pine Apple","Blue Berry","Guava","Fig","Custard Apple"]
fruits_name=random.choice(fruits)
print(fruits_name)
count=0
points=100

while count<4:
    guess=input("Enter fruit name:")
    if guess==fruits_name:
        print("You won!")
        print("points",points)
        break
    else:
        if count==0:
            print("Hint1:the lenth of fruit is",len(fruits_name))
        elif count==1:
            print("Hint2:the first letter of fruit is",fruits_name[0])
        elif count==2:
            hint3=fruits_name[0]
            for i in range(len(fruits_name)-1):
                hint3+= "*"
            print("Hint3:the fruit name could be",hint3 )
        elif count==3:
            hint4=fruits_name[0]
            for i in range (len(fruits_name)-2):
                hint4+="*"
            hint4+=fruits_name[-1]
            print("Hint4:The fruit name could be",hint4)
        else :
            pass    
    count+=1
    points-=20
