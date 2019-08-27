Take a look at the distribution of the scores across the cross-validation folds.

# Scaled Compare Algorithms
`fig = pyplot.figure()
fig.suptitle('Scaled Algorithm Comparison')
ax = fig.add_subplot(111)
pyplot.boxplot(results)
ax.set_xticklabels(names)
pyplot.show()`