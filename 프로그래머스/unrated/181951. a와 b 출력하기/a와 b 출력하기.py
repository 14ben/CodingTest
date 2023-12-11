#a, b = map(int, input().strip().split(' '))
#print("a=" + a)
#print("b=" + b)

#   -----------------------------------------------
#   Traceback (most recent call last):
#     File "/solution.py", line 4, in <module>
#       print("a=" + a)
#   TypeError: can only concatenate str (not "int") to str
#   -----------------------------------------------

a, b = map(int, input().strip().split(' '))
print("a = " + str(a))
print("b = " + str(b))