import os
import subprocess


python_files = os.popen('find "(cd ..; pwd)" -name "*.py" -and -not -name "test_*.py" -and -not -name "mut.py"')
python_output = python_files.read()

test_files = os.popen('find "(cd ..; pwd)" -name "test_*.py" -and -not -name "mut.py"')
test_output = test_files.read()

for files, tests in zip(sorted(python_output.strip().split('\n')),
                        sorted(test_output.strip().split('\n'))):
    print(f'mut.py --target {files} --unit-test {tests} --runner pytest --coverage')
    # os.system(f'mut.py --target {files} --unit-test {tests} --runner pytest --coverage')

    process = subprocess.Popen([f'mut.py --target {files} --unit-test {tests} --runner pytest'],
                               stdout=subprocess.PIPE,
                               universal_newlines=True)

    while True:
        output = process.stdout.readline()
        print(output.strip())
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
            # Process has finished, read rest of the output
            for output in process.stdout.readlines():
                print(output.strip())
            break
