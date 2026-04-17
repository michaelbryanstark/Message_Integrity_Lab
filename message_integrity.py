# message integrity
import hashlib

content = input("Enter a word to be encrypted \n==> ")
# Generate hash
hash_object = hashlib.sha256(content.encode('utf-8'))
hex_dig = hash_object.hexdigest()

print(f"Hashed String: {hex_dig}")

# Original hashed content storage
original_hash = hex_dig

# Content to verify
verify_data = content
verify_hash = hashlib.sha256(verify_data.encode('utf-8')).hexdigest()

# Compare the hashes
if verify_hash == original_hash:
    print("Integrity verified, message not altered")
else:
    print("Alert! Someone has been tampering the with the code!")
