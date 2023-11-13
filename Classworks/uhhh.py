import re

print(re.sub(r'\t', ',', '1\t2\t3\t4\t5\t6'))
print(re.sub(r',\s*','1,2,3,4,5,6,7,8'))
