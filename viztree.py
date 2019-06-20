import contextlib,threading
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return 'TreeNode({})'.format(self.val)
    
def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left  = kids.pop()
            if kids: node.right = kids.pop()
    return root

def drawtree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1
    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y-20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x-dx, y-60, dx/2)
            jumpto(x, y-20)
            draw(node.right, x+dx, y-60, dx/2)
    import turtle
    t = turtle.Turtle()
    t.speed(0); turtle.delay(0)
    h = height(root)
    jumpto(0, 30*h)
    draw(root, 0, 30*h, 40*h)
    t.hideturtle()
    turtle.mainloop()
def thread_drawtree(root):
    thread1 = threading.Thread(target = drawtree, args = (root,))
    thread1.start()
from timeit import default_timer as timer

@contextlib.contextmanager 
def benchmark(name,size=None):
    start = timer()
    yield
    t = timer() - start
    if size:
        print(("%s : %0.3g,size %d, %d per sec") % (name, t,size,size//t))
    else:
        print(("%s : %0.3g") % (name, t))

if __name__ == '__main__':
    #drawtree(deserialize('[2,-4]'))
    drawtree(deserialize('[-1,5,null,4,null,null,2,-4]'))
