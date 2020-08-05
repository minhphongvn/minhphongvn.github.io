# install included samples and test cuda
ver=$(echo ${f%%.sh} | tail -c -4) # get version number
echo "CUDA version: ${ver}"
/usr/local/cuda/bin/cuda-install-samples-${ver}.sh ~/
cd NVIDIA\_CUDA-${ver}\_Samples/1\_Utilities/deviceQuery
make
./deviceQuery