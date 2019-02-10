Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ~0b11101
-30
>>> 0b111&0b111
7
>>> 0b111&0b000
0
>>> 0b101|0b010
7
>>> 0b011|0b011
3
>>> 0b000|0b001
1
>>> 0b001|0b001
1
>>> 0b001^0b001
0
>>> 0b001^0b110
7
>>> 0b010^0b101
7
>>> 0b111^0b111
0
>>> 0b111<<
SyntaxError: invalid syntax
>>> 0b111<<1
14
>>> 0b000<<0b1
0
>>> 0b000<<1
0
>>> 0b111<<0b1
14
>>> 0b111>>0b1
3
>>> >>0b111>>0b1
SyntaxError: invalid syntax
>>> 
