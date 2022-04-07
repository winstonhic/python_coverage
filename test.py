import subprocess
import sub_process_sample



import os
os.environ['COVERAGE_PROCESS_START'] = ".coveragerc"


def test_via_subproc():
    proc = subprocess.Popen(["python3", "sub_process_sample.py", "-v"])
    proc.wait()