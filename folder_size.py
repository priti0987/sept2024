# import os
# import shutil
#
# oldpath = "C:\\Users\\Dell\\Downloads"
# ad = os.listdir(oldpath)
# for i in ad:
#     if i.__contains__(".pdf"):
#         print(i)
#         MYDIR = "C:\\Users\\Dell\\Downloads\\pdf"
#         CHECK_FOLDER = os.path.isdir(MYDIR)
#
#         if not CHECK_FOLDER:
#             os.makedirs(MYDIR)
#             print("created folder : ", MYDIR)
#
#         else:
#             print(MYDIR, "folder already exists.")
#             shutil.move(oldpath+"\\"+i,MYDIR+"\\"+i)

import os

path_1 = "C:\\13March"
# for i in os.listdir(path_1):
#     print(path_1 + "\\"+i)

print(os.path.getsize(path_1))
