def desconto(preco = 0.0, taxa = 0.0):
    vl_desc = preco * (taxa / 100)
    vl_fin = preco - vl_desc
    print(f"O valor de desconto é {vl_desc} e o valor final é {vl_fin}")

desconto(800,7)