#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      James
#
# Created:     16/07/2014
# Copyright:   (c) James 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import subprocess

import webbrowser
import time
##ff = webbrowser.get('google chrome')
##
##ff.open('www.google.com',2)


##print(type(ff))

##a = subprocess.call(r'reg query HKEY_LOCAL_MACHINE\SOFTWARE\Clients\StartMenuInternet\firefox.exe')
##
##print(a)

##import winreg
##
##HKLM = winreg.HKEY_LOCAL_MACHINE
##subkey = r'Software\Clients\StartMenuInternet'
##read32 = winreg.KEY_READ | winreg.KEY_WOW64_32KEY
##read64 = winreg.KEY_READ | winreg.KEY_WOW64_64KEY
##
##key32 = winreg.OpenKey(HKLM, subkey, access=read32)
##key64 = winreg.OpenKey(HKLM, subkey, access=read64)
### This should be true in Windows 7.
##assert winreg.QueryInfoKey(key32) == winreg.QueryInfoKey(key64)
##
####for i in range(winreg.QueryInfoKey(key64)[0]):
####    print(winreg.EnumKey(key64,i))
###print(key64)
##
##b = []
##i = 0
##while True:
##    try:
##        b += [winreg.EnumKey(key32,i)]
##        b += [winreg.EnumKey(key64,i)]
##    except EnvironmentError:
##        break
##    i += 1
##print(b)

##c = 'firefox'
##for x in range(len(b)):
##    b[x] = b[x].lower()
##
##fullpaths = []
##for i in b:
##    if i is not 'google chrome':
####        print(i)
##        temp_subkey = subkey + r'\\' + i + r'\shell\open\command'
####        print(temp_subkey)
##        key32 = winreg.OpenKey(HKLM, temp_subkey, access=read32)
##        key64 = winreg.OpenKey(HKLM, temp_subkey, access=read64)
####        print(winreg.EnumValue(key64,0)[1],end = '\n\n')



##print(c in b[0])

##webbrowser.register('firefox',None,webbrowser.WinFireFox('firefox'))

##ff = webbrowser.get('seamonkey')
####print(ff)
##ff.open('www.google.com')
##
print(webbrowser._tryorder)
print(webbrowser._browsers)
