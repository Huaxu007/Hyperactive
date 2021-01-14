# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import os
import dill
import shutil
import pandas as pd


def meta_data_path():
    current_path = os.path.realpath(__file__)
    return current_path.rsplit("/", 1)[0]


class LongTermMemory:
    def __init__(self, model_name, study_name=None, path=None, verbosity=None):
        if study_name is None:
            study_name = "default"

        model_study_name = model_name + ":" + study_name

        if path is None:
            self.model_dir = (
                meta_data_path() + "/ltm_data/" + model_study_name + "/"
            )
        else:
            self.model_dir = path + "/ltm_data/" + model_study_name + "/"

        if not os.path.exists(self.model_dir):
            os.makedirs(self.model_dir)

        print("\n model_dir \n", self.model_dir)

        self.search_data_path = self.model_dir + "search_data.pkl"
        self.obj_func_path = self.model_dir + "objective_function.pkl"

        self.n_old_samples = 0
        self.n_new_samples = 0

    def remove_model_data(self):
        try:
            shutil.rmtree(self.model_dir)
        except OSError:
            pass

    def _dill_dump(self, object_, path):
        with open(path, "wb") as handle:
            dill.dump(object_, handle)

    def _dill_load(self, path):
        if self._pkl_valid(path):
            with open(path, "rb") as handle:
                object_ = dill.load(handle)

            return object_

    def _pkl_valid(self, pkl_path):
        return os.path.isfile(pkl_path) and os.path.getsize(pkl_path) > 0

    def _get_old_samples_size(self, df):
        if isinstance(df, pd.DataFrame):
            self.n_old_samples = len(df)

    def load_obj_func(self):
        return self._dill_load(self.obj_func_path)

    def load_search_data(self):
        return self._dill_load(self.search_data_path)

    def load(self):
        print("Reading in long term memory ...", end="\r")
        self.results_old = self._dill_load(self.search_data_path)
        self._get_old_samples_size(self.results_old)

        print(
            "Reading long term memory was successful:",
            self.n_old_samples,
            "samples found",
        )

        return self.results_old

    def save(self, dataframe, objective_function):
        self.results_old = self._dill_load(self.search_data_path)

        if self.results_old is not None:
            self.n_old_samples = len(self.results_old)

            dataframe = (
                pd.merge(dataframe, self.results_old, how="outer")
                .drop_duplicates(keep="last")
                .reset_index(drop=True)
            )

        self.n_new_samples = len(dataframe)

        self._dill_dump(objective_function, self.obj_func_path)
        print("Saving long term memory ...", end="\r")

        self._dill_dump(dataframe, self.search_data_path)

        print(
            "Saving long term memory was successful:",
            self.n_new_samples - self.n_old_samples,
            "new samples found",
        )
