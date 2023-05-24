from ftplib import FTP
from ftplib import FTP_TLS

f = FTP()
f.set_pasv(False)
ff = FTP_TLS()

f.connect(host='127.0.0.1')
res = f.getwelcome()
print(res.split('\n',1)[-2])

res = f.sendcmd("User rangga")
print(res)

res = f.sendcmd("PASS ranggaaja")
print(res)

res = f.sendcmd("SYST")
print(res)

res = f.sendcmd("QUIT")
print(res)
