def format(s):
    return s[0].upper() + s[1::].lower()

lst=['adam','LisA','BEN']
print map(format,lst)