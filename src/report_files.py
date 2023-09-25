import os
import pandas as pd
from ydata_profiling import ProfileReport


def handle_files(file_list, save_path, format, resultado):
    for file in file_list:
        try:
            separator_by_so = os.path.sep
            new_name = file.split(separator_by_so)[-1].split(".")[0]

            resultado.insert(
                "end", "gerando report do arquivo: " + new_name + "." + format + "\n"
            )

            # transforma arquivo em dataframe
            if format == ".xlsx":
                df = pd.read_excel(file)
            elif format == ".csv":
                df = pd.read_csv(file, header=0)
            elif format == ".parquet":
                df = pd.read_parquet(file)

            # faz o profile do df
            profile = ProfileReport(df, title="Profiling Report")

            # salva o report em html
            profile.to_file(
                save_path + new_name + "_report.html",
            )
        except Exception as e:
            output_error = "error: " + str(e)
            resultado.insert("end", output_error + "\n")
