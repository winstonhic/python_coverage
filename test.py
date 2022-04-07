import subprocess

import os
os.environ['COVERAGE_PROCESS_START'] = ".coveragerc"


def test_via_subproc():
    proc = subprocess.Popen(["python3", "sub_process_sample.py", "-v"])
    proc.wait()