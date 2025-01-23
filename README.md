# Simple-Blockchain-Simulation

This project is a basic blockchain simulation designed to demonstrate the core concepts of blockchain, including block creation, hashing, and chain validation. It also includes optional Proof-of-Work for computational difficulty.

## Features
- Block structure with essential components (index, timestamp, transactions, hashes).
- Hashing using the SHA-256 algorithm.
- Chain management with validation to ensure data integrity.
- Optional Proof-of-Work for added computational difficulty.
- Demonstration of tampering detection.

## Prerequisites
- Python 3.x
- No additional libraries are required (uses only the standard library).

## Setup and Execution
1. Clone this repository or download the code file.
2. Ensure Python is installed on your machine. You can check by running:
   ```bash
   python --version
3.Run the script:
python simple_blockchain.py

## How It Works
A genesis block (the first block) is created automatically.
You can add new blocks with sample transactions.
The blockchain validates itself to ensure integrity.
The program demonstrates tampering detection by modifying a block and checking the chain's validity.

## Proof-of-Work
The Proof-of-Work mechanism makes block creation computationally intensive by solving a hash puzzle. You can adjust the difficulty by modifying the difficulty parameter in the code.

## OUTPUT
____________________________________________________________________________________
Block 0
Timestamp: 2025-01-23 14:26:59.737469
Transactions: ['Genesis Block']
Hash: cdb51a643450ca0964e6771cf0f4034c337b7d7ec8970175b743366cbda8302d
Previous Hash: 0

Block 1
Timestamp: 2025-01-23 14:26:59.738467
Transactions: ['Alice pays Bob 10 BTC']
Hash: 86f7dfb535adce94327c51ed2685dd6a748cba1e5164b5934aa947efd2801e8c
Previous Hash: cdb51a643450ca0964e6771cf0f4034c337b7d7ec8970175b743366cbda8302d

Block 2
Timestamp: 2025-01-23 14:26:59.738467
Transactions: ['Bob pays Charlie 5 BTC']
Hash: ad39c42c8df194ad8197fa001515aca698b595f34ed0ec9d082267c619983394
Previous Hash: 86f7dfb535adce94327c51ed2685dd6a748cba1e5164b5934aa947efd2801e8c

Is blockchain valid? True

After tampering:
Block 0
Timestamp: 2025-01-23 14:26:59.737469
Transactions: ['Genesis Block']
Hash: cdb51a643450ca0964e6771cf0f4034c337b7d7ec8970175b743366cbda8302d
Previous Hash: 0

Block 1
Timestamp: 2025-01-23 14:26:59.738467
Transactions: ['Alice pays Eve 20 BTC']
Hash: 94dc151414a1fb14239dada946a1a63bd4f8a02822b9fdd952e3a7464cad472c
Previous Hash: cdb51a643450ca0964e6771cf0f4034c337b7d7ec8970175b743366cbda8302d

Block 2
Timestamp: 2025-01-23 14:26:59.738467
Transactions: ['Bob pays Charlie 5 BTC']
Hash: ad39c42c8df194ad8197fa001515aca698b595f34ed0ec9d082267c619983394
Previous Hash: 86f7dfb535adce94327c51ed2685dd6a748cba1e5164b5934aa947efd2801e8c

Is blockchain valid? False
__________________________________________________________________________________
## Code Organization
Block class: Defines the structure of a single block.
Blockchain class: Manages the chain of blocks.
Methods:
add_block: Adds a new block to the chain.
is_chain_valid: Checks if the chain is valid.
display_chain: Prints all blocks in the chain.
tamper_block: Modifies a block to simulate tampering.

## Contributing
If you'd like to contribute or improve this simulation, feel free to fork the repository and create a pull request.
