#!/bin/bash

# go to neuraltalk2 path
cd ~/projects/openCon/neuraltalk2

# export LD_LIBRARY_PATH=/home/smilu/lib/cuda/lib64:$LD_LIBRARY_PATH

# edit your model-path
th eval.lua -model ~/model/model_id1-501-1448236541.t7 -image_folder $1 -num_images -1
