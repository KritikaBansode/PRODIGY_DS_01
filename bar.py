import matplotlib.pyplot as plt


age_groups = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100']
population_counts = [50, 100, 120, 100, 80, 70, 60, 50, 30, 10]


plt.figure(figsize=(10, 6))
plt.bar(age_groups, population_counts, color='skyblue')
plt.xlabel('Age Groups')
plt.ylabel('Number of Individuals')
plt.title('Age Distribution in a Population')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
