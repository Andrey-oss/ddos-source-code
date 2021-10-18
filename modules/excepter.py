from modules.color_text import *
from modules.logo import logo

def return_error(error):
    fix = str(error).replace('No module named', '').replace("'", "").replace("", "")
    logo()
    print (f'''
     {NORMAL}NAME      OUTPUT
     ==========================
    {NORMAL} EXIT BY:  {RED}ModuleNotFoundError
    {NORMAL} ERROR:   {RED} {error}
    {NORMAL} FIX:   {GREEN}   pip3 install{fix}
    {NORMAL} REASON:   {RED}Module{fix} is not installed
    ''')
    exit()
