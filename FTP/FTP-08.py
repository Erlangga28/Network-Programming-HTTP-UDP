from ftplib import FTP
from ftplib import FTP_TLS

f = FTP()
f.set_pasv(False)
ff = FTP_TLS()

f.connect(host='127.0.0.1')
res = f.getwelcome()
print(res.split('\n',1)[-2])

res = f.sendcmd("User Erlangga")

res = f.sendcmd("PASS 1234")

res = f.rmd("test2")
print(res)

res = f.sendcmd("QUIT")