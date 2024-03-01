import matplotlib.pyplot as plt


# Vẽ biểu đồ hist
# plt.hist(data, bins=2, edgecolor='red')
# plt.title('Biểu đồ Hist')
# plt.xlabel("Giá trị")
# plt.ylabel("Tần suất")

# plt.show()




data = [1,2,3,4,5]
# Nhãn của biểu đồ
labels = ["Nhãn A", "Nhãn B", "Nhãn C", "Nhãn D", "Nhãn E"]
# màu sắc
colors = ["red", "green", "yellow", "blue", "purple"]
# Vẽ biểu đồ
plt.pie(data, labels=labels, colors=colors)
plt.title("Biểu đồ Pie")

plt.show()