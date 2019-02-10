Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x=["a",10,"b"]
>>> x.append(20)
>>> print(x)
['a', 10, 'b', 20]
>>> y=[30,"C"]
>>> x.append(y)
>>> print(x)
['a', 10, 'b', 20, [30, 'C']]
>>> x=["a",10,"b"]
>>> y=[30,"C"]
>>> x.append(y)
>>> print(x)
['a', 10, 'b', [30, 'C']]
>>> x=["a",10,"b"]
>>> x.insert(2,"a a")
>>> print(x)
['a', 10, 'a a', 'b']
>>> x=["a",10,"b"]
>>> y=[30,"C"]
>>> x.insert(2,y)
>>> print(x)
['a', 10, [30, 'C'], 'b']
>>> x=["amal",5,5,"Nimal",10,5]
>>> x.count(5)
3
>>> x=["amal",5,5,"Nimal",10,5]
>>> print(x.count(5))
3
>>> x=["amal",5,5,"Nimal",10,5]
>>> print(x.index(5))
1
>>> print(x.remove(5))
None
>>> x=["amal",5,5,"Nimal",10,5]
>>> print(x.remove(5))
None
>>> print(len(x))
5
>>> x=["amal",5,5,"Nimal",10,5]
>>> print(len(x))
6
>>> 
