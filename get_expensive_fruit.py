def get_expensive_fruit(data:str)->str:
    """
    This function returns the name of the most expensive fruit in the list

    args:
        data: CSV file with the fruits data
    returns:
        name of the most expensive fruit
    """
    # your code here
    a=data.split()[1:]
    price=[]
    fruit=[]
    for i in a:
        price.append(float(i.split(",")[1]))
        fruit.append(i.split(",")[0])
        b=max(price)
        c=price.index(b)
        d=fruit[c]
    return d
f=open('fruits.csv')
data=f.read()
print(get_expensive_fruit(data)) 


