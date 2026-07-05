import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import streamlit as st
import tempfile

st.set_page_config(page_title="Electromagnetic Waves", layout="centered")

st.title("⚡ Electromagnetic Wave Simulation")
st.write("Python + Physics Visualization")

z = np.linspace(0, 4*np.pi, 300)
idx = np.linspace(0, len(z)-1, 36).astype(int)

fig = plt.figure(figsize=(8,6), facecolor='black')
ax = fig.add_subplot(111, projection='3d', facecolor='black')

ax.set_axis_off()
ax.view_init(elev=18, azim=-55)
ax.set_xlim(0,4*np.pi)
ax.set_ylim(-1.6,1.6)
ax.set_zlim(-1.6,1.6)

lineE, = ax.plot([],[],[],color='#00e5ff',lw=2.5)
lineB, = ax.plot([],[],[],color='#ff2d78',lw=2.5)

stemsE=[ax.plot([],[],[],color='#00e5ff',lw=.8)[0] for _ in idx]
stemsB=[ax.plot([],[],[],color='#ff2d78',lw=.8)[0] for _ in idx]

def update(frame):
    w=np.sin(z-frame*0.15)

    lineE.set_data(z,w)
    lineE.set_3d_properties(0*z)

    lineB.set_data(z,0*z)
    lineB.set_3d_properties(w)

    for e,b,k in zip(stemsE,stemsB,idx):
        e.set_data([z[k],z[k]],[0,w[k]])
        e.set_3d_properties([0,0])

        b.set_data([z[k],z[k]],[0,0])
        b.set_3d_properties([0,w[k]])

ani=FuncAnimation(fig,update,frames=200,interval=30)

tmp=tempfile.NamedTemporaryFile(suffix=".gif",delete=False)

ani.save(tmp.name,writer="pillow",fps=30)

st.image(tmp.name)