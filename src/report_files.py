import os
import pandas as pd
from ydata_profiling import ProfileReport

def handle_files(file_list, save_path, format, resultado):
    try:
        for file in file_list:
            new_name = file.split('/')[-1].split('.')[0]

            resultado.insert("end", "lendo arquivo: " + new_name + "." + format)

            # transforma arquivo em dataframe
            if format == '.xlsx':
                df = pd.read_excel(file)
            elif format == '.csv':
                df = pd.read_csv(file)
            elif format == '.parquet':
                df = pd.read_parquet(file)   
            
            # faz o profile do df
            profile = ProfileReport(df, title="Profiling Report")

            # salva o report em html
            profile.to_file(save_path + new_name + "_report.html")
    except Exception as e:
            output_error = "error: " + str(e)
            resultado.insert("end", output_error)