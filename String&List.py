    #01234       #012345
s = "Hello"; t = "Python"
x = [1,3,5,7]; y = [5,6,7,8]
r = s + t
z = x + y

print(len(s), len(r), len(x), len(z))      # lenght

print(s[1], x[2])                          # index
print(s[-1], s[-2], x[-1], x[-2])

print(s[0:3:1])   #[start:stop:step]       # slice
x[3] = 99
print(x[3])