import os

path = './bin/8.0/release/rodinia-3.1/'
file_list = os.listdir(path)
for file in file_list:
#    mv_cmd = 'mv ' + path+'/'+file + ' '+ path+'/'+file_
#    os.system(mv_cmd)
	dir_name = path  + file 
	if file == 'srad_v1' or file =='srad_v2':
		run_path= './src/cuda/rodinia/3.1/cuda/srad/'
		cpy_run = 'cp ' + run_path + file +'/run' + ' ' + dir_name +'/.'
	elif file == 'particlefilter_float' or file == 'particlefilter_naive':
		run_path = './src/cuda/rodinia/3.1/cuda/particlefilter/particlefilter/'
		print(run_path)
		cpy_run = 'cp ' + run_path + file +'/run' + ' ' + dir_name +'/.'
	else:	
		run_path = './src/cuda/rodinia/3.1/cuda/'
		cpy_run = 'cp ' + run_path + file +'/run' + ' ' + dir_name +'/.'
	os.system(cpy_run)
