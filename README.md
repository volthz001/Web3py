# Web3py
aplikasi Python sederhana yang menggunakan pustaka Web3 untuk melakukan transfer Ether peer-to-peer di jaringan Ethereum, terhubung ke Ganache sebagai jaringan blockchain lokal. Dalam proyek ini, aplikasi melakukan beberapa langkah penting seperti validasi kunci pribadi, pengaturan transaksi dengan data biaya gas dan nonce, hingga pengiriman dan konfirmasi transaksi menggunakan tanda tangan digital. Selain itu, aplikasi memeriksa saldo awal dan akhir kedua akun untuk menampilkan perubahan saldo setelah transaksi selesai.

Contoh Output
C:\Users\Volthz\Desktop\tugas>py test.py
Terhubung ke Ganache!
Masukkan jumlah Ether yang akan dikirim:0.222
-----------------------------------------------------------------------------
||TRANSAKSI BERHASIL!!!                                                     ||
||txn_Hash: 80e8d9642305ff1a2946b7a4feec9488f97aee3e0bf1f46242b9e39c1650dd69||
||Pengirim: 0x6DeFa57af17C310Dee28E5A6C5f83CeA2a447E10                      ||
||Penerima: 0xb7e2db54B010504B06a8BaBCEb7fDAc316656f9e                      ||
||Biaya transaksi: 0.00042 Ether                                            ||
||Status Transaksi: 1                                                       ||
||Time : 2024-11-13 01:47:14                                                ||
-----------------------------------------------------------------------------
Saldo Anda saat ini 986.536325 Etherum
