# from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv('pandas/av-data.csv', skiprows=5)
# print(df.values)

total_rev = 0
total_imps = 0

for val in df.values:
    adv_name, adv_revenue, adv_imps = val[1], val[2], val[3]
    Advertisers(adv_name, adv_revenue, adv_imps)
    print(f'{adv_name} | Revenue: ${adv_revenue:,.2f}, {adv_imps:,}, CPM: {adv_revenue/adv_imps*1000:,.2f}')
    total_rev += adv_revenue
    total_imps += adv_imps

print(f'Total Revenue: ${total_rev:,.2f}\nTotal Impressions: {total_imps:,}\nCPM: {total_rev/total_imps*1000:,.2f}')

# plt.plot(total_imps, total_rev)
# plt.show()