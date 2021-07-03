#!C:\Python34
s = "Tongue tied and twisted just an earth bound misfit I"

long = max(s.split(), key=len)
print(long)

#l= list(s.split())
logest = sorted(s.split(), key=len)
print(logest[-1])