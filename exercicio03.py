nome_produto: str
preco_produto: float
quantidade_estoque: int

nome_produto = input("digite o nome do produto: ")
preco_produto = float(input("digite o preco do produto:"))
quantidade_estoque = int(input("digite a quantidade em estoque:"))

print("produto:", nome_produto)
print("preco", preco_produto)
print("quantidade em estoque:", quantidade_estoque)