# !/usr/bin/env python3

import os
from glob import glob

def generate_seg_script(filepattern, model, out_seg_dir, out_script_file):
    # spm_encode --model =./ xxx.model - -output_format = piece <./ file_0_0.txt >./ file_0_0_seg.txt
    script_file = out_script_file
    outdir = out_seg_dir
    os.makedirs(outdir, exist_ok=True)
    infiles = glob(filepattern)
    cmd_list = []
    for infile in infiles:
        outfile = os.path.join(outdir, os.path.basename(infile))
        cmd = 'spm_encode --model={} --output_format=piece <{} >{}'.format(model, infile, outfile)
        cmd_list.append(cmd)
    with open(script_file, 'w') as f:
        f.write('\n'.join(cmd_list))