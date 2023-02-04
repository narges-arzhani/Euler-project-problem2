def fibonacci():
    if new%2==0:
        return True
    else:
        return False
first=1
second=2
sum=0
while first<4000000:
    if fibonacci():
        new=first+second
        first = second
        second = new
        sum=sum+first
print(sum)
