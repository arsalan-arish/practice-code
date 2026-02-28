from random import seed, randint, shuffle
from pathlib import Path

p = Path('test.jpg')

class File_Encryption:
    def __init__(self):
        self.key: int = None
        self.file: str | Path = None
        self.permutation: list = None

    def _set_seed(self, key: int):
        """Set the random module seed using the key for reproducible shuffling."""
        seed(key)

    def _generate_key(self):
        """Generate a random 8-bit key (1-255) for encryption."""
        self.key = randint(1, 255)

    def _embed_key(self, file: bytearray):
        """Hide the 8-bit key in LSBs of first 8 bytes"""
        for i in range(8):
            file[i] = (file[i] & ~1) | ((self.key >> (7 - i)) & 1)

    def _extract_key(self, file: bytearray):
        """Extract the 8-bit key in LSBs of first 8 bytes of the file bytes"""
        return sum((file[i] & 1) << (7 - i) for i in range(8))

    def encrypt(self, input_filePath: str | Path, output_filePath: str | Path):
        """
        Encrypt the file:
        1. Generate a key, and set seed.
        2. XOR each byte with the key.
        3. Shuffle bytes using permutation derived from key.
        4. Hide key in LSBs of first 8 bytes and save original first 8 bytes at the end.
        5. Save encrypted file.
        """
        self._generate_key(); self._set_seed(self.key)
        self.file = bytearray(Path(input_filePath).read_bytes())

        # XOR each byte with key
        xorred = bytearray(byte ^ self.key for byte in self.file)

        # Shuffle bytes
        permutation = list(range(len(self.file)))
        shuffle(permutation)
        shuffled = bytearray(xorred[i] for i in permutation)

        # Save the first 8 bytes separately by extending them to the end of file, so that key embedding does not corrupt them
        shuffled.extend(shuffled[:8])

        # Hide the key in first 8 bytes
        self._embed_key(shuffled)
        
        result = shuffled
        # Save encrypted file
        Path(output_filePath).write_bytes(bytes(result))

    def decrypt(self, input_filePath: str | Path, output_filePath: str | Path):
        """
        Decrypt the image:
        2. Extract key from first 8 bytes, and set seed.
        3. Restore uncorrupted first 8 bytes into the shuffled data.
        5. Unshuffle bytes with inverse permutation.
        6. XOR each byte with key.
        8. Save decrypted image.
        """
        self.file = bytearray(Path(input_filePath).read_bytes())
        
        # Extract key and set seed
        self.key = self._extract_key(self.file); self._set_seed(self.key)

        # Restore the original first 8 bytes from the end of the file to their positions and then remove them
        self.file[:8] = self.file[-8:]; self.file = self.file[:-8]

        # Reconstruct the original permutation
        permutation = list(range(len(self.file)))
        shuffle(permutation)
        
        # Create inverse permutation mapping
        inverse_permutation = [0] * len(permutation)
        for i, p in enumerate(permutation):
            inverse_permutation[p] = i

        # Unshuffle using inverse permutation
        unshuffled = bytearray(self.file[i] for i in inverse_permutation)

        # XOR to decrypt
        xorred = bytearray(byte ^ self.key for byte in unshuffled)

        result = xorred
        # Save decrypted image
        Path(output_filePath).write_bytes(bytes(result))


img_crypto = File_Encryption()

# Encrypt an image
img_crypto.encrypt('test.jpg', 'encrypted.jpg')

# Decrypt an image
img_crypto.decrypt('encrypted.jpg', 'decrypted.jpg')