# update software
sudo apt-get update
sudo apt-get -y dist-upgrade

# install dependencies
sudo apt-get install -y gcc g++ gfortran build-essential \
    git wget linux-image-generic libopenblas-dev \
    python-dev python-pip ipython python-nose\
    python-numpy python-scipy

# install bleeding edge theano
sudo pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

# get CUDA
sudo wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1404/x86_64/cuda-repo-ubuntu1404_7.0-28_amd64.deb

# depackage and install CUDA
sudo dpkg -i cuda-repo-ubuntu1404_7.0-28_amd64.deb
sudo apt-get update
sudo apt-get install -y cuda

# update PATH variables
{
    echo -e "\nexport PATH=/usr/local/cuda/bin:$PATH"
    echo -e "\nexport LD_LIBRARY_PATH=/usr/local/cuda/lib64"
} >> .bashrc

# reboot for CUDA
sudo reboot