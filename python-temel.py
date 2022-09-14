Patika.dev Python Temel Modülü Proje

1) Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. 

data = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flat_list=[]
def flatten_list(data):
    # iterating over the data
    for element in data:
        # checking for list
        if type(element) == list:
            # calling the same function with current element as new argument
            flatten_list(element)
        else:
            flat_list.append(element)

# flattening the given list
flatten_list(data)

# printing the flat_list
print(flat_list)


2) Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.

data = [[1, 2], [3, 4], [5, 6, 7]]

a =[]
def rev(k):
  for i in k:
    if type(i) == list:
      a.append(list(reversed(i)))
  return a
  
rev(data)
