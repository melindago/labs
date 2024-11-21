from functools import wraps
import time

def caesar_encrypt(plaintext, key):
    """
    Encrypt plaintext using Caesar cipher.

    Args:
        plaintext (str): The text to be encrypted.
        key (int): The encryption key.

    Returns:
        str: The encrypted text.
    """
    return ''.join(
        chr((ord(char) - 97 + key) % 26 + 97)
        if char.isalpha()
        else chr((ord(char) + key) % 128)
        for char in plaintext.lower()
    )

def caesar_decrypt(ciphertext, key):
    """
    Decrypt ciphertext using Caesar cipher.

    Args:
        ciphertext (str): The text to be decrypted.
        key (int): The decryption key.

    Returns:
        str: The decrypted text.
    """
    return ''.join(
        chr((ord(char) - 97 - key) % 26 + 97)
        if char.isalpha()
        else chr((ord(char) - key) % 128)
        for char in ciphertext.lower()
    )

def memoize(func):
    """
    Decorator to cache function results.

    Args:
        func (function): Function to be decorated.

    Returns:
        function: Memoized function.
    """
    cache = {}

    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]

    return wrapper

def recur_fibo(n):
    """
    Standard recursive Fibonacci sequence.

    Args:
        n (int): Fibonacci sequence position.

    Returns:
        int: Fibonacci number.
    """
    if n <= 1:
        return n
    return recur_fibo(n - 1) + recur_fibo(n - 2)

@memoize
def recur_fibo_memoized(n):
    """
    Optimized Fibonacci sequence using memoization.

    Args:
        n (int): Fibonacci sequence position.

    Returns:
        int: Fibonacci number.
    """
    if n <= 1:
        return n
    return recur_fibo_memoized(n - 1) + recur_fibo_memoized(n - 2)

if __name__ == "__main__":
    print("Task 1: Caesar Cipher (Functional Programming)")
    test_plaintext = "hello WORLD"
    test_key = 3

    encrypted = caesar_encrypt(test_plaintext, test_key)
    decrypted = caesar_decrypt(encrypted, test_key)

    print(f"Plaintext: {test_plaintext}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")

    print("\nTask 2: Fibonacci Sequence with Memoization")
    n = 35

    start_original = time.time()
    result_original = recur_fibo(n)
    time_original = time.time() - start_original

    start_memoized = time.time()
    result_memoized = recur_fibo_memoized(n)
    time_memoized = time.time() - start_memoized

    print(f"Fibonacci Number for n={n}: {result_original}")
    print(f"Original Function Time: {time_original:.6f} seconds")
    print(f"Memoized Function Time: {time_memoized:.6f} seconds")
