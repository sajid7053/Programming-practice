def encode(string):
    string2 = string.replace('a','1')
    string3 = string2.replace('e','2')
    string4 = string3.replace('i','3')
    string5 = string4.replace('o','4')
    string6 = string5.replace('u','5')
    return string6
    
def decode(string):
    string7 = string.replace('1','a')
    string8 = string7.replace('2','e')
    string9 = string8.replace('3','i')
    string10 = string9.replace('4','o')
    string11 = string10.replace('5','u')
    return string11
