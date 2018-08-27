import argparse
import json
import pprint
import os
import fnmatch as fnm
import ftp_download


#from nt import listdir

#filename="Ingest_List_3.json"
#directory="C:/Users/j_sal/git/Ingest"
#data_dir="../data/"


class Ingest(object):
    def __init__ (self, stream, myvars:dict):
        self.source_name_pattern = myvars['Source_Name_Pattern']
        self.source_dir = myvars['Source_Directory']
        self.s3_name = myvars['Destination_Name']
        self.s3_dir = myvars['Destination_Directory']
        self.action_list = myvars['Actions_List']
        self.data_dir = "../data/"
        self.stream = stream
        
        
    def rename_files(self):
        #Add another function to resolve pattern
        outfile = ""#fetch file pattern to use
        for file in os.listdir(self.data_dir):
            if fnm.fnmatch(file, self.source_name_pattern):
                os.rename(file, outfile)
                print(file)
        return None
    
    
    def s3_upload(self):
        return None


    def ftp_download (self):
        #create subprocess that will run the lftp process with a Linux script
        ftp_download.ftp_list_file()
        
        #or create python script to ftp files
        print("ftp_download.sh",
            f'"{self.source_name_pattern}"',
            f'"{self.source_dir}"',
            f'"{self.s3_name}"',
            f'"{self.s3_dir}"'
        )

    
    def print_vars(self):
        print(self.stream)
        print(self.source_name_pattern)
        print(self.source_dir)
        print(self.s3_name)
        print(self.s3_dir)
        print(self.action_list)
        
    
    def action_manager(self):
        self.ftp_download()
        if "Rename File" in self.action_list:
            self.rename_files()
        self.s3_upload()
        return None



#Not in use
def work_manager(stream, myvars:dict):
    print("Work Manager")
    print("ftp_download", myvars['Source_Name_Pattern'])
    vals = list (myvars.values())
    keys = myvars.keys()
    print("Keys", keys)
    print("Values", vals)


def process_work(myvars):
    print("--- Process Work ---")
    for k,v in myvars.items():
        print("Processing Stream :", k)
        ingest = Ingest(k,v)
        #ingest.print_vars()
        ingest.action_manager()


#Reads filename var declared at top; used for testing
def read_json ():
    print("Read JSON")
    with open(filename) as fn:
        js1 = json.load(fn)
    pprint.pprint(js1)
    return js1


#User specifies the json file to be parsed
def read_args ():
    print("Read Args")
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', nargs=1, help="JSON Filename", type=argparse.FileType('r'))
    arguments = parser.parse_args()
    js = json.load(arguments.filename[0])
    pprint.pprint(js)
    return js


def main():
    print(__name__,"Main")
    process_work(read_args())
#    process_work(read_json())

if __name__ == '__main__':
    main()