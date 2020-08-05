#  set up the theano config file to use gpu by default
{
    echo -e "\n[global]\nfloatX=float32\ndevice=gpu"
    echo -e "[mode]=FAST_RUN"
    echo -e "\n[nvcc]"
    echo -e "fastmath=True"
    echo -e "\n[cuda]"
    echo -e "root=/usr/local/cuda" 
}>> ~/.theanorc