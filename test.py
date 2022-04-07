import subprocess
# from sub_process_sample import printsomething
# from subprocess import check_output



import os
os.environ['COVERAGE_PROCESS_START'] = ".coveragerc"


def test_via_subproc():
    proc = subprocess.Popen(["python3", "sub_process_sample.py", "-v"])
    # out = check_output(["python3", "sub_process_sample.py", "-v"])
    # print(out)
    proc.wait()
    # printsomething()