Arquivo = float(input("Digite o tamanho do arquivo para download (MB): "))
Internet = float(input("Digite a velocidade da Internet (Mbps): "))

Download = (Arquivo * 8) / (Internet * 60)

print(f"Tempo aproximado de download: {Download:.2f} minutos")