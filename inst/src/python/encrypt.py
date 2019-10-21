#!/usr/bin/python3

def protect_py(inputfile, passphrase, template):
  
    try:
        from pbkdf2 import PBKDF2
    except:
        print("install pbkdf2: \"pip install pbkdf2\"")
        exit(1)
      
    try:
        from Crypto import Random
        from Crypto.Cipher import AES
    except:
        print("install pycrypto: \"pip install pycrypto\"")
        exit(1)
      
    import os, sys
    from base64 import b64encode


    try:
        with open(inputfile, "rb") as f:
            data = f.read()
    except:
        print("Cannot open file: %s"%inputfile)
        exit(1)

    salt = Random.new().read(32)
    iv = Random.new().read(16)
    key = PBKDF2(passphrase=passphrase,salt=salt,iterations=100).read(32)

    cipher = AES.new(key, AES.MODE_CBC, IV=iv)
    padded = data.decode("utf-8", "replace")
    # workaround for padding issue https://github.com/dlitz/pycrypto/issues/277
    for i in range(16):
        try:
            encrypted = cipher.encrypt(padded)
            break
        except ValueError:
            padded += chr(0)

    with open(template) as f:
        templateHTML = f.read()

    encryptedJSON = "{\"salt\":\"%s\",\"iv\":\"%s\",\"data\":\"%s\"}"%(
        b64encode(salt).decode("utf-8"), b64encode(iv).decode("utf-8"), b64encode(encrypted).decode("utf-8"))
    
    encryptedDocument = templateHTML.replace("/*{{ENCRYPTED_PAYLOAD}}*/\"\"", encryptedJSON)
    return(encryptedDocument)

