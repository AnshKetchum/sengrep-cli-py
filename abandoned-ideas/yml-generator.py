from csv import reader
import yaml
import json

def splitrow(row, DELIMETER):
    x = row.split(DELIMETER)
    return ([] if row == '' else x)

def get_data_from_csv(settings, DELIMETER = '|'):

    rules = []
    with open(settings['CSV_FILENAME'], 'r') as csv_file:
        csv_reader = reader(csv_file)

        for row in csv_reader:
            bug_id = row[0]
            pattern_either = splitrow(row[1], DELIMETER)
            pattern_inside = splitrow(row[2], DELIMETER)
            pattern_not_inside = splitrow(row[3], DELIMETER) 
            languages = splitrow(row[4], DELIMETER)
            message = row[5]
            severity = row[6]

            patterns = { "pattern-either": {"pattern":patt for patt in pattern_either} , 
                         "pattern-not-inside" : { "pattern": patt for patt in pattern_not_inside },
                         "pattern-inside" : {"pattern" : patt for patt in pattern_inside}, 
            }

            patterns = {k: v for k, v in patterns.items() if v}

            
            single_rule_obj = { "id" : bug_id, "patterns" : patterns, "message" : message, "languages" : languages, "severity" : severity            }
            rules.append(single_rule_obj)
            return {"rules" : rules}

def convert_json_to_yaml(yml_dict, settings):
    with open(settings['OUTPUT_FILENAME'], 'w') as ymlfile:
        yaml.dump(yml_dict, ymlfile, allow_unicode=True)

def go(config_filename = 'yml-generator-config.json'):
    with open(config_filename, 'r') as json_file:
        settings = json.load(json_file)
        yml_dict = get_data_from_csv(settings, settings['DELIMETER'])
        convert_json_to_yaml(yml_dict, settings)

go()

