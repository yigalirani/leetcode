
''' sorry attempt to automaticalt convert to iteration. idea: can this 
def get_alloc_f()

def flat_runner(input,f):
    stack=[]
`   ans.append(input)
    cache={}
    while(stack):
        top=stack.pop()
        ans = cache.get(top,None)
        if ans:
            if len(stack)==0:
                return ans
            continue
        
    
def get_alloc_iter(n,k):
    stack=[]
`   ans.append((n,k))
    cache={}
    while(stack):
        top=stack.pop()
        if len(stack)==0 and top in cache:
            return stack[top]
        
'''        
def get_alloc(n,k):
    if k==1:
        return [[n]]
    ans=[]
    for i in range(0,n+1):
        for x in get_alloc(n-i,k-1):
            ans.append(x+[i])
    return ans

for i,x in enumerate(get_alloc(5,2)):
    print(i,x,sum(x))
    