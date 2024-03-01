import pandas as pd
import matplotlib.pyplot as plt


# Data bài 2
df = pd.read_excel('E:\CODING\mindX\Classes\CSA-08\pandas_overview\coastlines.xls')
# Data bài 1
df1 = pd.read_excel('E:\CODING\mindX\Classes\CSA-08\pandas_overview\provinces.xls')


# Tìm số tỉnh thành giáp biển
print(len(df))

# Thêm dữ liệu đường bờ biển vào data bài 1
df_merge = df1.merge(df, how='left', on='Name')
# Set giá trị 0 cho các tỉnh không giáp biển
df_merge['Coastline'].fillna(0, inplace=True)

print(df_merge)
# Xuất ra file excel
# df_merge.to_excel('data_after_merge.xlsx', index=False)

# Dữ liệu
index_array = df_merge.index.values

# Tạo biểu đồ đường

plt.plot(index_array, df_merge['Coastline'], marker='o', label='Đường bờ biển')
plt.plot(index_array, df_merge['Population'], marker='o', label='Dân số')
plt.plot(index_array, df_merge['Area'], marker='o', label='Diện tích')

# Đặt tiêu đề và nhãn trục
plt.title('Biểu đồ đường')
plt.xlabel('X')
plt.ylabel('Y')

# Hiển thị biểu đồ
plt.show()