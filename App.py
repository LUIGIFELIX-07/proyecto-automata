import tkinter as tk
import os
from PIL import ImageTk,Image
"""
# Cargar ruta del proyecto
principal_folder = os.path.dirname(__file__)
#Cargarb ruta carpeta de imagenes
images_folder = os.path.join(principal_folder, "imagenes")
# Se crea la ventana
root = tk.Tk()
vp = tk.Frame(root)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))

# se asigna imagen a una variable
rio = ImageTk.PhotoImage(Image.open(os.path.join(images_folder, "ImagenRio.webp")).resize((600,600)))
lobo = ImageTk.PhotoImage(Image.open(os.path.join(images_folder, "lobo.jpg")).resize((600,600)))
#
fondo = tk.Label(vp, image = rio)
#fondo.pack()

button = tk.Button(root, image = lobo)
button.grid(column=1, row=1)

root.mainloop()"""""






def permute(s,n):
    seq=range(s)
    permutations = []
    nodes = list(seq)
    while len(permutations) < s**n:
        node = nodes.pop(0)
        children = list(seq)
        permutation = permutations.pop(0) if len(permutations)>1 else []
        for i in range(len(children)):
            perm = list(permutation)
            perm.append(children[i])
            permutations.append(perm)
            nodes.append(children[i])
    return permutations

def solve(q):
    not_visited = range(len(Q))
    paths = []
    nodes = [Qx(q)]
    while not_visited:
        node = nodes.pop(0)
        children = valid_transitions(Q[node])
        path = paths.pop(0) if len(paths)>0 else []
        for i in range(len(children)):
            child = children[i][1]
            if child in not_visited:
                not_visited.remove(child)
                newpath = list(path)
                e = children[i][0]
                newpath.append(e)
                paths.append(newpath)
                nodes.append(child)
                if (child == Qx(F)):
                    return newpath
    return paths

Q = permute(2,4)
Qx = lambda q: Q.index(q)
F = Q[-1]
E = [ (i, 0, j) for i in [1,0] for j in range(4)]
T = lambda q, i: [ i[0] if i[1] == j or i[2] == j else q[j] for j in range(len(q))]
prohibited = [(1,2),(2,3)]
valid = lambda q: not (sum([q[p[0]]==q[p[1]] and q[0]!=q[p[0]] for p in prohibited]) > 0)
transition = lambda q: [ (e, Qx( T(q,e) )) for e in E if e[0]!=q[0] and e[0]!=q[e[2]]]
valid_transitions = lambda q: [ n for n in transition(q) if valid(Q[n[1]])  ]
solution = solve(Q[0])
q = Q[0]
print(q) 
for e in solution:
    q = T(q,e)
    print(q)