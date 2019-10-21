# Remember we are using the R tikzDevice package to produce a LaTeX tikz code representing the R graph - you do not have to use this
#The Escape characters themselves needs also to be escaped. % needs to be escaped in LaTex =\%. This also needs to be escaped for R.
# general usage: tikz(file = 'myPlot.tex', width = 7, height = 7, onefile=TRUE, bg="transparent", fg="black", pointsize=10,... )
# you can include LaTeX code in legends, axes titles eg: plot( 1, 1, main = '\\LaTex\\ is $\\int e^{xy}$' )

library(tikzDevice)
tikz(file = 'MosaicPlot.tex', width = 6, height = 6)
par(mar=c(3, 3.5, 1, 0.4), mgp=c(2,0.2,0))

#Actual R Plot
mosaicplot(table(OrderedDataWithInt), color = TRUE, main="", xlab = "Versions", ylab = "Interaction", legend=TRUE,  cex.axis = 0.66, las = 1, direction = "v")
#End of plot

dev.off()
