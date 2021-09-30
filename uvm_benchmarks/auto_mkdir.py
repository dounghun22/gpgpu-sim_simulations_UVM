import os

path = './bin/8.0/release/'
file_list = os.listdir(path)
cmd = 'mkdir ' + path + 'rodinia-3.1'
os.system(cmd)

for file in file_list:
    file_ = file.replace('-rodinia-3.1', '')

#    mv_cmd = 'mv ' + path+'/'+file + ' '+ path+'/'+file_
#    os.system(mv_cmd)
    dir_name = path + 'rodinia-3.1/' + file_
    cmd = 'mkdir ' + dir_name
    os.system(cmd)
  
    mv_cmd = 'mv ' + path+ file + ' '  + dir_name + '/' + file_
    os.system(mv_cmd)

    run_path = './src/cuda/rodinia/3.1/cuda/'
    if file_ == 'srad_v1' or 'srad_v2':
	run_path= './src/cuda/rodinia/3.1/cuda/srad/'
	cpy_run = 'cp' + run_path + file_ +'/run' + ' ' + dir_name +'/.'
	
    elif file_ == 'particlefilter_float' or 'particlefilter_naive':
	run_path = './src/cuda/rodinia/3.1/cud/particlefilter/'
	cpy_run = 'cp' + run_path + file_ +'/run' + ' ' + dir_name +'/.'
    else:
    	cpy_run = 'cp' + run_path + file_ +'/run' + ' ' + dir_name +'/.'
