
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
def get_alloc2(n,k):
    if k==1:
        return [[n]]
    ans=[]
    for i in range(0,n+1):
        for x in get_alloc2(n-i,k-1):
            ans.append(x+[i])
    return ans

def get_alloc(n,k):
    return [tuple(x) for x in get_alloc2(n,k)]

def get_alloc_iter(n,k):
    cur=[(n,k,[])]
    while True:
        nxt=[]
        all_done=True
        for n,k,r in cur:
            if k==0:
                nxt.append((n,k,r))
                continue
            all_done=False
            #print ('>>>>>',n,k,r)
            for i in range(n+1):
                #print(i)
                if k>1 or i==n:
                    nxt.append((n-i,k-1,r+[i]))
        if all_done:
            return [tuple(x[2]) for x in nxt]
        cur=nxt

a1=set(get_alloc(40,5))
a2=set(get_alloc_iter(20,5))
#print(a1)
print(a2)
print(len(a1))
print (a1.difference(a2))
