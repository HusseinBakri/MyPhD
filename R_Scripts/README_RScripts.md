#R scripts for graphs and stat#
All R graphs here will outputted to  LaTeX. Please include in your LateX document, the package tikz 
by  \usepackage{tikz} in the document preamble. You might need to add this also 
```
\usetikzlibrary{positioning,shadows.blur}
```
on the R sides, 2 pakcages do the job of integrating in LaTeX. Package 'tikzDevice' for inserting R plot commands into LaTeX and the 
package 'xtable' for inserting any table produced by R into LateX thus automatically creating Latex tables.

Please you need to know the """"width""" of your Latex colum in case of a 2 colums paper
The TeX Files that would be generated from R Studio are usually in the default workspace of RStudio. You can retrieve the working directory by getwd()

##Example General Usage
```
library(tikzDevice)
tikz(file = 'myPlot.tex', width = 7, height = 7, onefile=TRUE, bg="transparent",fg="black", pointsize=10,... )
```

for more info/parameters see the R tikzDevice Reference PDF guide. Width and height are in inches.

***Example:*** width = 2.75/3 is advisable as 7 to 8 cm is normally the width of a colum in a 2 colums paper.
```
tikz(file = 'myPlot.tex', width = 2.75,height = 2.75)
plot( 1, 1, main = '\\LaTex\\ is $\\int e^{xy}$' )
dev.off()
```
Always include dev.off() when you finish

On side of LaTeX, you include your TeX files in the right place that you want
It is advisable to put \include in a \begin{figure} -- \end{figure} block and you should not include the extension .tex

```
\begin{figure}[h!]
\centering
\include{pathtoplot\myPlot}
\caption{}
\end{figure}
```
One problem solved by this is the page break normally created in Latex when not inlucding it in a figure

***For loading Excel files***

Install XLConnect and xlsx packages into R. The following code show you how to load an Excel file you choose
```
library(XLConnect)
library(plotrix)
theData <- readWorksheet(loadWorkbook(file.choose()),sheet=1, header = TRUE)
attach(theData)
```

You can try also the R Commander (GUI interface for R) which in my opinion is not effective
```
library(Rcmdr)
```

We can try R Deducer (another GUI for R) {install.packages(c("JGR","Deducer","DeducerExtras"))}
```
library(JGR)
JGR()
```
