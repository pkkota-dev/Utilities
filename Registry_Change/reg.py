import winreg
import argparse


print('Please select the option t0 choose the agency')
print('1-> For Case1 \n')
print('2-> For Case2 \n')
print('3-> For Case3 \n')
print('4-> For Case4 \n')

print('\n')
option = int(input('Please Enter your choince '))

if option ==1:
    dest_value='Case1'
if option ==2:
    dest_value='Case2'
if option == 3:
    dest_value='Case3'
if option ==4:
    dest_value= 'Case4'

REG_PATH= r'SOFTWARE\XYZ\ABX'
CONFIG_PATH = r'SOFTWARE\WOW6432Node\ABC\123'

configured_config = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, CONFIG_PATH,0, winreg.KEY_READ)
config_value = winreg.QueryValueEx(configured_config, 'Default')
print(config_value)

path= CONFIG_PATH + '\\'  + config_value[0]
get_key= winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path, 0, winreg.KEY_WRITE)
get_value =  winreg.SetValueEx(get_key,'REG_VAR',0, winreg.REG_SZ, dest_value)