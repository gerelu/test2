import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import streamlit as st

fpath=Path(__file__).parent
file=fpath/"data.txt"
# print(file)
data=np.loadtxt(file)

# print(data)
# print(data[:,1])

fig=plt.figure()
ax=fig.subplots()

ax.plot( data[:,0], data[:,1] )

# plt.show()
st.pyplot(fig)
