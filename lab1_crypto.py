import base64
from itertools import cycle

def caesar_shift(text, shift):
    result = []
    for ch in text:
        if 'a' <= ch <= 'z':
            result.append(chr((ord(ch)-97 + shift) % 26 + 97))
        elif 'A' <= ch <= 'Z':
            result.append(chr((ord(ch)-65 + shift) % 26 + 65))
        else:
            result.append(ch)
    return ''.join(result)

def brute_force_caesar(ciphertext):
    results = []
    for s in range(26):
        results.append((s, caesar_shift(ciphertext, s)))
    return results

def repeating_key_xor(data_bytes, key_bytes):
    return bytes([b ^ k for b, k in zip(data_bytes, cycle(key_bytes))])

def main():
    # Part 1: Caesar full sentence
    cipher1 = "Hvs Eiwqy Pfckb Tcl Xiadg Cjsf Hvs Zonm Rcu."
    print("=== Caesar brute-force for cipher1 ===")
    for s, p in brute_force_caesar(cipher1):
        print(f"shift {s:2d}: {p}")
    print("\n(Find which line is proper English; likely 'The Quick Brown Fox Jumps Over The Lazy Dog.')\n")

    # Part 2: Small Caesar challenge
    cipher2 = "mznxpz"
    print("=== Caesar brute-force for cipher2 (mznxpz) ===")
    candidates = brute_force_caesar(cipher2)
    for s, p in candidates:
        print(f"shift {s:2d}: {p}")
    print("\n(We see shift=5 -> 'rescue'. Rearrange 'rescue' -> 'secure' (passphrase).)\n")

    # Part 3: XOR decryption
    b64_ct = "Jw0KBlIMAEUXHRdFKyoxVRENEgkPEBwCFkQ="
    ct_bytes = base64.b64decode(b64_ct)
    passphrase = "secure"  # recovered from step 2
    pt_bytes = repeating_key_xor(ct_bytes, passphrase.encode('ascii'))
    print("Base64 decoded ciphertext (hex):", ct_bytes.hex())
    print("Using passphrase:", passphrase)
    try:
        print("Decrypted plaintext:", pt_bytes.decode('utf-8'))
    except UnicodeDecodeError:
        print("Decrypted bytes (hex):", pt_bytes.hex())

if __name__ == "__main__":
    main()
