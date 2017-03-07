from collections import deque

def hash_state(state):
    return str(state[0])+':'+str(state[1])

def graph_search(start_state,enum_neigboors,is_goal,hash_state):
    visited=set()
    visited.add(hash_state(start_state))
    queue=deque()
    queue.append((start_state,0))
    while len(queue) :
        current,cost=queue.popleft()

        if (is_goal(current)):
            return cost
        
        for x in enum_neigboors(current):
            hash=hash_state(x)
            if hash not in visited:
                visited.add(hash)
                queue.append((x,cost+1))

    
class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        
        """
        len_ring=len(ring)
        len_key=len(key)
       
        def get_next(state):
            ring_pos,key_pos=state
            if ring[ring_pos]==key[key_pos]:
                yield (ring_pos,key_pos+1)#press enter
            else:
                yield ((ring_pos+1)%len_ring,key_pos)
                yield ((ring_pos-1)%len_ring,key_pos)

        def is_goal(state):
            ring_pos,key_pos=state
            return key_pos==len_key
 
        return graph_search((0,0),get_next,is_goal,hash_state)
        
        
        