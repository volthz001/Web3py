from web3 import Web3
from datetime import datetime, timezone
# Menghubungkan Web3 ke Ganache
ganache_url = "http://127.0.0.1:8545"
w3 = Web3(Web3.HTTPProvider(ganache_url))
# Memeriksa apakah koneksi berhasil dengan ternary operator

print("Terhubung ke Ganache!" if w3.is_connected() else "Gagal terhubung ke Ganache.") if w3.is_connected() else exit()


# Mendapatkan akun yang tersedia
accounts = w3.eth.accounts
sender_address = accounts[0]  # Pengirim
receiver_address = accounts[1]  # Penerima

# Private key untuk pengirim (pastikan ini valid)
private_key = "0x5d338cb0c7790c5dd515883b752e87b1635a40d55f734a6f9b318384aae6dc2b"  # Gantilah dengan private key yang benar (harus 64 karakter hex)

# Pastikan private key yang digunakan valid (harus diawali dengan "0x" dan 64 karakter heksadesimal)
# Menggunakan ternary untuk memeriksa apakah private_key valid
print("Kunci pribadi tidak valid. Pastikan kunci pribadi diawali dengan '0x' dan berisi 64 karakter hexadecimal.") if not private_key.startswith('0x') or len(private_key) != 66 else None
exit() if not private_key.startswith('0x') or len(private_key) != 66 else None


# Menentukan jumlah yang ingin dikirim (misalnya 0.5 Ether)
amount_in_ether:float = input("Masukkan jumlah Ether yang akan dikirim:")  # Jumlah Ether yang ingin dikirim
amount_in_wei = w3.to_wei(amount_in_ether, 'ether')  # Menggunakan to_wei

# Menentukan biaya transaksi (Gas Used * Gas Price)
gas_used = 21000  # Gas yang digunakan untuk transaksi transfer Ether
gas_price_gwei = 20  # Gas price yang digunakan (dalam Gwei)

# Mengonversi gas price ke Wei
gas_price_wei = w3.to_wei(gas_price_gwei, 'gwei')

# Menghitung biaya transaksi dalam Wei
transaction_cost_wei = gas_used * gas_price_wei

# Mengonversi biaya transaksi ke Ether
transaction_cost_ether = w3.from_wei(transaction_cost_wei, 'ether')

# Memeriksa saldo pengirim dan penerima sebelum transaksi
sender_balance_before = w3.eth.get_balance(sender_address)
receiver_balance_before = w3.eth.get_balance(receiver_address)

# Mengonversi saldo dari Wei ke Ether
sender_balance_before_ether = w3.from_wei(sender_balance_before, 'ether')
receiver_balance_before_ether = w3.from_wei(receiver_balance_before, 'ether')

#print(f"Saldo Pengirim Sebelum Transaksi: {sender_balance_before_ether} Ether")
#print(f"Saldo Penerima Sebelum Transaksi: {receiver_balance_before_ether} Ether")


# Membuat transaksi
transaction = {
    'to': receiver_address,
    'value': amount_in_wei,
    'gas': gas_used,  # Gas yang dibutuhkan untuk transaksi transfer Ether
    'gasPrice': gas_price_wei,  # Harga gas (dalam Gwei) menggunakan to_wei
    'nonce': w3.eth.get_transaction_count(sender_address),  # Nonce untuk pengirim
    'chainId': 1337  # ID jaringan untuk Ganache (defaultnya 1337)
}

# Menandatangani transaksi menggunakan private key
signed_transaction = w3.eth.account.sign_transaction(transaction, private_key)

# Mengirim transaksi
tx_hash = w3.eth.send_raw_transaction(signed_transaction.raw_transaction)

# Menunggu transaksi selesai
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print(f"-----------------------------------------------------------------------------\n||TRANSAKSI BERHASIL!!! \t\t\t\t\t\t    ||\n||txn_Hash: {tx_hash.hex()}||")
print(f"||Pengirim: {accounts[0]}\t\t\t    ||")
print(f"||Penerima: {accounts[1]}\t\t\t    ||")
print(f"||Biaya transaksi: {transaction_cost_ether} Ether\t\t\t\t\t    ||")
print(f"||Status Transaksi: {tx_receipt['status']}\t\t\t\t\t\t\t    ||")
timestamp = w3.eth.get_transaction(tx_hash)
datetime_object = datetime.fromtimestamp((w3.eth.get_block(timestamp["blockNumber"])['timestamp']),timezone.utc)

# Menampilkan waktu yang lebih mudah dibaca
formatted_time = datetime_object.strftime('%Y-%m-%d %H:%M:%S')
print(f"||Time : {formatted_time}\t\t\t\t\t\t    ||\n-----------------------------------------------------------------------------")
#print(f"Date {datetime.fromtimestamp(w3.eth.get_block(transaction['blockNumber'])["timestamp"], timezone.utc)}")

# Memeriksa saldo pengirim dan penerima setelah transaksi
sender_balance_after = w3.eth.get_balance(sender_address)
receiver_balance_after = w3.eth.get_balance(receiver_address)

# Mengonversi saldo dari Wei ke Ether
sender_balance_after_ether = w3.from_wei(sender_balance_after, 'ether')
receiver_balance_after_ether = w3.from_wei(receiver_balance_after, 'ether')
print(f"Saldo Anda saat ini {sender_balance_after_ether} Etherum")

# Menampilkan saldo setelah transaksi
#print(f"\nSaldo Pengirim Setelah Transaksi: {sender_balance_after_ether} Ether")
#print(f"Saldo Penerima Setelah Transaksi: {receiver_balance_after_ether} Ether")
