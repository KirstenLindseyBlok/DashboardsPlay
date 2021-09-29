#import required libraries
#to help you initialise your application
import dash
#to allow you to create interactive components like graphs, dropdowns, or date ranges
import dash_core_components as dcc
#to let you access HTML tags
import dash_html_components as html
#to help you read and organise the data
import pandas as pd

data = pd.read_csv("avocado.csv")
data = data.query("type == 'conventional' and region == 'Albany'")
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)

app = dash.Dash(__name__)
