spam = [2,5,3.14,1,-7]
spam.sort()
print(spam)
spam.sort(reverse=True)
#or spam.reverse()
print(spam)
spam = ['Alles', 'ant','Bob','badgers', ]
#sorteer met via de asi tabbel
spam.sort
print(spam)
#voor te zorgen dat het wel alfabeeties is 
spam.sort(key=str.lower)
print(spam)
spam = [2, 'x']
#kan niet met strings en int sorteren
spam.sort