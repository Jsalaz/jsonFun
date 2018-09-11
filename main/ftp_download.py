import argparse
import os
import subprocess

# lftp  $PROTOCOL://$URL <<- DOWNLOAD
#     user $USER "$PASS"
#     cd $REMOTEDIR
#     mget -E $REGEX
# DOWNLOAD
LFTP_INSTALLED = False


def run_command(command):
    return_code = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return return_code


def fetch_command(command, *args):
    if args == ():
        args = (None, None)
    command_dict = {
        "CheckInstall": ["which", "lftp"],
        "InstallLFTP": ["sudo", "yum", "-y", "install", "lftp"],
        "FetchPassword" ["sudo", "jsia"]
        "ListFiles": ["lftp", "-u", args[0], "-p", args[1]],
        "DownloadFile": ["lftp", "-u", args[0], "-p", args[1]],
        "DownloadMultiple": ["lftp", "-u", args[0], "-p", args[1]],
        "DeleteFile": ["lftp", "-u", args[0], "-p", args[1]],
        "MoveFile": ["lftp", "-u", f"{args[0]},{args[1]}"]
    }
    return command_dict[command]


def install_ftp():
    # check if lftp is installed
    if not LFTP_INSTALLED:
        command = fetch_command("CheckInstall")
        print(command)
        # rc = run_command(fetch_command("CheckInstall"))
        # if rc.returncode == 0:
        #     LFTP_INSTALLED = True
        #     return
        #  install lftp
        command = fetch_command("InstallLFTP")
        print(command)
        # #rc = run_command(fetch_command("CheckInstall"))
        # if rc.returncode == 0:
        #     return rc.stdout
        # else:
        #     return rc.stderr


def ftp_list_file(ftp_args):
    print("- Ftp List -")
    command = fetch_command("ListFiles")
    print(command)
    return None


def ftp_download_file():
    print("- Ftp Download -")
    command = fetch_command("DownloadFile")
    print(command)
    return None


def ftp_download_multiple():
    print("- Ftp Download Multi -")
    command = fetch_command("DownloadMultiple")
    print(command)
    return None


def ftp_delete():
    print("- FTP_Delete -")
    command = fetch_command("DeleteFile")
    print(command)
    return None


def move_file():
    print("- FTP_Move -")
    command = fetch_command("MoveFile")
    print(command)
    return None


def read_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filepattern", help="file name or pattern")
    parser.add_argument("-d", "--directory", help="file source/directory")
    parser.add_argument("-u", "--user", help="application or user ID")
    parser.add_argument("-p", "--password", help="password")
    parser.add_argument("-s", "--server", help="ftp server")
    arguments = parser.parse_args()
    return arguments


if __name__ == "__main__":
    main()
    install_ftp()
    ftp_args = read_args()
    files_to_download = ftp_list_file(ftp_args)
