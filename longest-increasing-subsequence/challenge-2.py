# Challenge 2 : Écrire un programme qui prend en entrée une liste de nombres et retourne la plus longue
# sous-séquence croissante de cette liste. Par exemple, si la liste d'entrée
# est [3, 1, 4, 1, 5, 9, 2, 6, 5, 1, 2, 3, 5, 8, 9, 7], 
# la plus longue sous-séquence croissante est [1, 2, 3, 5, 8, 9].

def longestIncreasingSubsequence(arr) :
    arrFinal = []
    arrTemp = []
    
    for i in range (len(arr)):
        j=i
        while (j+1 < len(arr)) and (arr[j] < arr[j+1]) :
            arrTemp.append(arr[j])
            j+=1
            
        arrTemp.append(arr[j])
        
        if (len(arrTemp)>len(arrFinal)):
            arrFinal = arrTemp
            arrTemp = []
        else:
            arrTemp = []
    return arrFinal

print(longestIncreasingSubsequence([3, 1, 4, 1, 5, 9, 2, 6, 5, 1, 2, 3, 5, 8, 9, 7]))