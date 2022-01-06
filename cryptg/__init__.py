from tgcrypto import ige256_decrypt as decrypt_ige
from tgcrypto import ige256_encrypt as encrypt_ige
from tgcrypto import ctr256_encrypt as encrypt_ctr
from tgcrypto import ctr256_decrypt as decrypt_ctr
__all__ = [
    "decrypt_ige",
    "encrypt_ige",    
    "encrypt_ctr",
    "decrypt_ctr"
    ]
