from turtle import width
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title('Streamlit　超入門')

st.write('Display Image')

img = Image.open('sample.png')
st.image(img, caption='Sample Image', use_column_width=True)


# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50,50] + [35.69,139.70],
#     columns=['lat','lon']
# )

# 行指定は1
# 列指定は0
# st.dataframe(df.style.highlight_max(axis=0))
# st.write(df)
# 静的な表はtable
# st.table(df)

# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

# st.map(df)

# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import pandas as pd
# import numpy as np
# ```
# """