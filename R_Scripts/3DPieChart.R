#The Escape characters themselves needs also to be escaped. % needs to be escaped in LaTex =\%. This also needs to be escaped for R.
# Remember we are using the R tikzDevice package to produce a LaTeX tikz code representing the R graph
tikz(file = '3DPieChart.tex', width = 2.5, height = 2.5)
par(mar=c(4, 3.5, 1, 1), mgp=c(2,1,0))

slices <- gender
legend <- c("Female", "Male", "Other")
colors <- c("red","blue","green")
pie3D(table(slices),col=colors,explode=0.1, cex=0.8)
legend("topright",legend, fill=colors, cex=0.6)

dev.off()
