
# Binary Tree

Un pequeño motor de arbol binario que proporciona una clase principal Arbol, que sirve como estructura principal para construir el Nodo raiz y realizar los recorridos. Puedes iniciar y testear esta clase con los archivos de la carpeta `/tests` o también puede ejecutar `main.py` para ingresar sus valores propios por teclado

### Instalación desde CMD o Powershell

```bash
git clone https://github.com/Santserrano/binarytree.git
```

### Ejemplo de uso - test

Ejecute algún test con valores previamente definidos:

```python
print('Hola mundo')
```

### Ejemplo de uso - valores por teclado

The notebook `demo.ipynb` provides a full demo of training an 2-layer neural network (MLP) binary classifier. This is achieved by initializing a neural net from `micrograd.nn` module, implementing a simple svm "max-margin" binary classification loss and using SGD for optimization. As shown in the notebook, using a 2-layer neural net with two 16-node hidden layers we achieve the following decision boundary on the moon dataset:

![2d neuron](moon_mlp.png)

### Jupyter Notebook / ipynb

Los archivos de Jupyter Notebook, tales como `trace_graph.ipynb` produce gráficos de visualización para construir los digrafos. Estos archivos presentan la extensión `.ipynb` que, a diferencia de python `.py` ofrece ejecución en bloques de código y renderizado gráfico (ej. tablas, trazos, grafos, gráficas de función, etc).

Puede utilizar la documentación didáctica para entender el funcionamiento del código :)
Incluyen los archivos:
`arbol.ipynb` `grafo.ipynb` `graph.ipynb`

Aquí un ejemplo:

```python
from micrograd import nn
n = nn.Neuron(2)
x = [Value(1.0), Value(-2.0)]
y = n(x)
dot = draw_dot(y)
```
![2d neuron](gout.svg)

### Configurar git 

Clone el repositorio como se menciona en el inicio de la documentación.
Luego, utilizando CMD o Windows Powershell posicionado en la carpeta del proyecto, realice los cambios pertinentes y haga uso de los siguientes comandos para generar el commit y que se vea reflejada la actualización.

En "Descripción breve de los cambios realizados" puede reemplazar con un comentario acerca de los cambios que realizó.

```bash
git add .
git commit -m "Descripción breve de los cambios realizados"
git push origin master
```

También puede utilizar el siguiente comando para verificar el estado de los cambios que aún no han sido guardados.
```bash
git status
```
