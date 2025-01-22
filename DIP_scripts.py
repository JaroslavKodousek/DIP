def dip_calculation(
                    input_monthly: int,
                    interest_yearly_percent: float,
                    buying_fee: float,
                    earnings_yearly_percent: float,
                    buying_frequency_yearly: int = 12,
                    years_investing: int = 36,
                    ):
    yearly_earnings = input_monthly * 12
    buying_fee_yearly = buying_fee * buying_frequency_yearly
    interest_yearly_percent = (100 + interest_yearly_percent) / 100
    earnings_yearly_percent = (100 + earnings_yearly_percent) / 100
    earnings_yearly = yearly_earnings - buying_fee_yearly

    sum = 0

    for year in range (1, years_investing+1):
        sum += earnings_yearly
        sum /= interest_yearly_percent
        sum *= earnings_yearly_percent
        #print(f"Your earnings in year {year} are {sum:,.0f} Kč")
    # print("=====================================")


    return sum




# Portu:
portu_sum = dip_calculation(4000, 0.5, 0, 6, 12, 34)
print(f"Portu celkem je {portu_sum:,.0f} Kč")
# print("=====================================")
# print("=====================================")
# print("=====================================")
patria_sum = dip_calculation(4000, 0.12, 150, 6, 12, 34)
print(f"Patria celkem je {patria_sum:,.0f} Kč")
print("=====================================")

print(f"Výdělky Portu minus Patria se rovnají {portu_sum - patria_sum:,.0f} Kč")
if portu_sum > patria_sum:
    print("PORTU JE LEPŠÍ VOLBA")
else:
    print("PATRIA JE LEPŠÍ VOLBA")