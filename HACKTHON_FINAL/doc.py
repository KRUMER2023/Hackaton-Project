from time import strftime
import datetime,os
from docx import Document
import saveNames


# strDate = datetime.datetime.now().strftime("%d_%m_%Y")
# today=datetime.datetime.now().strftime("%A")
# # print(strDate)
# # print(today)

# folder=saveNames.get_folder()
# # print(folder)
# file=saveNames.get_dname()
# # print(file)
# ofile=file+".docx"
# # print(ofile)
# filepath=folder+"/"+ofile
# # print(filepath)

filepath=""

def set_filepath(nname):
  global filepath
  filepath=nname

def file_maker():
  global filepath
  folder=saveNames.get_folder()
  # print(folder)
  file=saveNames.get_dname()
  # print(file)
  ofile=file+".docx"
  # print(ofile)
  filepath=folder+"/"+ofile
  print(filepath)

  if os.path.isfile(filepath):
      None
  else:
    doc = Document()
    doc.save(filepath)
    
def fname():
    return (filepath)
  
def fold():
  folder=saveNames.get_folder()
  return folder