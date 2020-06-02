import hashlib
import json

class Block():
    def __init__(self, data, nonce):
        self.nonce = nonce
        self.data = data
        self.previousHash = 0
        self.hash = self.calHash()

    def calHash(self):
        while 1:
            val = hashlib.sha256(str(self.nonce).encode() + str(self.data).encode()
                                  + str(self.previousHash).encode()).hexdigest()
            if self.nonce == 0:
                return val
            
            if val[0:5] == '00000':
                return val
            else:
                self.nonce += 1

class BlockChain:
    def __init__(self):
        self.chain = []
        self.createGenesis()

    def createGenesis(self):
        self.chain.append(Block('Genesis', 0))

    def addBlock(self, nBlock):
        nBlock.previousHash = self.chain[len(self.chain)-1].hash
        nBlock.hash = nBlock.calHash()
        self.chain.append(nBlock)

onion = BlockChain()
onion.addBlock(Block("2nd", 1))
onion.addBlock(Block("3rd", 1))

for block in onion.chain:
    print((json.dumps(vars(block), indent=0)).strip('{').strip('}'))