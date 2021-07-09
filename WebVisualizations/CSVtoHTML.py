import pandas as pd
import os

weather_df = pd.read_csv("WebVisualizations\Resources\cities.csv")

weather_html = weather_df.to_html()

text_file = open("WebVisualizations\weather_data.html", "w")
text_file.write(weather_html)
text_file.close()