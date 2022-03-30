import plotly.express as px
import pandas as pd

px.set_mapbox_access_token()

df = pd.read_csv("")


fig = px.scatter_mapbox(
    df,
    lat="le_latitude_deg",
    lon="le_longitude_deg",
    hover_data={
        "ident": True,
        "le_ident": True,
        "region_name": True,
        "municipality": True,
    },
    color="le_ident",
    color_continuous_scale="Turbo",
    size_max=50,
    zoom=3.1,
    opacity=0.6,
    center={"lat": 38.0902, "lon": -90.7129},
    mapbox_style="dark",
)

# fig.show()
fig.write_html("map.html")
