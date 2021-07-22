#Runs the semgrep command
import sys # Get args from command line
import subprocess #Use the command line

'''
Ex of Calling Script: 
python3 test_file.java test.yml

'''

def run_semgrep(filename, config):
    '''
        filename: the filename of the src file that needs to be checked (test.py, test.java)
        config: A YML file containing the Rules 
    '''
    process = subprocess.Popen(f'semgrep --config={config} {filename}', shell = True, stdout = subprocess.PIPE )
    output  = process.stdout.read().strip()
    output  = output.decode('UTF-8')

    print('Output\n\n', output)
    print('\n\nActions Completed')
    return output

fname = sys.argv[1]
config = sys.argv[3]

print('Args Received')
print(fname, lang, config)

run_semgrep(fname, config)
    
