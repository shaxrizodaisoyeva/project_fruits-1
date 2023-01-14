def get_total_price(data:str)->float:
    """
    This function returns the total price of the fruits in the list

    args:
        data: CSV file with the fruits data
    returns:
        list of fruits total price
    """
    a=data.split()[1:]
    sum=0
    for i in a:
        sum+=float(i.split(",")[1])
    return sum
f=open('fruits.csv')
data=f.read()
print(get_total_price(data))    