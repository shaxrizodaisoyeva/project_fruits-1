def get_frutis_name(data:str)->list:
    """
    This function returns the name of the fruits in the list

    args:
        data: CSV file with the fruits data
    returns:
        list of fruits names
    """
    a=data.split()[1:]
    fruit_name=[]
    for i in a:
        fruit_name.append(i.split(",")[0])
    return fruit_name
f=open('fruits.csv')
data=f.read()
print(get_frutis_name(data)) 

    