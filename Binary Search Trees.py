def insert (bst, key):
    if bst == {}:
        bst['key']=key
        bst['right']={}
        bst['left']={}
##        return bst
    elif key<bst['key']:
        insert(bst['left'],key)
    else:
        insert(bst['right'],key)
bst={}
lst=[68, 88, 61, 89, 94, 50, 4, 76, 66, 82]
for i in lst:
    insert(bst,i)
print("a): create bst:")
print(bst)
print('\n')


def exist(bst,key):
    if bst=={}:
        return False
    elif bst['key']==key:
        return True
    elif key<bst['key']:
        return exist(bst['left'],key)
    else:
       return exist(bst['right'],key) 
print("whether key 50 exists:")
print(exist(bst,50))
print('\n')

print("whether key 49 exists:")
print(exist(bst,49))
print('\n')

def maximum(bst):
    if bst['right']=={}:
        return bst['key']
    else:
        return maximum(bst['right'])
print("maximum is:")
print(maximum(bst))
print('\n')

print(bst)
print('\n')

def inorder_traversal(bst):
    #ascending order: smallest to largest, First left then it's key then right branch.
    if bst=={}:
        return
    inorder_traversal(bst['left'])
    print(bst['key'])
    inorder_traversal(bst['right'])
    
print("inorder_traversal")
inorder_traversal(bst)
print('\n')

def preorder_traversal(bst): #all lefts(highest to lowest: up to down), key, then right (lowest to highest: up to down)
    if bst=={}:
        return
    print(bst['key'])
    preorder_traversal(bst['left'])
    preorder_traversal(bst['right'])
print("preorder_traversal")
preorder_traversal(bst)
print('\n')
    
def postorder_traversal(bst): #by levels, lowest to highest level 
    if bst=={}:
        return
    postorder_traversal(bst['left'])
    postorder_traversal(bst['right'])
    print(bst['key'])
    
print("postorder_traversal")
postorder_traversal(bst)
print('\n') 
