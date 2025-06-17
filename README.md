# Web3py Project

A beginner-friendly Python project that demonstrates basic interaction with the Ethereum blockchain using the [Web3.py](https://web3py.readthedocs.io/) library.

## ✨ Features
- Connect to a local or remote Ethereum node (HTTP provider)
- Read Ethereum account balances
- Send transactions (ETH transfer)
- Call smart contract methods

## 📆 Requirements
- Python 3.8+
- Ganache CLI or Infura endpoint

## ⚙️ Installation
```bash
# Clone the repository
$ git clone https://github.com/volthz001/Web3py.git
$ cd Web3py

# Create virtual environment (optional)
$ python -m venv venv
$ source venv/bin/activate  # on Windows use venv\Scripts\activate

# Install dependencies
$ pip install -r requirements.txt
```

## 📊 Usage
Edit the `config.py` file to set your RPC endpoint, account addresses, and private keys.

```bash
$ python main.py
```

## 👁️ Example
```python
from web3 import Web3

web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
print("Connected:", web3.is_connected())
print("Balance:", web3.eth.get_balance("0x1234..."))
```

## ✏️ Configuration
Update `config.py` with your:
- RPC provider URL (Ganache, Infura)
- Sender and receiver addresses
- Private key for signing transactions

## □ Project Structure
```
Web3py/
├── main.py
├── config.py
├── requirements.txt
├── README.md
├── LICENSE
└── tests/
    └── test_web3.py
```

## ✅ To Do
- [ ] Add smart contract interaction (via ABI)
- [ ] Add unit tests with mocking
- [ ] Setup GitHub Actions CI/CD

## ✉️ License
This project is licensed under the MIT License. See `LICENSE` for details.

## 👥 Author
Hizkia Siallagan
