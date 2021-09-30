from comandos import Switch, ReceptorLuz, ComandoLigarLuz, ComandoDesligarLuz

if __name__ == "__main__":
    luz = ReceptorLuz()
    ligarLuz = ComandoLigarLuz(luz)
    desligarLuz = ComandoDesligarLuz(luz)

    switch = Switch()
    switch.registrar("ON", ligarLuz)
    switch.registrar("OFF", desligarLuz)

    switch.execute("ON")
    switch.execute("OFF")

    print(switch.historico)
