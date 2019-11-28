
from django.shortcuts import render
from datetime import timedelta
from pgpy.constants import PubKeyAlgorithm, KeyFlags, HashAlgorithm, SymmetricKeyAlgorithm, CompressionAlgorithm

from .models import PairKeyReq
from datetime import datetime  
from datetime import timedelta 
import hashlib 
import mysql.connector
import pyautogui
import pgpy
import time


db = mysql.connector.connect(host='localhost',database='pgppki',user='root',password='')

def index(request):
    return render(request,'apps/index.html')

def cakey(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        purphose = request.POST.get('purphose')
        keytype = request.POST.get('key')
        #keysize = request.POST.get('keysize')
        keysize = "1024"
        confirmpassphrase = request.POST.get('confirmpassphrase')
        activation = request.POST.get('activation')
    

        key = pgpy.PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 1024)
        uid = pgpy.PGPUID.new(username, email=email)

        key.add_uid(uid, usage={KeyFlags.Sign}, hashes=[HashAlgorithm.SHA512, HashAlgorithm.SHA256],
                    ciphers=[SymmetricKeyAlgorithm.AES256, SymmetricKeyAlgorithm.Camellia256],
                    compression=[CompressionAlgorithm.BZ2, CompressionAlgorithm.Uncompressed],
                    key_expires=timedelta(days=1095))

        subkey = pgpy.PGPKey.new(PubKeyAlgorithm.RSAEncrypt, 1024)
        key.add_subkey(subkey, usage={KeyFlags.Authentication})
        key.protect(confirmpassphrase, SymmetricKeyAlgorithm.AES256, HashAlgorithm.SHA256)

        publkeyy = key.pubkey 

        publickey = str(publkeyy)
        privatkey = str(key)

        nowtime = datetime.now()
        expirestime =  datetime.now() + timedelta(days=1095) 

        cursor = db.cursor(buffered=True)

        sql1 = "insert into kunci(id, fullname, purpose, email, keytype, keysize, passphrase, privkey, pubkey, datehistory, expires) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = ("", username, purphose, email, keytype, keysize, confirmpassphrase, privatkey, publickey, nowtime, expirestime)

        cursor.execute(sql1,val)
        db.commit()
 
        return render(request,'apps/index.html')

    else :    
        pyautogui.alert('failed')
        return render(request,'apps/index.html')

def historykey(request):
    
    pairkey = PairKeyReq.objects.all()
    createkey = {'pairkey': pairkey} 
    
    return render(request,'apps/history.html', createkey)
