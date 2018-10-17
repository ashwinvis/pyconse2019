import matplotlib.pyplot as plt
import networkx as nx
from networkx.readwrite.adjlist import read_adjlist

colors = {
    'royalblue': ('Python', 'Cython', 'Pythran', 'Numba', 'numpy.f2py', 'PyPy',
             'pyjulia', 'mpi4py', 'multiprocessing', 'threading', 'asyncio',
             'numba', 'dask', 'trio',),
    'pink': ('C', 'SWIG', 'C++', 'Boost.Python', 'xproject', 'xsimd',
             'xtensor', 'xtensor-python',),
    'goldenrod': ('Rust', 'rust-numpy',),
    'grey': ('Fortran',),
    'forestgreen': ('Julia', 'PyCall.jl',),
    'slategrey': ('CUDA', 'OpenMP', 'MPI', 'SIMD',),
}

G = read_adjlist("graph.txt")
node_color = []
for node in G.nodes():
    color = [k for k, v in colors.items() if node in v]
    node_color.append(color[0])

nx.draw(G, with_labels=True, node_shape='s', node_color=node_color)
plt.show()
