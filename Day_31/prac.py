mykeys = ['Name', 'Age', 'Class']
mydict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'} # order doesn't matter

dict_items = list(mydict.items())
dict_items.insert(0, ("new_key", "_value"))
mydict=dict(dict_items)
print(mydict)