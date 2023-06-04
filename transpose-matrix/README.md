# English Version
## Transpose a Matrix
### Description
This Python program allows you to transpose a matrix. Transposing a matrix means to swap its rows and columns. For example, the transpose of the following matrix:

```
1 2 3
4 5 6
```

is the following matrix:

```
1 4
2 5
3 6
```

### Usage

To use this program, you need to call the transposeFunction function passing the matrix you want to transpose as an argument. The function will return the transposed matrix.

Here is an example of usage:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transpose = transposeFunction(matrix)

print(transpose)
```

This will produce the following output:

```
[[1, 4], [2, 5], [3, 6]]
```

### How it works

The program starts by determining the number of rows and columns of the matrix using the len functions. Then, it creates a new matrix called transpose which has the number of columns of the original matrix as the number of rows and the number of rows of the original matrix as the number of columns.

Next, the program uses a nested for loop to go through each element of the original matrix and place it in the corresponding position in the transposed matrix.

Finally, the program returns the transposed matrix.

### Contributing

If you would like to contribute to this project, you can create a pull request on GitHub https://github.com/wadeekt
I am always happy to receive contributions from the community!



# Version Française
## Transposer une matrice
### Description
Ce programme Python permet de transposer une matrice. La transposition d'une matrice consiste à échanger ses lignes et ses colonnes. Par exemple, la transposition de la matrice suivante:

```
1 2 3
4 5 6
```

donne la matrice suivante:

```
1 4
2 5
3 6
```

### Utilisation
Pour utiliser ce programme, vous devez appeler la fonction transposeFunction en passant la matrice que vous souhaitez transposer en tant qu'argument. La fonction renverra la matrice transposée.

Voici un exemple d'utilisation:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transpose = transposeFunction(matrix)

print(transpose)
```

Cela produira la sortie suivante:

```
[[1, 4], [2, 5], [3, 6]]
```

### Fonctionnement
Le programme commence par déterminer le nombre de lignes et de colonnes de la matrice en utilisant les fonctions len. Ensuite, il crée une nouvelle matrice appelée transpose qui a le nombre de colonnes de la matrice d'origine comme nombre de lignes et le nombre de lignes de la matrice d'origine comme nombre de colonnes.

Ensuite, le programme utilise une boucle for imbriquée pour parcourir chaque élément de la matrice d'origine et le placer dans la position correspondante dans la matrice transposée.

Enfin, le programme renvoie la matrice transposée.

### Contribuer
Si vous souhaitez contribuer à ce projet, vous pouvez créer une demande de tirage sur GitHub https://github.com/wadeekt . Je suis toujours heureux de recevoir des contributions de la communauté!


by WadeeKT.