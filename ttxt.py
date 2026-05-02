import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import streamlit as st

# fpath=Path(__file__).parent
# file=fpath/"data.txt"
file="data.txt"
# print(file)
data=np.loadtxt(file)

# print(data)
# print(data[:,1])

fig=plt.figure()
ax=fig.subplots()

ax.plot( data[:,0], data[:,1] )

# plt.show()
st.pyplot(fig)

file2="phipmm.txt"
data=np.loadtxt(file2)
st.write(data)

# st.sidebar.header("view setting")
# elev=st.sidebar.slider("elev",0,90,30)
# azim=st.sidebar.slider("azim",0,360,40)
# # orth=st.sidebar.checkbox("ortho")

# st.title("PMM Interaction Surface")


# fig=plt.figure(figsize=(9,9))
# ax=fig.add_subplot(projection="3d")



# file="phipmm.txt"
# nang=97
# nc=100

# # 取得目前py所在的絕對路徑
# base_path = Path(__file__).parent
# file_path = base_path / file
# st.write(file_path)

# data=np.loadtxt(file_path)


# x=data[:,0].reshape(nang, nc)
# y=data[:,1].reshape(nang, nc)
# z=data[:,2].reshape(nang, nc)
# ax.plot_surface(x,y,z,alpha=0.2,edgecolor="gray",lw=0.3,cmap="Blues")

# ax.set_xlabel(r'$\phi \cdot M_{nx}$ (tf-m)')
# ax.set_ylabel(r'$\phi\cdot M_{ny}$ (tf-m)')
# ax.set_zlabel(r'$\phi\cdot P_n$ (tf)')
# ax.set_title('P-Mx-My Interaction Surface')
# ax.tick_params(labelsize=8)
# # ax.view_init(elev=0,azim=270)

# # ax.axis("equal") #xy等比例。ps:xy範圍相同即等比例。
# rng=np.ptp([x,y]) #設定範圍
# rng=rng*1.05/2
# ax.set_xlim(-rng,rng) #xy軸均相同範圍
# ax.set_ylim(-rng,rng)
# ax.set_proj_type('ortho') #正交投影顯示

# ax.view_init(elev,azim)


# st.pyplot(fig)
