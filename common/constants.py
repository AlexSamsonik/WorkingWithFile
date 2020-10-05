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

MODE_400 = "400"
MODE_644 = "644"

PERMISSION_MSG = "Operation not permitted"

FILE_READ_ONLY = "file_read_only.txt"

LIST_FILE_NAME = ["linux.txt", "windows.rtf", "macOS.doc", FILE_NAME, FILE_OWNER, FILE_NOBODY_OWNER, FILE_READ_ONLY]
