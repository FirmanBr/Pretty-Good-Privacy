from django.db import models

class PairKeyReq(models.Model):
    id          = models.AutoField(primary_key=True)
    fullname    = models.CharField(max_length=100)
    purpose     = models.CharField(max_length=100,null=True)
    email       = models.CharField(max_length=100)   
    keytype     = models.CharField(max_length=100)  
    keysize     = models.CharField(max_length=100)  
    passphrase  = models.CharField(max_length=100)  
    privkey     = models.TextField(null=True)    
    pubkey      = models.TextField(null=True)  
    datehistory = models.DateTimeField(null=False)
    expires     = models.DateTimeField(null=False)

    class Meta:
        managed = True
        db_table = 'kunci'