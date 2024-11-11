import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import plotly.graph_objects as go
from steepestAscent import makeCube, objectiveFunction

# Untuk yang kubus awal (Initiate)
def showInitiateCube(cube):
    x, y, z, text = [], [], [], []
    for i in range(5):
        for j in range(5):
            for k in range(5):
                x.append(i)
                y.append(j)
                z.append(k)
                text.append(str(cube[i][j][k]))
    
    fig = go.Figure(data=[go.Scatter3d(
        x=x,
        y=y,
        z=z,
        mode='text',
        text=text,
        textposition="middle center",
        textfont=dict(size=15, color='red')
    )])

    fig.update_layout(scene=dict(
        xaxis=dict(nticks=5, range=[-1, 5], showticklabels=False, showgrid=False, showline=False, showbackground=False),
        yaxis=dict(nticks=5, range=[-1, 5], showticklabels=False, showgrid=False, showline=False, showbackground=False),
        zaxis=dict(nticks=5, range=[-1, 5], showticklabels=False, showgrid=False, showline=False, showbackground=False),
    ),
    title="Magic Cube Initial State",
    margin=dict(l=0, r=0, b=0, t=30)) 

    fig.show()

# Untuk kubus akhir
def showFinalCube(cube):
    x, y, z, text = [], [], [], []
    for i in range(5):
        for j in range(5):
            for k in range(5):
                x.append(i)
                y.append(j)
                z.append(k)
                text.append(str(cube[i][j][k]))
    
    fig = go.Figure(data=[go.Scatter3d(
        x=x,
        y=y,
        z=z,
        mode='text',
        text=text,
        textposition="middle center",
        textfont=dict(size=15, color='green')
    )])

    fig.update_layout(scene=dict(
        xaxis=dict(nticks=5, range=[-1, 5], showticklabels=False, showgrid=False, showline=False, showbackground=False),
        yaxis=dict(nticks=5, range=[-1, 5], showticklabels=False, showgrid=False, showline=False, showbackground=False),
        zaxis=dict(nticks=5, range=[-1, 5], showticklabels=False, showgrid=False, showline=False, showbackground=False),
    ),
    title="Magic Cube Final State",
    margin=dict(l=0, r=0, b=0, t=30)) 

    fig.show()