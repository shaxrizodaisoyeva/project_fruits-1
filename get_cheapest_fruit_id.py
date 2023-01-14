def get_cheapest_fruit_id(data:str)->id:
    """
    This function returns the index of the cheapest fruit in the list

    args:
        data: CSV file with the fruits data
    returns:
        name of the cheapest fruit
    """
    # your code here
    a=data.split()[1:]
    price=[]
    fruit=[]
    for i in a:
        price.append(float(i.split(",")[1]))
        fruit.append(i.split(",")[0])
        b=min(price)
        c=price.index(b)
        d=fruit[c]
        e=fruit.index(d)
    return e
f=open('fruits.csv')
data=f.read()
print(get_cheapest_fruit_id(data)) 