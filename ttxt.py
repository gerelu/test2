import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# --- 步驟 1: 初始化 Session State (確保變數存在) ---
if "elev" not in st.session_state:
    st.session_state.elev = 20
if "azim" not in st.session_state:
    st.session_state.azim = 40
if "view_selection" not in st.session_state:
    st.session_state.view_selection = None

# 定義一個處理視角切換的函數 (Callback)
def update_view():
    if st.session_state.view_selection == "P-Mx":
        st.session_state.elev, st.session_state.azim = 0, 90
    elif st.session_state.view_selection == "P-My":
        st.session_state.elev, st.session_state.azim = 0, 0
    elif st.session_state.view_selection == "Mx-My":
        st.session_state.elev, st.session_state.azim = 90, 90

# 當 Slider 被滑動時：解除 Pills 的選取
def slider_change():
    # 只要滑桿有動，就強制將 Pills 設定為未選取狀態
    st.session_state.view_selection = None


st.title("PMM Interaction Surface")

col1 = st.columns(1, border=True)[0]
with col1:
    st.write("#### 視角設定")
    elev=st.slider("仰角",0,90, key="elev",on_change=slider_change)
    azim=st.slider("旋轉角",0,360, key="azim",on_change=slider_change)
    view = st.pills(
        "快速選擇視角",
        options=["P-Mx", "P-My", "Mx-My"],
        key="view_selection",
        on_change=update_view
    )

# orth=st.sidebar.checkbox("ortho")

if view is not None:
    # st.write(view)
    if view=="P-Mx":
        elev,azim=0,90
    elif view=="P-My":
        elev,azim=0,0
    elif view=="Mx-My":
        elev,azim=90,90


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
