### Bir listeyi düzleştiren (flatten) fonksiyon yazımı ###
def flatten(liste):
    output = []
    for i in liste:
        if type(i) is list:
            output.extend(flatten(i))
        else:
            output.append(i)
    return output

### Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazımı ###
def ters(liste):
    for i in liste:
        i.reverse()
    liste.reverse()
    return liste

if __name__ == '__main__':
    liste1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
    result1 = flatten(liste1)
    print(result1)
    liste2 = [[1, 2], [3, 4], [5, 6, 7]]
    result2= ters(liste2)
    print(result2)


