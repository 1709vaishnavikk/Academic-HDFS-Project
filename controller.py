from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from hdfs import InsecureClient
import os

BLOCK_SIZE = 64 * 1024  # Block size for splitting files
KEY = b'ThisIsASecretKey'  # 16-byte AES key

# Establish connection with the HDFS Web interface
client = InsecureClient('http://172.17.68.107:9870', user='hadoopuser')  # Adjust user if necessary

def encrypt_and_upload(file_path):
    """
    Encrypts a file in blocks and uploads them to HDFS.
    Each block is encrypted using AES CBC with a new IV.
    The IV is prepended to the ciphertext before upload.
    """
    index = 0
    with open(file_path, 'rb') as file:
        while chunk := file.read(BLOCK_SIZE):
            cipher = AES.new(KEY, AES.MODE_CBC)
            encrypted = cipher.encrypt(pad(chunk, AES.block_size))
            iv = cipher.iv                    # Prepend IV to the ciphertext

            hdfs_path = f"/cloud/{os.path.basename(file_path)}_part{index}.enc"
            with client.write(hdfs_path, overwrite=True) as writer:
                writer.write(iv + encrypted)
            print(f"✅ Uploaded: {hdfs_path}")
            index += 1

def download_and_decrypt(file_prefix, block_count, output_file):
    """
    Downloads encrypted blocks from HDFS and reconstructs the original file.
    Extracts the IV from each block and decrypts using the original AES key.
    """
    with open(output_file, 'wb') as output:
        for i in range(block_count):
            hdfs_path = f"/cloud/{file_prefix}_part{i}.enc"
            with client.read(hdfs_path) as reader:
                data = reader.read()
                iv = data[:16]                # First 16 bytes are IV
                ct = data[16:]                # Rest is ciphertext

                cipher = AES.new(KEY, AES.MODE_CBC, iv)
                pt = unpad(cipher.decrypt(ct), AES.block_size)
                output.write(pt)
            print(f"✅ Downloaded and decrypted: {hdfs_path}")
