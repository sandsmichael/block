import hashlib
import json

class Block:
    ''' blockchain represented by linked list structure'''
    id = None           # current block id
    history = None      # message
    parent_id = None    # previous block id
    parent_hash= None   # unique hash comprising of previous block id's and messages

a = Block()
a.id = 1
# a.history = 'block a'
# a.history = 'block b parent hash should change becuase i\'m changing the block a message'
a.history = 'block a' 


b = Block()
b.id =  2
b.history = 'block b'
b.parent_id = a.id
b.parent_hash = hashlib.sha256(json.dumps(a.__dict__).encode('utf-8')).hexdigest()

c = Block()
c.id = 3
c.history = 'block c'
c.parent_id = b.id
b.parent_hash = hashlib.sha256(json.dumps(a.__dict__).encode('utf-8')).hexdigest()


print(c.parent_id)

print(a.__dict__)

print(b.__dict__)

print(b.parent_hash)