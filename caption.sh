#!/bin/bash

cd ~/projects/openCon/neuraltalk2

th eval.lua -model ~/model/cpu_model_id1-501-1448236541.t7_cpu.t7 -image_folder ~/iron/static/files/images_before -num_images -1
