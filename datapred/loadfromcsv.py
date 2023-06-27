from __future__ import annotations

from pathlib import Path
import pandas as pd
from typing import Dict

class DataAnalysisBuilder:
    """
    A class to find all csv file inside a path all load each of them into a dataframe 
    """
    @staticmethod
    def open_csv_files(path: Path) -> Dict[str,pd.Dataframe]:
        """
        Open the csv files and load them into a dataframe object for each files

        :param  path : The path where are located the files
                       
        :return: A dictionnary with each key correspond to its dataframe  
        """
        pathlist = path.rglob('*.csv')

        d_files = {e.stem:str(e.absolute()) for e in pathlist if 'csv' in e.suffix}

        d_dataframes = {k:pd.read_csv(v) for k,v in d_files.items()}

        return d_dataframes



    

