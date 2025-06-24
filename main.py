import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    '장소': ['경복궁', '남산타워'],
    '위도': [37.5702, 37.5512],
    '경도': [126.992, 126.9882]
})

fig = px.scatter_mapbox(df, lat='위도', lon='경도', text='장소',
                        zoom=10, height=500)
fig.update_layout(mapbox_style="open-street-map")  # 무료 스타일
fig.show()
