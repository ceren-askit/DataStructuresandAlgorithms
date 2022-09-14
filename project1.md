[22,27,16,2,18,6] -> Insertion Sort

1) Yukarı verilen dizinin sort türüne göre aşamalarını yazınız.
[2,27,16,22,18,6] --> [2,6,16,22,18,27] --> [2,6,16,18,22,27]

2) Big-O gösterimini yazınız.
[2,27,16,22,18,6] --> (n)
[2,6,16,22,18,27] --> (n-1)
[2,6,16,18,22,27] --> 1

3) Time Complexity: Average case: Aradığımız sayının ortada olması,Worst case: Aradığımız sayının sonda olması, Best case: Aradığımız sayının dizinin en başında olması.
Worst Case: O(n2)
Average Case: O(n2)
Best Case: O(n)

4) Dizi sıralandıktan sonra 18 sayısı hangi case kapsamına girer? Yazınız.
[2,6,16,18,22,27] --> 18 sayısı ortada yer aldığından average case kapsamına girer. 
