# Remember we are using the R tikzDevice package to produce a LaTeX tikz code representing the R graph - you do not have to use this
#The Escape characters themselves needs also to be escaped. % needs to be escaped in LaTex =\%. This also needs to be escaped for R.
# general usage: tikz(file = 'myPlot.tex', width = 7, height = 7, onefile=TRUE, bg="transparent", fg="black", pointsize=10,... )
# you can include LaTeX code in legends, axes titles eg: plot( 1, 1, main = '\\LaTex\\ is $\\int e^{xy}$' )

library(tikzDevice)
tikz(file = 'barplotGender.tex', width = 2.5, height = 2.5)
par(mar=c(4, 3.5, 1, 1), mgp=c(2,1,0))

#Actual R Plot
legend <- c("Female", "Male", "Other")
colors <- c("red","blue","green") 
slices <- gender
barplot((table(slices)/sum(table(slices))) *100, main = "",xlab = "Percentage (\\%)", horiz=TRUE, names.arg=c("Female", "Male", "Other"), xlim = c(0,70))
#End of plot

dev.off()
