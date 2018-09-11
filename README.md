Thoughts on workflows:

Ingestor/Manager:
    1. Picks up the configuration files
    2. Iterates through the Ingest_List
        a. Gets list of Files to download from OnPrem
        b. Downloads files from OnPrem to Ec2 from list
        c. Renames the files if required
        d. Uploads files to Aws
            i. Updates Online Tracker based on md5 hash?
        e. Moves OnPrem File to Archive if required
        f. Deletes File from OnPrem if required
        g. Deletes File from Ec2 if required
    3. Uploads Log File & Tracker


ftp_download:
    1. Installs LFTP
    2. Runs LFTP commands based on Ingestor's commands
        a. List Files on server
        b. Download files
        c. Move files
        d. Delete files


s3_download:
    1. Uploads object
        a. Regular Upload
        b. Multipart Uploads
    2. Moves Object
    3. Deletes Object (for corrections)




Configuration Files:
    1. Ingest_List, which will have information about:
        a. File stream
        b. Source_Name_Pattern
        c. Source_Directory
        d. Actions_List: LFTP and S3 actions?
        e. Destination_Name
        f. Destination_Directory
    2. Region Properties File, which will have information about:
        a. Aws configurations
            i. AWS account to run in
            ii. Bucket name
            iii. KMS Keys
        b. OnPrem configurations
            i. Application Ids
            ii. Application passwords
