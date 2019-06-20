from viztree import *
                                                                                   
def get_next(root,val):
    if root.val==val:
        return root
    for child in [root.left,root.right]:
        if child and child.val==val:
            return child
    return None
def find_element_in_complete_tree(root,num): #answer to the question
    path=[]
    while num:
        path.append(num)
        num=num//2
    for x in path[::-1]:
        root=get_next(root,x)
        if root is None:
            return False
    return True

def collect_layer(layer):
    for parent in layer:
        for child in [parent.left,parent.right]:
            if child:
                yield child
            else:
                return
def build_layer(layer,first_num,last_num):
    def make_child(i):
        if i>last_num:
            return None,i
        else:
            return TreeNode(i),i+1
    i=first_num
    for parent in layer:
        parent.left,i=make_child(i)
        parent.right,i=make_child(i)
        if i>last_num:
            break
    return list(collect_layer(layer)),i


def build_tree(last_num):
    root=TreeNode(1)
    layer=[root]
    start_num=2
    while start_num<last_num:
        layer,start_num=build_layer(layer,start_num,last_num)
    return root


def test_it(size):
    with benchmark('build tree',size):
        t=build_tree(size)
    #drawtree(t)
    with benchmark('find in tree'):
        expect_true=find_element_in_complete_tree(t,size)
        expect_false=find_element_in_complete_tree(t,size+1)
    print('expect_true',expect_true)
    print('expect_true',expect_false)

test_it(10000000)