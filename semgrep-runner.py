#Runs the semgrep command
import sys # Get args from command line
import subprocess #Use the command 
import json
import os 
import glob
import shutil

'''
Ex of Calling Script: 
python3 semgrep-runner.py 

MAKE SURE THAT THE RUNNER CONFIG FILE IS SETUP IN THE SAME DIRECTORY
OR PASS THE DIRECTORY WITHIN THE go() METHOD!!!

'''



def run_semgrep(filename, config, output_filename, verbose = True):
    '''
        filename: the filename of the src file that needs to be checked (test.py, test.java)
        config: A YML file containing the rules Semgrep will follow 
    '''

    #Getting data from semgrep
    if verbose: 
        print('Getting data from Semgrep ...')

    process = subprocess.Popen(f'semgrep --config={config} {filename}', shell = True, stdout = subprocess.PIPE )
    output  = process.stdout.read().strip()
    output  = output.decode('UTF-8')

    #Outputting Sengrep's output to the output file specified

    with open(output_filename, 'a') as f:
        print(f'Semgrep Report for {filename}\n', file=f)
        print(output, file =f)
        print(f'\n\n', file=f)
    
    if verbose:
        print(f'A file {output_filename} has been sucessfully created!')
        print(f'End Semgrep Runner')

def process_yml(yml_file, yml_file_path, settings):
    '''
        Load the directories where the fields 

    '''
    print('Processing: ', yml_file, yml_file_path)


    output_file_path = os.path.join(settings['RUNNER_OUTPUT_DIRECTORY'], f'runner_output_{yml_file[0:yml_file.find(".yml")]}.txt') 


    for path in settings['RUNNER_TEST_FILE_INPUT_DIRECTORIES']:
        for file_extension in settings['FILE_EXTENSIONS_TO_LOOK_FOR']:
            for test_filename in glob.glob(f'{path}/*.{file_extension}'):
                print(test_filename)
                run_semgrep(test_filename, yml_file_path, output_file_path, settings['shouldOutputBeVerbose'] == 'True')


def go(JSON_SETTINGS_FILE_PATH = 'runner_config.json'):
    '''
        Load all the settings stored in the JSON_SETTINGS_FILE_PATH
        configuration file and call each of the methods
    '''

    with open(JSON_SETTINGS_FILE_PATH, "r") as json_file:
        settings = json.load(json_file)

        if os.path.exists(settings['RUNNER_OUTPUT_DIRECTORY']):
            shutil.rmtree(settings['RUNNER_OUTPUT_DIRECTORY'])
        os.mkdir(settings['RUNNER_OUTPUT_DIRECTORY'])



        for yml_path in settings['RUNNER_INPUT_YML_DIRECTORIES']:
            for filename in glob.glob(f'{yml_path}/*.yml'):
                directory, file_name = os.path.split(filename)
                process_yml(file_name, filename, settings)



go()
    
    
