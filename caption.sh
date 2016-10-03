#!/bin/bash

# go to neuraltalk2 path
cd ~/projects/openCon/neuraltalk2

# edit your model-path 
th eval.lua -model ~/model/cpu_model_id1-501-1448236541.t7_cpu.t7 -image_folder $1 -gpuid -1 -num_images -1
