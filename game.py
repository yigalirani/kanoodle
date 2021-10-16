input='''
 1 
111
 1

 22
22 
2

3
33
3
3

44
 4
44

5
5
5
5

66
6

 7
 7
 7
77

 8
88
88

 9
 9
99
9 

aa
aa

  b
  b
bbb

c
c
cc
'''
def trim_line(x):
  for i in range(len(x),0,-1):
    if x[i-1]!=' ':
      return x[0:i]
  return ''
def pad(x,n):
  x=x+'        '
  return x[:n]
def trim_shape(x):
  #print(x)
  n=max([len(trim_line(line)) for line in x.split('\n')])
  ans= [pad(line,n)for line in x.split('\n') if trim_line(line)!='']
  #print(ans)
  return ans

def print_piece(v):
  print('.'*(len(v[0])+2))
  for x in v:
    print('.'+x+'.')
  print('\n')    
  return
  lines=x
  m=len(lines)
  n=max(len(line) for line in lines)
  print('.'*(m+2))
  for oline in lines:
    line=trim_line(oline)
    line=line+(m-len(line))*' '
    print('.'+line+'.')
  print('.'*(m+2),'\n'  )
def main():
  for x in input.split('\n\n'):
    print_piece(trim_shape(x))
main()