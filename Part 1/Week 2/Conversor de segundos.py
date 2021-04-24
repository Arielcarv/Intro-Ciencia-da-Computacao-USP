segundos_total = int(input("Por favor, entre com o número de segundos que deseja converter:"))

dias = segundos_total // (24 * (60 * 60))
horas = (segundos_total // 3600) - (dias * 24)
minutos = (segundos_total//60)-((horas*60)+(dias*1440))
segundos = segundos_total - ((minutos*60)+(horas*3600)+(dias*86400))

print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos.")
