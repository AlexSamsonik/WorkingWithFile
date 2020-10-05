import os

TEMP_DIRECTORY = os.path.join("/tmp", "temp_directory")

FILE_NAME = "file_name.txt"
FILE_NAME_CONTEXT = "Easier to ask the forgiveness than permission."

FILE_OWNER = "file_owner.txt"
UID = os.getuid()  # 1000
GID = os.getgid()  # 1000

FILE_NOBODY_OWNER = "file_nobody_owner.txt"
UID_NOBODY = 65534
GID_NOBODY = 65534

MODE_644 = "644"

LIST_FILE_NAME = ["linux.txt", "windows.rtf", "macOS.doc", FILE_NAME, FILE_OWNER, FILE_NOBODY_OWNER]
