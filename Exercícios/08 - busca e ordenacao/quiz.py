# def estranho(A, x, ini, fim):
#     if ini > fim:
#         return -1
#     meio = (ini+fim) //2
#     if A[meio] == x:
#         return meio
#     if x < A[meio]:
#         return estranho(A,x, ini, meio -1)
#     else: return estranho(A, x, meio + 1, fim)
    
# A = [2, 5, 7, 12, 18, 25, 31, 40]
# x = 18
# ini =0
# fim = 7

# res = estranho(A, x, ini, fim)
# print(res)
#######################################################
# def estranho(A, x, l, r, depth = 0):
#     if l > r:
#         return -1
#     if depth % 2 == 0:
#         if A[l] == x:
#             return l
#         if A[r] == x:
#             return r
#     else:
#         if A[r]== x:
#             return r
#         if A[l] == x:
#             return l
        
#     return estranho(A, x, l+1, r-1, depth+1)

# A = [9, 6, 8, 0, 7, 1, 5, 4, 2, 3, 10]

# res = estranho(A, 4, 0, len(A)-1)

# print(res)


#################################################

# from util import bubble_sort

# lista = [11, 5, 7, 3, 2, 1]

# res = bubble_sort(lista)
# print(res)

#######################################################

# def ordena(A):
#     for i in range(1, len(A)):
#         x = A[i]
#         j   = i-1
#         while j >= 0 and A[j] >= x:
#             A[j+1] = A[j]
#             j -= 1
#         A[j+1] = x
#     return A

# res = ordena([56, 34, 12, 7, 89, 90, 5])
# print(res)

###################################################

# # função de busca sequencial
# def estranho(A,x, i=0, passo=1):
#     if i >= len(A):
#         return - 1
    
#     achou = (A[i]== x)
#     r = estranho(A, x, i + passo, passo +1)
#     if r != -1:
#         return r
#     if achou:
#         return i
#     return -1
###############################################
## merge sort

# def estranho(A):
#     n = len(A)
#     size = 1
#     B = A[:]

#     while size < n:
#         for start in range(0, n, 2 * size):
#             mid = min(start + size, n)
#             end = min(start + 2 * size, n)
            
#             i, j = start, mid
#             k = start
            
#             # Merge (Mesclagem)
#             while i < mid and j < end:
#                 if B[i] <= B[j]:
#                     A[k] = B[i]
#                     i += 1
#                 else:
#                     A[k] = B[j]
#                     j += 1
#                 k += 1
            
#             # Copia elementos restantes do primeiro sub-array (se houver)
#             while i < mid:
#                 A[k] = B[i]
#                 i += 1
#                 k += 1

#         # Prepara para a próxima passagem com o dobro do tamanho (size * 2)
#         B = A[:]
#         size *= 2

#     return A

#####################################################

# def estranho(A):
#     if len(A) <= 1:
#         return A
    
#     p = A[0]
#     L = [x for x in A[1:] if x < p]
#     E = [x for x in A if x == p]
#     G = [x for x in A[1:] if x > p]
#     return estranho(G) + E + estranho(L)

