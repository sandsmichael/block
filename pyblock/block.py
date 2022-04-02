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

# print(d.__dict__)
# print(c.parent_id)
# print(a.__dict__)
# print(b.__dict__)
# print(b.parent_hash)


d = Block()
d.id = 4
d.history = 'block d'
d.parent = c.id


import json
serialized_block = json.dumps(d.__dict__).encode('utf-8')
print(serialized_block)

def mining():
    '''
    miner writes block to chain by solving puzzle (PoW); puzzle is finding hash of serialized block that has five leading zeros.
    solution requires brute force
    succesfull result entails adding a nonce, or bytte value of a  number to the contents of the block, geting it's hash, and  checking  for 5 leading zeros.
    '''
    data_str = json.dumps(d.__dict__)
    data_bytes = bytes(data_str, 'utf8')
    for i in range(1000000):
        nonce = str(i).encode('utf-8')
        result = hashlib.sha256(data_bytes + nonce).hexdigest()
        print(f'[INVALID] try again: {result}')
        if result[:5] == '00000':
            print(f'[SUCCSS] puzzle solved! {result}')
            break
mining()

