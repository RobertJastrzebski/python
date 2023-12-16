import re

question= "lovely spam! Wonderful spam!"

result = re.search("spam",question)
print(result)

print(question[7:11])
print(result.span())
print(result.start())
print(result.end())