from viztree import *
def find(root,num):
    pass
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

t=build_tree(20)
drawtree(t)