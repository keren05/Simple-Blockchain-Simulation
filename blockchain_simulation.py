import hashlib
import time

class Block:
    def __init__(self, index, transactions, previous_hash):
        """
        Initialize a Block.
        :param index: Block index.
        :param transactions: List of transactions.
        :param previous_hash: Hash of the previous block.
        """
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculate the hash of the block.
        :return: Hash value as a hexadecimal string.
        """
        block_string = (
            str(self.index) +
            str(self.timestamp) +
            str(self.transactions) +
            str(self.previous_hash) +
            str(self.nonce)
        )
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        """
        Perform proof-of-work to mine the block.
        :param difficulty: Number of leading zeros required in the hash.
        """
        target = '0' * difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    def __init__(self, difficulty=4):
        """
        Initialize the Blockchain.
        :param difficulty: Difficulty level for mining.
        """
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty

    def create_genesis_block(self):
        """
        Create the genesis block.
        :return: Genesis block.
        """
        return Block(0, "Genesis Block", "0")

    def get_latest_block(self):
        """
        Get the latest block in the chain.
        :return: Latest block.
        """
        return self.chain[-1]

    def add_block(self, transactions):
        """
        Add a new block to the blockchain.
        :param transactions: List of transactions to include in the block.
        """
        previous_block = self.get_latest_block()
        new_block = Block(len(self.chain), transactions, previous_block.hash)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Validate the integrity of the blockchain.
        :return: True if valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                print(f"Block {i} has been tampered with!")
                return False

            if current_block.previous_hash != previous_block.hash:
                print(f"Block {i}'s previous hash doesn't match Block {i-1}'s hash!")
                return False

        return True

    def print_chain(self):
        """
        Print the details of the blockchain.
        """
        for block in self.chain:
            print("Index:", block.index)
            print("Timestamp:", time.ctime(block.timestamp))
            print("Transactions:", block.transactions)
            print("Previous Hash:", block.previous_hash)
            print("Hash:", block.hash)
            print("Nonce:", block.nonce)
            print("-" * 50)

# Demonstration
if __name__ == "__main__":
    blockchain = Blockchain(difficulty=4)

    print("Mining block 1...")
    blockchain.add_block(["Alice pays Bob 5 BTC", "Bob pays Charlie 2 BTC"])

    print("Mining block 2...")
    blockchain.add_block(["Charlie pays Alice 1 BTC", "Alice pays David 3 BTC"])

    print("Blockchain integrity check:", blockchain.is_chain_valid())

    print("\nBlockchain:")
    blockchain.print_chain()

    # Tampering with the chain
    print("\nTampering with the blockchain...")
    blockchain.chain[1].transactions = ["Alice pays Eve 100 BTC"]

    print("Blockchain integrity check after tampering:", blockchain.is_chain_valid())
