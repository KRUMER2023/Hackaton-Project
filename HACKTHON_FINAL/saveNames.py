folder="rt"
docx_name="on"
# print(type(folder))

def set_folder(fname):
    global folder
    folder=fname
    # print(folder)
    
def set_dname(dname):
    global docx_name
    docx_name=dname
    # print(docx_name)
    
def get_folder():
    # print(folder)
    return folder

def get_dname():
    # print(docx_name)
    return docx_name