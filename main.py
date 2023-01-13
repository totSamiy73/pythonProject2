money = int(input("Введите сумму вклада: "))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
bank_deposit = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
procent = list(per_cent.values())
TKB = round(procent[0]/100*money)
SKB = round(procent[1]/100*money)
VTB = round(procent[2]/100*money)
SBER = round(procent[3]/100*money)
deposit = [TKB, SKB, VTB, SBER]

print("Доход:", deposit)

max_bank_deposit = max(bank_deposit, key=bank_deposit.get)

print("Максимальная сумма заработка:", str(max(deposit)), "Банк -", str(max_bank_deposit))
