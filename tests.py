import itertools
def int_of_bool():
    print (int(2==2))
    print (int(True))
    print (int(False))
def test_generator_expressions():
    l= (x+1 for x in range(1000000))
    ans=max(l)
    print(ans)
def test_split():
    print(print('  hello  world   '.split()))
def test_first():
    r=range(10)
    r=iter(r)
    first=next(r)
    print('flrst',first)
    #print('first',first)
    for row in r:
        print('decond',row)
def test_combinations():
    def print_it(name,gen): 
        print(name,"\n"+"*"*30)
        for i,x in enumerate(gen):
            print(i,':',x)
        
    input=range(3)
    print_it('input',input)
    print_it('combinations',itertools.combinations(input,3))
    print_it('permutations',itertools.permutations(input))
def tokenizer(s):
    ans=''
    for c in s+' ':
        if c in "-+/":
            yield ans
            ans=''
            yield c
            continue
        if c==' ':
            yield ans
            ans=''
            return
        ans+=c
 
def test_re():
    import re
    s="-45/2+45/3-45/4"
    print(re.split('\+|-',s))
    print([x for x in itertools.grouper(tokenizer(s),3)])

if __name__=='__main__':
    #int_of_bool()
    #test_generator_expressions()
    #test_split()
    #test_first()
    #test_combinations()
    test_re()
