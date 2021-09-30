import os

path = './release/rodinia-3.1'
file_list = os.listdir('release')

for file in file_list:
    file_ = file.replace('-rodinia-3.1', '')

#    mv_cmd = 'mv ' + path+'/'+file + ' '+ path+'/'+file_
#    os.system(mv_cmd)
    dir_name = path + '/' + file_
    cmd = 'mkdir ' + dir_name
    os.system(cmd)
  
    mv_cmd = 'mv ' + './release/'+ file + ' '  + dir_name
    os.system(mv_cmd)
