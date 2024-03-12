import hashlib

def generate_hashes(text):

    hashes = {
        'md5': hashlib.md5(text.encode('utf-8')).hexdigest(),
        'sha1': hashlib.sha1(text.encode('utf-8')).hexdigest(),
        'sha256': hashlib.sha256(text.encode('utf-8')).hexdigest(),
        'sha384': hashlib.sha384(text.encode('utf-8')).hexdigest(),
        'sha512': hashlib.sha512(text.encode('utf-8')).hexdigest()
    }
    return hashes

if __name__ == '__main__':
    text = input('Enter a text: ')
    hashes = generate_hashes(text)
    print('\nHash values:')
    for algorithm, hash_value in hashes.items():
        print(f'{algorithm}: {hash_value}')