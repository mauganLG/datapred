from __future__ import annotations
from datetime import date
import pandas as pd
from typing import Tuple

class TopFamilyProductSales:
    """
    A class to return the sales and the associate date of the top family product
    """
    def __init__(self,df: pd.DataFrame) -> None:
        self.df = df
      
    @staticmethod
    def builder(df_product: pd.DataFrame,df_sales: pd.DataFrame) -> TopFamilyProductSales:
        """ 
        Builder method that construct an TopFamilyProductSales object from two DataFrame

        :param  df_product : A DataFrame class that contain product datas
                df_sales   : A DataFrame class that contain sales_data datas
        
        :return: TopFamilyProductSales object
        """
        df_p = df_product[['product_id','family_id']].copy()
        df_s = df_sales[['product_id', 'date','sales']].copy()

        df_s['date'] = pd.to_datetime(df_sales['date'])
        df_fuse = df_p.join(df_s.set_index('product_id'), on='product_id')
        
        df_fuse = df_fuse.dropna(subset=['sales'])
        return TopFamilyProductSales(df_fuse)
    def request(self,start: date=None,end: date=None)-> Tuple[int,pd.DataFrame]:
        """
        Perform a request to find the top family product  and return the sales for a defined period date

        :param  start : A datetime.data to indicate the date start time
                        if None the date will be the first date
                end   : A datetime.data to indicate the end start time
                        if None the date will be the last date
        
        :return: A tuple with the top family id product and its Dataframe of the sales for each date
        """
    
        if start:
            self.df = self.df[(self.df['date'].dt.date >= start)]
        if end:
            self.df = self.df[(self.df['date'].dt.date <= end)]          
        
        df_no_date = self.df.drop(columns='date')

        d = df_no_date.groupby(by='family_id').sum()
        d = d.sort_values(by='sales',ascending=False)

        l = d.take([0])

        top_family_product = l.index.tolist()[0]

        df_tfp = self.df.loc[self.df['family_id'] == top_family_product]

        return (top_family_product,df_tfp[['sales','date']].reset_index(drop=True))