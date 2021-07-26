def get_observations(data, id, model, metric):
    # conditions
    id_c = data['id'] == id
    model_c = data['model'] == model
    filter_c = id_c & model_c
    observations = data[filter_c][metric]
    observations = observations.to_numpy()
    return observations

def get_observations_to_plot(data, id, metric):
    # conditions
    id_c = data['id'] == id
    observations = data[id_c][metric]
    return observations

from pathlib import Path, PurePosixPath

def get_pure_path(path_relative_to_home):
    path = PurePosixPath(Path.home().joinpath(path_relative_to_home))
    return path

from pandas import read_csv

def csv_to_df(csv_file_path, dtype_dict):
    with open (csv_file_path, 'rb') as file:
        data = read_csv(file, 
                        encoding = 'UTF-8',
                        decimal = '.',
                        dtype = dtype_dict)
    return data 


