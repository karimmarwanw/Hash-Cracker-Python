import hashlib


def identify_hash(hash_string):
    length = len(hash_string)
    if length == 32:
        return "md5"
    elif length == 40:
        return "sha1"
    elif length == 64:
        return "sha256"
    elif length == 96:
        return "sha384"
    elif length == 128:
        return "sha512"
    else:
        return None

def hash_password(password, algo):
    password = password.strip().encode()
    if algo == "md5":
        return hashlib.md5(password).hexdigest()
    elif algo == "sha1":
        return hashlib.sha1(password).hexdigest()
    elif algo == "sha256":
        return hashlib.sha256(password).hexdigest()
    elif algo == "sha384":
        return hashlib.sha384(password).hexdigest()
    elif algo == "sha512":
        return hashlib.sha512(password).hexdigest()
    else:
        return None

def bruteforce(hashh):
    algo = identify_hash(hashh)
    print("hash algo is:", algo)
    with open("rockyou.txt", "r", encoding="latin-1") as file:
        for password in file:
            password = password.strip()
            hashed_password = hash_password(password, algo)
            if hashed_password == hashh:
                print("Password found", password)
                break
        else:
            print("Password not found, try again")

def main():
    while True:
        hashh = input("Hash (or press Enter to exit): ").strip()
        if hashh == "":
            break
        bruteforce(hashh)

if __name__ == "__main__":
    main()
