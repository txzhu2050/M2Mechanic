import os
os.environ["OMP_NUM_THREADS"] = "1"
# Threads per process can be adjusted according to the total number of cpus.

import argparse
import sys
sys.stdout.reconfigure(line_buffering=True)
from pathlib import Path
from mpi4py import MPI

from Main import kernel

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-xml', action='store')
    parser.add_argument('-config', action='store')
    parser.add_argument('--output_dir', action='store', default='.')

    parser_args = parser.parse_args()
    xml_file = Path(parser_args.xml)
    config_file = Path(parser_args.config)
    dir_name = Path(parser_args.output_dir)

    comm = MPI.COMM_WORLD
    if comm.rank == 0:
        if not dir_name.exists():
            dir_name.mkdir(parents=True)
    comm.barrier()
    
    kernel(
        xml_file = xml_file,
        config_file = config_file,
        dir_name = dir_name,
        comm = comm
    )