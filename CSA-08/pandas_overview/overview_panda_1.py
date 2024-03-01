import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('E:\CODING\mindX\Classes\CSA-08\pandas_overview\provinces.csv')

# Tính mật độ dân số
df['Population_Density'] = df['Population'] * 1000 / df['Area']

# In ra DataFrame với cột mật độ dân số
print(df)

# # Tìm tỉnh thành có mật độ dân số cao nhất
max_density_city = df.loc[df['Population_Density'].idxmax(), 'Name']

# # Tìm tỉnh thành có mật độ dân số thấp nhất
min_density_city = df.loc[df['Population_Density'].idxmin(), 'Name']

# # In ra kết quả
print("Tỉnh thành có mật độ dân số cao nhất:", max_density_city)
print("Tỉnh thành có mật độ dân số thấp nhất:", min_density_city)

# Vẽ biểu đồ bar
# df_sorted = df.sort_values(by='Population_Density', ascending=False)
# top_3 = df_sorted.head(3)
# plt.bar( top_3['Name'], top_3['Population_Density'])

df_top5_density = df.sort_values(by='Population_Density', ascending=False)
top_5 = df_top5_density.head(5)
plt.bar(top_5["Name"], top_5['Population_Density'])
plt.title('Biểu đồ mật độ dân số')
plt.xlabel("Các tỉnh thành")
plt.ylabel("Mật độ dân số")
plt.show()
