import argparse
import json
import pprint
import os
import fnmatch as fnm
import ftp_download
#from nt import listdir

# filename="Ingest_List_3.json"
# directory="C:/Users/j_sal/git/Ingest"
# data_dir="../data/"

# Action Sets
FTP_Action_Set = {"FTP_Download", "FTP_Move", "FTP_Copy", "FTP_Delete"}
File_Actions = {"Rename", "Unzip"}
S3_Action_Set = {"S3_Upload", "S3_Move", "S3_Delete"}


class Ingest(object):
    def __init__(self, stream, ingest_vars: dict, config_vars: dict):
        self.stream = stream
        self.source_name_pattern = ingest_vars['Source_Name_Pattern']
        self.source_dir = ingest_vars['Source_Directory']
        self.s3_name = ingest_vars['Destination_Name']
        self.s3_dir = ingest_vars['Destination_Directory']
        self.action_list = ingest_vars['Actions']
        self.ftp_source = ingest_vars['FTP_Source']
        self.bucketname = config_vars['Bucketname']
        self.kms = config_vars['S3_KMS_ARN']
        self.app_id = config_vars['App_ID']
        self.app_vault = config_vars['App_Vault']
        self.zs_password = config_vars['ZS_Password']
        self.up_password = config_vars['UP_Password']
        self.ftp_server = config_vars['FTP_DNS']
        self.data_dir = "../data/"

    def rename_files(self):
        # Add another function to resolve pattern
        outfile = self.s3_name  # fetch file pattern to use
        for file in os.listdir(self.data_dir):
            if fnm.fnmatch(file, self.source_name_pattern):
                os.rename(self.data_dir+file, self.data_dir+outfile)
                print(file)
        return None

    def file_actions(self):
        return None

    def s3_actions(self):
        return None

    def ftp_actions(self):
        return None

    def action_manager(self):
        # No Actions
        if self.action_list == None:
            return
        # Ftp Actions
        if set(self.action_list) & FTP_Action_Set:
            # redirect to new script
            self.ftp_actions()
        # File Actions
        if set(self.action_list) & File_Actions:
            # redirect o new script?
            self.rename_files()
        # S3 Actions
        if set(self.action_list) & S3_Action_Set:
            # redirect to new script
            self.s3_actions()


def process_work(ingest_vars, config_vars):
    print("--- Process Work ---")
    for stream_name, stream_vars in ingest_vars.items():
        print("Processing Stream :", stream_name)
        ingest = Ingest(stream_name, stream_vars, config_vars)
        ingest.action_manager()


# Reads filename var declared at top; used for testing
def read_json():
    print("--- Read JSON ---")
    with open(filename) as fn:
        js1 = json.load(fn)
    pprint.pprint(js1)
    return js1


# User specifies the json file to be parsed
def read_args():
    print("--- Read Args ---")
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ingestfile", nargs=1,
                        help="Ingestion List Filename", type=argparse.FileType('r'))
    parser.add_argument("-c", "--configfile", nargs=1,
                        help="Configuration Filename", type=argparse.FileType('r'))
    parser.add_argument("-b", "--bucketname", help="S3 Bucketname")
    arguments = parser.parse_args()
    return arguments


if __name__ == '__main__':
    print(__name__, "Main")
    arguments = read_args()
    ingestfile = json.load(arguments.ingestfile[0])
    configfile = json.load(arguments.configfile[0])
    pprint.pprint(ingestfile)
    pprint.pprint(configfile)
    process_work(ingestfile, configfile)
#    process_work(read_json())
