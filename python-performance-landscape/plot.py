import matplotlib.pyplot as plt
import networkx as nx
from networkx.readwrite.adjlist import read_adjlist

colors = {
    "royalblue": (
        "Python",
        "Cython",
        "Pythran",
        "Numba",
        "Cupy",
        "Cocos",
        "hpat",
        "numpy.f2py",
        "f90wrap",
        "PyPy",
        "pyjulia",
        "mpi4py",
        "multiprocessing",
        "threading",
        "asyncio",
        "numba",
        "dask",
        "trio",
        "transonic",
    ),
    "pink": (
        "C",
        "SWIG",
        "C++",
        "Boost.Python",
        "xproject",
        "xsimd",
        "xtensor",
        "xtensor-python",
        "Bohrium",
        "ArrayFire",
    ),
    "goldenrod": ("Rust", "rust-numpy"),
    "grey": ("Fortran",),
    "forestgreen": ("Julia", "PyCall.jl"),
    "slategrey": ("CUDA", "OpenCL", "OpenMP", "MPI", "SIMD"),
}

G = read_adjlist("graph.txt")
node_color = []
for node in G.nodes():
    color = [k for k, v in colors.items() if node in v]
    if not color:
        raise ValueError(f"Color undefined for {node}")
    node_color.append(color[0])
    G.node[node]["value"] = color[0]

type_plot = "classic"
#  type_plot = "circos"

plt.figure(figsize=(8,5), dpi=150)
if type_plot == "classic":
    # Classic graphviz plot
    nx.draw(
        G,
        with_labels=True,
        node_shape="o",
        node_color=node_color,
        node_size=600,
        font_size=8
    )
elif type_plot == "circos":
    from nxviz.plots import CircosPlot as Plot

    c = Plot(
        G,
        node_color="value",
        node_order="value",
        node_labels=True,
        # , node_color=node_color
    )
    c.draw()
plt.tight_layout()
plt.savefig("graph.png")
plt.show()
