import argparse
import os
import ftplib

def ftp_list_file():
    print("Inside FTP Script")
    return None


def ftp_download_file():
    return None


def ftp_download_multiple():
    return None


def ftp_list_delete():
    return None
    

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filepattern", help="file name or pattern")
    parser.add_argument("-d", "--directory", help="file source/directory")
    parser.add_argument("-u", "--user", help="application or user ID")
    parser.add_argument("-p", "--password", help="password")
    parser.add_argument("-s", "--server", help="ftp server")
    
    arguments = parser.parse_args()


if __name__ == "__main__":
    ftp_list_file()