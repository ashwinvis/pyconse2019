import matplotlib.pyplot as plt
import networkx as nx
from networkx.readwrite.adjlist import read_adjlist

colors = {
    "skyblue": (
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
        "arrayfire-python",
        "pyccel",
        "cffi",
        "numexpr",
        "RPython",
        "pybind11",
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
        "ROCm",
    ),
    "goldenrod": ("Rust", "rust-numpy", "PyO3", "Weld"),
    "purple": ("Fortran",),
    "forestgreen": ("Julia", "PyCall.jl"),
    "slategrey": ("CUDA", "OpenCL", "OpenMP", "OpenACC", "MPI", "SIMD", "LLVM",),
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
#  type_plot = "nxviz"

plt.figure(figsize=(10,7), dpi=150)
if type_plot == "classic":
    # Classic graphviz plot
    nx.draw(
        G,
        with_labels=True,
        node_shape="o",
        node_color=node_color,
        node_size=800,
        font_size=8
    )
elif type_plot == "nxviz":
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

try:
    import pygraphviz
    from networkx.drawing.nx_agraph import write_dot
    print("using package pygraphviz")
except ImportError:
    try:
        import pydot
        from networkx.drawing.nx_pydot import write_dot
        print("using package pydot")
    except ImportError:
        print()
        print("Both pygraphviz and pydot were not found ")
        print("see  https://networkx.github.io/documentation/latest/reference/drawing.html")
        print()
        raise

write_dot(G, "graph.dot")
