VAT = 23
obliczonyVAT = (1 + VAT / 100)

cenaNettoJava = 10
cenaNettoAjax = 20
cenaNettoJs = 30
cenaNettoHTML = 10

cenaBruttoJava = cenaNettoJava * obliczonyVAT
cenaBruttoAjax = cenaNettoAjax * obliczonyVAT
cenaBruttoJs = cenaNettoJs * obliczonyVAT
cenaBruttoHTML = cenaNettoHTML * obliczonyVAT

print(cenaBruttoAjax)
print(cenaBruttoJava)
print(cenaBruttoHTML)
print(cenaBruttoJs)