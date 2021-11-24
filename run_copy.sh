rm -rf data_dirs
rm -rf benchmarks/data_dirs
rm -rf uvm_benchmarks/data_dirs

cat datas/data.tar.gz* | tar zxvf -

cp -r data_dirs benchmarks
cp -r data_dirs uvm_benchmarks
rm -rf data_dirs
