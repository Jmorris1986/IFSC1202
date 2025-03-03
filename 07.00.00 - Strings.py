# Example 1
print("Example 1")
print('>_< ' * 5)  # >_< >_< >_< >_< >_<
 
# Example 2
print("Example 2")
print(len('abcdefghijklmnopqrstuvwxyz'))
# 26
 
# Example 3
print("Example 3")
s = str(2 ** 100)
print(s)  
# 1267650600228229401496703205376
print(len(s))
# 31
 
# Example 4
print('Example 4')
s='Hello'
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[-1])
print(s[-2])
print(s[-3])
print(s[-4])
print(s[-5])
 
# Example 5
print('Example 5')
s = 'abcdefg'
print(s[1])     #b
print(s[-1])    #g
print(s[1:3])   #bc
print(s[1:-1])  #bcdef
print(s[:3])    #abc
print(s[2:])    #cdefg
print(s[:-1])   #abcdef
print(s[::2])   #aceg
print(s[1::2])  #bdf
print(s[::-1])  #gfedcba
 
# Example 6 
print('Example 6')
s = 'abcdefghijklm'
print(s[0:10:2])
for i in range(0, 10, 2):
    print(i, s[i])
    
# Example 7 
print("Example 7")
s = 'Hello'
print(s.find('e'))   # 1
print(s.find('ll'))  # 2
print(s.find('L'))   # -1
 
# Example 8
print('Example 8')
s = 'abracadabra'
print(s.find('b'))  # 1
print(s.rfind('b')) # 8
 
# Example 9
print('Example 9')
s = 'my name is bond, james bond, okay?'
print(s.find('bond'))     # 11
print(s.find('bond', 12)) # 23
 
# Example 10
print('Example 10')
print('a bar is a bar, essentially'.replace('bar', 'pub'))  # 'a pub is a pub, essentially'
 
# Example 11
print('Example 11')
print('a bar is a bar, essentially'.replace('bar', 'pub', 1)) # 'a pub is a bar, essentially'
 
# Example 12
print('Example 12')
print('Abracadabra'.count('a'))    # 4
print(('aaaaaaaaaa').count('aa'))  # 5