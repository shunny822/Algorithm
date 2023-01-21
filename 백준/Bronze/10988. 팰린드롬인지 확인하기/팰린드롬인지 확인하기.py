s = input()
n = len(s)//2
print( 1 if s[:n] == s[-1:-(n+1):-1] else 0)