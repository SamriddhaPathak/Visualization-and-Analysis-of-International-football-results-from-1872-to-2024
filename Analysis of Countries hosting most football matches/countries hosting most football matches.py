import plotly.express as px
import pandas as pd
from collections import Counter

data = pd.read_csv("Data(file_format_CSV)/results.csv")

data_country =  data['country'] 

count_noof_hostings_by_countries = Counter(data_country)
    
top4_count_noof_hostings_by_countries = count_noof_hostings_by_countries.most_common(10)

countries = [item[0] for item in top4_count_noof_hostings_by_countries]

no_of_hostings = [item[1] for item in top4_count_noof_hostings_by_countries]

dft = {
    'countries': countries,
    'no_of_hostings': no_of_hostings
}

df = pd.DataFrame(dft)
    
fig = px.bar(df, x = 'countries', y = 'no_of_hostings', color = 'countries', title = "Countries Hosting The Most Number of Football Mathces from 1872 to 2024")

fig.show()