import matplotlib.pyplot as plt

cat_a = [4.4, 3.4, 2.6, 3.8, 4.9, 4.6, 5.2, 4.7, 4.1, 2.6, 6.7, 4.1, 3.6, 2.9,
         2.6, 4.0, 4.3, 3.9, 4.8, 4.5, 4.4, 3.1, 5.7, 4.5]
cat_a.sort()

cat_b = [3.4, 1.1, 2.9, 5.5, 6.4, 5.0, 5.8, 2.5, 3.7, 3.8, 3.1, 1.6, 3.5, 5.9,
         6.7, 5.2, 6.3, 2.6, 4.3, 3.8]
cat_b.sort()


plt.boxplot((cat_a, cat_b), sym='x', whis=1.5, positions=[1, 2], widths=0.8,
            labels=('Catalyst A', 'Catalyst B'))
plt.title('')
plt.ylabel('Percentage Yield')

print(cat_a)
print(cat_b)
plt.show()
