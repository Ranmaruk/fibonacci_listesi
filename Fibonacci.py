###Fibonacci

fibonacci_listesi=[1,1]
eleman=0
krange=int(input("Fibonacci Series Cluster number of elements:"))-2


for i in range(0,krange):
    eleman=fibonacci_listesi[i]+fibonacci_listesi[i+1]
    fibonacci_listesi.append(eleman)
print(fibonacci_listesi)    