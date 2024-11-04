#  The purpose of this file is to test Lines.py

m= 50

while True:
    print('Amount due:',m,'cents')
    a= int(input('Insert coin:'))
    if a==5 or a==25 or a==10:
        if a>=m:
            print('Amount Owed:',m-a)
            break
        m=m-a
    else:
        continue