"""GITI9072-e"""
"""Maribel Vargas Exiga"""
"""Daniela Alejandra Vargas Palomino"""

import ftplib

def list_files():
    ftp_client = ftplib.FTP('www.kernel.org', 'anonymous', 'danyale@hotmail.com')
    ftp_client.cwd('/pub/linux/kernel/u4.x')
    files = ftp_client.dir()
    print (files)

    changelogFile = open('ChangeLog-4.0.1.txt', 'wb')
    
    ftp_client.retrbinary('RETR ChangeLog-4.0.1', changelogFile.write)
    chengelogFile.close()
    ftp_client.quit()

if __name__ == '__main__':
    list_files()
    
