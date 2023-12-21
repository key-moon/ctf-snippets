# HEADER
# name: Template for Interactive
# prefix: interactive
# description: Template for Interactive
# author: keymoon
# template: true

# VARIABLES
# script_name: ["python", "./hoge.py"]
# nc_string: nc hogenet 3141592

# BODY
from ctf import *

BIN_NAME = script_name
LOCAL = not (("REMOTE" in os.environ) or ("REMOTE" in sys.argv))

if LOCAL: stream = process(BIN_NAME)
else: stream = remote("nc_string")

#cursor

stream.interactive()
