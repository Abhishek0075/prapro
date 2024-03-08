import sys
from commandLine import parseCommandLineAndSum


sys.argv = ['your_script_name', '1', '2', '3', '4']
numbers, result = parseCommandLineAndSum()

def test_parseCommandLine():
    assert numbers == [1,2,3,4]

def test_summation():
    assert result == 10