catNames=['Kitty','Oliver','Felix']
 #om te zien of iets in een de lijst staat
'Oliver' in catName


#om te zien of iets niet in de lijst ziet
'Oliver' not in catName




#om geen fout code te krijgen
def elementInList (element, mylist):
    try:
        return mylist.index(element)
    except:
        return -1