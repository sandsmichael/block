from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes

'''
sign a message with a private key and verify it with a public key

- calculate the hash of the message
- decrypt the signature using public key
- compare decrypted signature with calculated hash
- if they match valid, else invalid

- my private key is necesary for me to be able to sign a message that can then be verified with my public key (which itself was derived from theprivate key)
- using the same private key, a signature can be created that is unique to the message  being  assigned

'''

# Configuration
GENERATE_PRIVATE_KEY = False
DERIVE_PUBLIC_KEY_FROM_PRIVATE_KEY = False
PRIVATE_KEY_FILE = r"/Users/michaelsands/Documents/secret/xyz.pem"
PUBLIC_KEY_FILE = "./xyz.pub"
MESSAGE = b"use xyz private key to sign this message. use xyz public key to verify this message"

if GENERATE_PRIVATE_KEY:
    # Generate private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
else:
    # Load private key from pem file
    with open(PRIVATE_KEY_FILE, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )

# returns <cryptography.hazmat.backends.openssl.rsa._RSAPrivateKey object>
signature = private_key.sign(
    MESSAGE,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

if DERIVE_PUBLIC_KEY_FROM_PRIVATE_KEY:
    # Getting public key from private key
    public_key = private_key.public_key()
else:
    # Load public key from file
    with open(PUBLIC_KEY_FILE, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )

public_key.verify(
    signature,
    MESSAGE,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print(signature)

