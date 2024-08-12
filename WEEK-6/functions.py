
import logging
import os
import yaml

#for basic validation
def clean_column_names(df):
    
    # Convert column names to lowercase
    df.columns = df.columns.str.lower()
    
    # Replace any non-alphanumeric characters with underscores
    df.columns= df.columns.str.replace('[^\w]','_',regex=True)
    
    # remove any spaces
    df.columns = df.columns.str.strip()
    
    return df

#for validating columns 
def validate_columns(df, Yaml_file_name):
    # checking if the length and file names are same
    if list(df.columns) == Yaml_file_name['columns'] and len(df.columns) == len(Yaml_file_name['columns']):
        print("column name and column length validation passed")
        return 1
    else:
        if list(df.columns) != Yaml_file_name['columns']:
            print("column names are different,please check column names in the uploaded file",set((df.columns))-set(Yaml_file_name['columns']))
        if len(df.columns) != len(Yaml_file_name['columns']):
            print("columns length are differnt, please add or remove extra columns.")                    
        return 0
    
# for opening/reading Yaml File
def read_config_file(filepath):
    with open(filepath, 'r') as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as exc:
            logging.error(exc)
