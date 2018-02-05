# -*- coding: utf-8 -*-
# =====================
# Test module of CaCo

import main_cc as cc
import os
import yaml

# define input and output directories
prj_dir = os.path.join('..', 'caco_myprj')  # set project root (pr)
i_dir =  'input'  # pr subdir
o_dir = 'output'  # pr subdir

# get default parameters and set input/output
param3 = cc.get_param3()
param3['input_dir']  = os.path.join(prj_dir, i_dir)
param3['output_dir'] = os.path.join(prj_dir, o_dir)

# run CaCo
cc.caco_all(param3)

# save settings
with open('caco.yml', 'w') as outfile:
    yaml.dump(param3, outfile, default_flow_style=False)

