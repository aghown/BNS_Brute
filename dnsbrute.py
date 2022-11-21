import dns.resolver

res = dns.resolver.Resolver()
arquivo = open("wordlist.txt", "r")
subdominios = arquivo.read().splitlines()

alvo = input("Alvo: ")
for subdominio in subdominios:
    try:
        sub_alvo = subdominio + "." + alvo
        resultado = res.resolve(sub_alvo, "A")
        for ip in resultado:
            print("Subdmoninios: ", sub_alvo,'\n', "IP: ", "->", ip)
    except:
        pass