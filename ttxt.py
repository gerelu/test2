import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


st.title("PMM Interaction Surface")

col1 = st.columns(1, border=True)[0]
with col1:
    st.write("#### 視角設定")
    elev=st.slider("仰角",0,90,20)
    azim=st.slider("旋轉角",0,360,40)
# orth=st.sidebar.checkbox("ortho")



fig=plt.figure(figsize=(9,9))
ax=fig.add_subplot(projection="3d")


file="phiPMM.npy"
nang=97
nc=100


data=np.load(file)


x=data[:,0].reshape(nang, nc)
y=data[:,1].reshape(nang, nc)
z=data[:,2].reshape(nang, nc)
ax.plot_surface(x,y,z,alpha=0.2,edgecolor="gray",lw=0.3,cmap="Blues")

ax.set_xlabel(r'$\phi \cdot M_{nx}$ (tf-m)')
ax.set_ylabel(r'$\phi\cdot M_{ny}$ (tf-m)')
ax.set_zlabel(r'$\phi\cdot P_n$ (tf)')
ax.set_title('P-Mx-My Surface & loads ')
ax.tick_params(labelsize=8)
# ax.view_init(elev=0,azim=270)

# ax.axis("equal") #xy等比例。ps:xy範圍相同即等比例。
rng=np.ptp([x,y]) #設定範圍
rng=rng*1.05/2
ax.set_xlim(-rng,rng) #xy軸均相同範圍
ax.set_ylim(-rng,rng)
ax.set_proj_type('ortho') #正交投影顯示

ax.view_init(elev,azim)


st.pyplot(fig)
