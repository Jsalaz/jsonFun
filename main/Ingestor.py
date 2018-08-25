import argparse
import json
import pprint

filename="Ingest_List.json"
directory="C:/Users/j_sal/git/Ingest"


class Ingest(object):
    def __init__ (self, stream, myvars:dict):
        self.source_name = myvars['Source_Name']
        self.source_dir = myvars['Source_Directory']
        self.s3_name = myvars['Destination_Name']
        self.s3_dir = myvars['Destination_Directory']
        self.action_list = myvars['Actions_List']
        self.stream = stream


    def print_vars(self):
        print(self.stream)
        print(self.source_name)
        print(self.source_dir)
        print(self.s3_name)
        print(self.s3_dir)
        print(self.action_list)
        
    
    def action_manager(self):
        return None


    def ftp_download (self):
        #create subprocess that will run the lftp process with a Linux script
        print("ftp_download.sh",
            f'"{self.source_name}"',
            f'"{self.source_dir}"',
            f'"{self.s3_name}"',
            f'"{self.s3_dir}"'
        )

#User specifies the json file to be parsed
def read_args ():
    print("Read Args")
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', nargs=1, help="JSON Filename", type=argparse.FileType('r'))
    arguments = parser.parse_args()
    js = json.load(arguments.filename[0])
    pprint.pprint(js)
    return js


#Reads filename var declared at top
#No longer works but keeping for future testing
def read_json ():
    print("Read JSON")
    with open(filename) as fn:
        js1 = json.load(fn)
        pprint.pprint(js1)
    return js1


def process_work(myvars):
    print("--- Process Work ---")
    for k,v in myvars.items():
        print("Processing Stream :", k)
        ingest = Ingest(k,v)
        ingest.print_vars()
        ingest.action_manager()
        ingest.ftp_download()
        #work_manager(k, v)
        # for key, val in v.items():
        #     print(key, ":", val)
        #     print("Value:", val)


#Not in use
def work_manager(stream, myvars:dict):
    print("Work Manager")
    print("ftp_download", myvars['Source_Name'])
    vals = list (myvars.values())
    keys = myvars.keys()
    print("Keys", keys)
    print("Values", vals)

def main():
    print(__name__,"Main")
    process_work(read_args())
#    process_work(read_json())

if __name__ == '__main__':
    main()