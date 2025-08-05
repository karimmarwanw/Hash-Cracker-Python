# 🔐 Hash Identifier & Brute-Forcer

This is a simple Python tool that helps identify the hashing algorithm used (based on hash length) and attempts to brute-force the original password using the popular `rockyou.txt` wordlist.

---

## 🧠 Features

- **Hash Type Detection**  
  Automatically detects hash type based on its length:
  - MD5
  - SHA1
  - SHA256
  - SHA384
  - SHA512

- **Dictionary Attack**  
  Uses a wordlist (`rockyou.txt`) to brute-force the hash.

- **Interactive CLI**  
  Input hashes repeatedly until you press Enter to exit.

---

## 🚀 How It Works

1. Enter a hash when prompted.
2. The script identifies the algorithm based on the hash length.
3. It hashes each password from `rockyou.txt` using the identified algorithm.
4. If a match is found, the original password is printed.

---

## 📁 Requirements

- Python 3.x
- `rockyou.txt` wordlist (included in the repository)

---

## 💻 Usage

```bash
python3 hash_cracker.py
