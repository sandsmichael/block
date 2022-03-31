

class Block:
    ''' blockchain represented by linked list structure'''
    id = None
    history = None
    parent_id = None

a = Block()
a.id = 1
a.history = 'block a'

b = Block()
b.id =  2
b.history = 'block b'
b.parent_id = a.id

c = Block()
c.id = 3
c.history = 'block c'
c.parent_id = b.id


print(c.parent_id)