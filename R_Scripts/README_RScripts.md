# R scripts for graphs and stat
All R graphs here will outputted to  LaTeX. Please include in your LateX document, the package tikz 
by  \usepackage{tikz} in the document preamble. You might need to add this also 
```
\usetikzlibrary{positioning,shadows.blur}
```
on the R sides, 2 pakcages do the job of integrating in LaTeX. Package 'tikzDevice' for inserting R plot commands into LaTeX and the 
package 'xtable' for inserting any table produced by R into LateX thus automatically creating Latex tables.

Please you need to know the """"width""" of your Latex colum in case of a 2 colums paper
The TeX Files that would be generated from R Studio are usually in the default workspace of RStudio. You can retrieve the working directory by getwd()

## General Usage
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

## Explanation of par(mar=c(3.5, 3.5, 2, 1))

par() is a parametric function that is very very important.
```
par(mar=c(5.1, 4.1, 4.1, 2.1), mgp=c(3, 1, 0), las=0)
```
The par function sets or adjusts plotting parameters. Here we consider the following three parameters: margin size (mar), axis label locations (mgp), and axis label orientation (las).
* mar – A numeric vector of length 4, which sets the margin sizes in the following order: bottom, left, top, and right. The default is c(5.1, 4.1, 4.1, 2.1).
* mgp – A numeric vector of length 3, which sets the axis label locations relative to the edge of the inner plot window. The first value represents the location the labels (i.e. xlab and ylab in plot), the second is the tick-mark labels, and third is the tick marks. The default is c(3, 1, 0).
* las – A numeric value indicating the orientation of the tick mark labels and any other text added to a plot after its initialization. The options are as follows: always parallel to the axis (the default, 0), always horizontal (1), always perpendicular to the axis (2), and always vertical (3).

To retrieve your defaults for your graphs:
```
par("mar")
[1] 5.1 4.1 4.1 2.1		=> Defaults
> par("mgp")
[1] 3 1 0				=> Defaults
> par("las")
[1] 0					=> Defaults
```
