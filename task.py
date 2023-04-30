



python_programming=499
python_libraries=855
datascience=654
delivery=250
gst=12
m=n=p=0
cus_choice1=input('do u want book1 ty')
if cus_choice1=='yes':
    m=int(input('enter quantity'))
cus_choice2=input('do u want book2 ty')
if cus_choice2=='yes':
    n=int(input('enter quantity'))
cus_choice3=input('do u want book3 ty')
if cus_choice3=='yes':
    p=int(input('enter quantity'))
invoice=0.00
total=python_programming*m+python_libraries*n+datascience*p
if m or n or p !=0:
    invoice=total+(total*gst)/100+delivery
print(invoice)
