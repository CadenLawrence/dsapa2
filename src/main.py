
import sys,string,random,binascii

def encrypt():
    secret_key = get_key()
    plain_text = get_text()
    f= open("./data/ciphertext.txt","w+")
    if(len(secret_key)!=len(plain_text)-1):
        return f.write('')
        raise Exception('length is incorrect!')
    else:
        sum = bin(int(secret_key,2) + int(plain_text,2))
        
        print(sum[2:])
        return f.write(str(sum))

def decrypt():
    secret_key = get_key()
    cipher_text = get_cipher_text()
    sum = bin(int(cipher_text,2)-int(secret_key,2))
    result = int(sum,2).to_bytes((int(sum,2).bit_length() + 7) // 8, 'big').decode()
    f= open("./data/result.txt","w+")
    print(result)
    return f.write(result)

def key_generator():
    lamb = input('How many bits do you want it to be? ')
    chars = int(lamb)/int(8)
    f= open("./data/newkey.txt","w+")
    if type(chars) is float:
        random_key = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(int(chars))])
        print(random_key)
        f.write(random_key)
    else:
        f.write('')
        raise TypeError('needs to be type float')
    

def get_key():
    sk=open("./data/key.txt", "r")
    secret_key = sk.read()
    if(len(secret_key)==32):
        return secret_key
    else:
        raise Exception('secret key needs to be equal to 32 bits')
    
def get_text():
    pt=open("./data/plaintext.txt", "r")
    nonbinary_plaintext = pt.read()
    #converts plaintext to binary
    plain_text = bin(int.from_bytes(nonbinary_plaintext.encode(), 'big'))
    return plain_text

def get_result():
    rt=open("./data/result.txt", "r")
    result_text = rt.read()
    return result_text

def get_cipher_text():
    ct=open("./data/ciphertext.txt", "r")
    cipher_text = ct.read()
    return cipher_text



if __name__ == '__main__':
    globals()[sys.argv[1]]()