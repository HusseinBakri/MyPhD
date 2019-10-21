# Remember we are using the R tikzDevice package to produce a LaTeX tikz code representing the R graph - you do not have to use this
#The Escape characters themselves needs also to be escaped. % needs to be escaped in LaTex =\%. This also needs to be escaped for R.
# general usage: tikz(file = 'myPlot.tex', width = 7, height = 7, onefile=TRUE, bg="transparent", fg="black", pointsize=10,... )
# you can include LaTeX code in legends, axes titles eg: plot( 1, 1, main = '\\LaTex\\ is $\\int e^{xy}$' )

library(tikzDevice)
tikz(file = 'AssociationPlot.tex', width = 6, height = 6)

#Actual R Plot
assoc(structable(OrderedDataWithInt), color = TRUE, main="Association Plot", xlab = "Versions", ylab = "Interaction", legend=TRUE, cex.axis = 0.66, las = 1, shade=TRUE, direction = "v")
#End of plot

dev.off()
