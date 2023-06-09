import statistics

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

prumer = [statistics.mean(teplota) for teplota in teploty]
ranni = [teplota[0] for teplota in teploty]
nocni = [teplota[3] for teplota in teploty]
poledni_nocni = [[teplota[1], teplota[3]] for teplota in teploty]

print(prumer)
print(ranni)
print(nocni)
print(poledni_nocni)
