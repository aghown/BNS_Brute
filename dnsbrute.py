import dns.resolver

res = dns.resolver.Resolver()
alvo = "bancocn.com"

try:
    resultado = res.resolve(alvo, "A")
    for info in resultado:
        print(alvo, "->", info)
except:
    pass