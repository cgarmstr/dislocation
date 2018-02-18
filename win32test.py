import win32com.client
import sys

print("Python version {}".format(sys.version))
o = win32com.client.Dispatch("Excel.Application")
o.Visible = 1
o.Workbooks.Add() # for office 97 ? 95 a bit different!
o.Cells(1,1).Value = "Hello"
