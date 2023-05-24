from ftplib import FTP

f = FTP()
serv = f.connect(host='localhost')
serv_name = serv.split('-')[-2]
serv_status = serv_name.split('-')[0]
print(serv_status)