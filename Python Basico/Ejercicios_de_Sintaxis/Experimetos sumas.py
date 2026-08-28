word1 = "Hola "
word2 = "mundo"

int_try1 = 1
int_try2 = 4

list_try1 = [1,2,3,4,5,"Hola"]
list_try2 = [6,7,8,9,"mundo"]

float_try = 1.5

bool_try1 = True
bool_try2 = False

try1 = word1 + word2 #Result=  Hola mundo
try2 = word1 + int_try1 #Result: TypeError: can only concatenate str (not "int") to str
#try3 = int_try2 + word2 #Result: TypeError: unsupported operand type(s) for +: 'int' and 'str'
try4 = list_try1 + list_try2 #Result: [1, 2, 3, 4, 5, 'Hola', 6, 7, 8, 9, 'mundo']
#try5 = word1 + list_try1 #Result: TypeError: unsupported operand type(s) for +: 'int' and 'str'
try6 = float_try + int_try1 #Result: 2.5
try7 = bool_try1 + bool_try2 #Result: 1

print(try7)
