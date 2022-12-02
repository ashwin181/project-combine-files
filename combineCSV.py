import os
import pandas as pd
import sys

'''
    function to check for empty arguments passed in command line
'''
def check_size_file_list(file_list):
    if len(file_list) == 0:
        raise Exception("Please input command line args and files")

'''
  function to check the combined csv if present otherwise delete it
'''
def is_file_exists(file_object):
    if os.path.exists(file_object):
        os.remove(file_object)

'''
   merge function for combining csv
'''
def merge_csvs(file_list):
    
    #check the size of the file list
    check_size_file_list(file_list)
    
    #fetch the last output file if it exists then delete it
    possible_output_file = file_list[::-1][0]
    print(possible_output_file)
    is_file_exists(possible_output_file)
    
    n = len(file_list)
    
    set_header = True
    
    for i in range(1,n-1):
        list_items = file_list[i].split('/')
        get_file_name = list_items[len(list_items)-1]
        
        try:
            data_in_chunks = pd.read_csv(file_list[i], chunksize=8192)
        except Exception:
            raise Exception("Error occured, corrupt file")
        
        for chunk in data_in_chunks:
            chunk['filename'] = get_file_name
            chunk.to_csv(possible_output_file, index=False, mode="a", encoding = 'utf-8', header = set_header)
    
    set_header = False
    
if __name__ == "__main__":
    merge_csvs(sys.argv)