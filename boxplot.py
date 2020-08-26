import matplotlib.pyplot as plt
from quantiles import *

# Compute the median and the first and third quartiles of the sample.
# Indicate these with horizontal lines.
# Draw vertical lines to complete the box.
# Find the largest sample value that is no more than 1.5 IQR above the third quartile,
# and the smallest sample value that is no more than 1.5 IQR below the first quartile.
# Extend vertical lines (whiskers) from the quartile lines to these points.
# Points more than 1.5 IQR above the third quartile, or more than 1.5 IQR below the first quartile,
# are designated as outliers. Plot each outlier individually.


cat_a = [4.4, 3.4, 2.6, 3.8, 4.9, 4.6, 5.2, 4.7, 4.1, 2.6, 6.7, 4.1, 3.6, 2.9,
         2.6, 4.0, 4.3, 3.9, 4.8, 4.5, 4.4, 3.1, 5.7, 4.5]
cat_a.sort()
cat_a_median = quantile_val(cat_a, 2)
cat_a_quartiles = quantile_val(cat_a, 4)
cat_a_first_quart = cat_a_quartiles[0]
cat_a_third_quart = cat_a_quartiles[2]
cat_a_IQR = cat_a_third_quart - cat_a_first_quart


cat_b = [3.4, 1.1, 2.9, 5.5, 6.4, 5.0, 5.8, 2.5, 3.7, 3.8, 3.1, 1.6, 3.5, 5.9,
         6.7, 5.2, 6.3, 2.6, 4.3, 3.8]
cat_b.sort()
cat_b_median = quantile_val(cat_b, 2)
cat_b_quartiles = quantile_val(cat_b, 4)
cat_b_first_quart = cat_b_quartiles[0]
cat_b_third_quart = cat_b_quartiles[2]
cat_b_IQR = cat_b_third_quart - cat_b_first_quart

plt.boxplot((cat_a, cat_b), sym='x', whis=1.5, positions=[1, 2], widths=0.8,
            labels=('Catalyst A', 'Catalyst B'))
plt.title('')
plt.ylabel('Percentage Yield')
plt.show()
