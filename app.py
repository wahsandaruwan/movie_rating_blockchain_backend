# Third-party module imports
import fastapi as fa

# Custom module imports
from block import Block

# Instance of block
bl = Block()

# Initialize an app
app = fa.FastAPI()

# Endpoint to mine blocks
@app.post("/mine/")
def mine(data : str):
    """
    This is the function which can be used to mine blocks.
    """ 
    
    if (not bl.bc.validate_blockchain()):
        return fa.HTTPException(status_code = 400, details = "The blockchain is invalid!")

    block = bl.mine_block(data = data)

    return block

# Endpoint to get the entire blockchain
@app.get("/blockchain/")
def blockchain():
    """
    This is the function which can be used to retrieve the entire blockchain.
    """ 

    if (not bl.bc.validate_blockchain()):
        return fa.HTTPException(status_code = 400, details = "The blockchain is invalid!")

    blockchain = bl.bc.get_chain()

    return blockchain

# Endpoint to validate the blockchain
@app.get("/validate/")
def validate():
    """
    This is the function which can be used to validate the entire blockchain.
    """ 
    if (not bl.bc.validate_blockchain()):
        return fa.HTTPException(status_code = 400, details = "The blockchain is invalid!")
    else:
        return {"status_code" : 200, "details" : "The blockchain is valid!"}


# Endpoint to return previous block
@app.get("/previous/")
def previous():
    """
    This is the function which can be used to retrieve the previous block of the blockchain.
    """ 
    if (not bl.bc.validate_blockchain()):
        return fa.HTTPException(status_code = 400, details = "The blockchain is invalid!")
    
    return bl.bc.get_prev_block()