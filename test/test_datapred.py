from datetime import date

import pandas as pd
import datapred.threetopretailers as ttr
import datapred.topfamilyproductsales as tfp


def test_three_top_retailers():


    data_store = {
        "store_id":[0,1,2,3,4,5,6,7,8,9],
        "store_name":["store_0","store_1","store_2","store_3","store_4","store_5","store_6","store_7","store_8","store_9"],
        "retailer_id":[2,1,2,0,2,3,1,3,1,0]
    }
   
    data_sales = {
        "product_id":[0,0,0,0,0,0,0,0,0,0],
        "store_id":  [0,1,2,3,4,5,6,7,8,9],
        "date":["2016-01-01","2016-01-02","2016-01-03","2016-01-04","2016-01-05","2016-01-06","2016-01-07","2016-01-08","2016-01-09","2016-01-10"],
        "sales": [1,5,9,12,3,4,30,11,81,53],
        "revenue": [100,200,300,400,500,600,700,800,900,1000]
    }

    df_store = pd.DataFrame(data_store)
    df_sales= pd.DataFrame(data_sales)

    three_top = ttr.ThreeTopRetailers.builder(df_store,df_sales)

    l_three_top = three_top.request()
    
    assert  [1,0,3] == l_three_top

def test_top_family_product_sales():

    data_product = {
        "product_id": [0,1,2,3,4,5,6,7,8,9],
        "product_name": ["product_0","product_1","product_2","product_3","product_4","product_5","product_6","product_7","product_8","product_9"],
        "family_id" : [6,8,0,2,7,5,0,4,8,5],
        "price" : [100,200,300,400,500,600,700,800,900,1000]
    }
  
    data_sales = {
        "product_id":[8,3,0,2,7,5,4,5,5,1],
        "store_id":  [0,1,2,3,4,5,6,7,8,9],
        "date":["2016-01-01","2016-01-02","2016-01-03","2016-01-04","2016-01-05","2016-01-06","2016-01-07","2016-01-08","2016-01-09","2016-01-10"],
        "sales": [1,5,9,12,3,4,30,11,81,53],
        "revenue": [100,200,300,400,500,600,700,800,900,1000]
    }
    df_product = pd.DataFrame(data_product)
    df_sales= pd.DataFrame(data_sales)

    top_family = tfp.TopFamilyProductSales.builder(df_product,df_sales)
    top = top_family.request()

    data_test = {
        "sales": [4.0,11.0,81.0],
        "date": ["2016-01-06","2016-01-08","2016-01-09"]
    }

    df_test = pd.DataFrame(data_test)
    df_test['date'] = pd.to_datetime(df_test['date'])
    

    assert 5 == top[0]
    assert df_test.equals(top[1]) == True
