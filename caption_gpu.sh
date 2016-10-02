#!/bin/bash

cd ~/projects/openCon/neuraltalk2

export LD_LIBRARY_PATH=/home/smilu/lib/cuda/lib64:$LD_LIBRARY_PATH

th eval.lua -model ~/model/model_id1-501-1448236541.t7 -image_folder ~/iron/static/files/images_before -num_images -1
