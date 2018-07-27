import json
import re
import traceback

class dataPrep(object):
    def __init__(self):
        self.mappings = json.load(open("data_class_mapping.json","r"))
        

    def findMapp(self, df):
        try:
            all_columns = list(df)
            for each_col in all_columns:
                if not each_col in self.mappings.keys():
                    continue
                df[each_col] = list(map(lambda x : self.mappings[each_col][x], df[each_col]))
        except:
            print "Error in findMapp",traceback.format_exc()
        return df



if __name__ == '__main__':
    dp_obj = dataPrep()