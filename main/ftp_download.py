import argparse
import os
import subprocess

# lftp  $PROTOCOL://$URL <<- DOWNLOAD
#     user $USER "$PASS"
#     cd $REMOTEDIR
#     mget -E $REGEX
# DOWNLOAD

# Global var
LFTP_INSTALLED = False
FTP_ACTION_SET = {"FTP_list", "FTP_Download", "FTP_Download_Multiple", "FTP_Move", "FTP_Delete"}


def run_command(command):
    return_code = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return return_code


def fetch_command(command, *args):
    if args == ():
        args = (None, None)
    command_dict = {
        "FTP_CheckInstall": ["which", "lftp"],
        "FTP_Install": ["sudo", "yum", "-y", "install", "lftp"],
        "FTP_list": ["lftp", "-u", args[0], "-p", args[1]],
        "FTP_Download": ["lftp", "-u", args[0], "-p", args[1]],
        "FTP_Download_Multiple": ["lftp", "-u", args[0], "-p", args[1]],
        "FTP_Move": ["lftp", "-u", args[0], "-p", args[1]],
        "FTP_Delete": ["lftp", "-u", f"{args[0]},{args[1]}"]
    }
    return command_dict[command]


def install_ftp():
    # check if lftp is installed
    if not LFTP_INSTALLED:
        command = fetch_command("FTP_CheckInstall")
        print(command)
        # rc = run_command(fetch_command("CheckInstall"))
        # if rc.returncode == 0:
        #     LFTP_INSTALLED = True
        #     return
        ######
        #  install lftp
        command = fetch_command("FTP_Install")
        print(command)
        # #rc = run_command(fetch_command("CheckInstall"))
        # if rc.returncode == 0:
        #     return rc.stdout
        # else:
        #     return rc.stderr


def ftp_list_file(ftp_args):
    print("- Ftp List -")
    command = fetch_command("FTP_list")
    return_code = ""  # run_command(command)
    if return_code.returncode == 0:
        file_list = return_code.stdout.decode().splitlines()
    print(command)
    return file_list


def ftp_download_file():
    print("- Ftp Download -")
    command = fetch_command("FTP_Download")
    print(command)
    return None


def ftp_download_multiple():
    print("- Ftp Download Multi -")
    command = fetch_command("FTP_Download_Multiple")
    print(command)
    return None


def ftp_delete():
    print("- FTP_Delete -")
    command = fetch_command("FTP_Delete")
    print(command)
    return None


def move_file():
    print("- FTP_Move -")
    command = fetch_command("FTP_Move")
    print(command)
    return None


def process_work(file_pattern,
                 source_dir,
                 user,
                 password,
                 host,
                 actions=[]):
    install_ftp()
    for action in actions:
        command = fetch_command(action, file_pattern, source_dir, user, password, host)
        run_command(command)
    return None


def read_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filepattern", help="file name or pattern")
    parser.add_argument("-d", "--directory", help="file source/directory")
    parser.add_argument("-u", "--user", help="application or user ID")
    parser.add_argument("-p", "--password", help="password")
    parser.add_argument("-s", "--server", help="ftp server")
    parser.add_argument("-a", "--actions", help="actions to perform")
    arguments = parser.parse_args()
    return arguments


if __name__ == "__main__":
    main()
    ftp_args = read_args()
    process_work(
        ftp_args.filepattern
        ftp_args.directory
        ftp_args.user
        ftp_args.password
        ftp_args.server
        ftp_args.actions)
