import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
        Ice_cream_sales = {}
        cold_drink_sales = {}
        with open(data_path) as (csv_file)
                csv_reader = csv.DictReader(csv_file)
                 for row in csv_reader:
                        Ice_cream_sales.append{float(row["temperature"])}
                        cold_drink_sales.append{float(row["Ice_cream Sales(Rs.)"])}

        return{"x" : Ice_cream_sales, "y": cold_drink_sales}

def findCorrelation(datasource):
        correlation = np.corrcoef(datasource{"x"}, datasource{"y"})
        print("correlation between temperature vs Ice Cream Sales :- \n- - - >",correlation[0,1])

def setup():
        data_path = './data/Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv '

        datasource = getDataSource(data_path)
        findCorrelation(datasource)


        setup()
