from __future__ import annotations
from datetime import date
import pandas as pd

class ThreeTopRetailers:
    """
    A class to find the three top retailers
    """

    def __init__(self,df: pd.DataFrame) -> None:
        self.df = df
    @staticmethod
    def builder(df_stores: pd.DataFrame,df_sales: pd.DataFrame) -> ThreeTopRetailers:
        """ 
        Builder method that construct an ThreeTopRetailers object from two DataFrame

        :param  df_stores : A DataFrame class that contain stores datas
                df_sales  : A DataFrame class that contain sales_data datas
        
        :return: ThreeTopRetailers object
        """
        df_st = df_stores[['store_id','retailer_id']].copy()
        df_sa = df_sales[['store_id', 'date','revenue']].copy()

        df_sa['date'] = pd.to_datetime(df_sa['date'])
        df_fuse = df_st.join(df_sa.set_index('store_id'), on='store_id')
        
        return ThreeTopRetailers(df_fuse)
    
    def request(self,start: date=None,end: date=None) -> list:
        """
        Perform a request to find the top three retailers by an defined lap time or not

        :param  start : A datetime.data to indicate the date start time
                        if None the date will be the first date
                end   : A datetime.data to indicate the end start time
                        if None the date will be the last date
        
        :return: A list of the top three retailers 
        """
        if start:
            self.df = self.df[(self.df['date'].dt.date >= start)]
        if end:
            self.df = self.df[(self.df['date'].dt.date <= end)]    

        df_no_date = self.df.drop(columns='date')
        df_gb_retail = df_no_date.groupby(by='retailer_id').sum()
        df_gb_retail = df_gb_retail.sort_values(by='revenue',ascending=False)

        index_top_three = df_gb_retail.take([0,1,2])

        return index_top_three.index.tolist()