# Code that plot an Empirical Cumulative Distribution Function 
# Remember we are using the R tikzDevice package to produce a LaTeX tikz code representing the R graph - you do not have to use this
#The Escape characters themselves needs also to be escaped. % needs to be escaped in LaTex =\%. This also needs to be escaped for R.
# general usage: tikz(file = 'myPlot.tex', width = 7, height = 7, onefile=TRUE, bg="transparent", fg="black", pointsize=10,... )
# you can include LaTeX code in legends, axes titles eg: plot( 1, 1, main = '\\LaTex\\ is $\\int e^{xy}$' )

library(tikzDevice)
tikz(file = 'CDFPlot.tex', width = 6, height = 6)

#Actual R Plot
plot(ecdf(Rating), xlab = "Rating", ylab = "CDF of Rating")
#End of plot

dev.off()

