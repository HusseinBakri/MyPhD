# R scripts for graphs and stat
I have wrote several very well received blog articles on my official website on how to marry LaTeX & R. Please view the following articles to learn how. This also helps you understand the R scripts in this repository.
* [Part 1](http://husseinbakri.org/the-marriage-between-r-and-latex-part-1/ "R and LaTeX")
* [Part 2](http://husseinbakri.org/the-marriage-between-r-and-latex-part-2/ "R and LaTeX")
* [Part 3](http://husseinbakri.org/the-marriage-between-r-and-latex-part-3-xtable-package/ "R xtable and LaTeX")
* [Part 4](http://husseinbakri.org/the-marriage-between-r-and-latex-part-4-r-code-inside-latex/ "R and LaTeX")

All R graphs here will outputted to  LaTeX. Please include in your LateX document, the package tikz 
by  \usepackage{tikz} in the LaTeX document preamble. You might need to add this also 

On LaTeX side:
```
\usetikzlibrary{positioning,shadows.blur}
```
on the R sides, 2 pakcages do the job of integrating in LaTeX. Package 'tikzDevice' for inserting R plot commands into LaTeX and the 
package 'xtable' for inserting any table produced by R into LateX thus automatically creating Latex tables.

Please you need to know the """"width""" of your Latex colum in case of a 2 colums paper
The TeX Files that would be generated from R Studio are usually in the default workspace of RStudio. You can retrieve the working directory by getwd()

## To LaTeX - General Usage

### R graphs to LaTeX tikz code
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
Always include dev.off() when you finish. Sometimes I include dev.off() two times to make things work.

Sometimes you need to play with the par() function to fit the plot well (please see the section about par() later in this documentation).

On side of LaTeX, you include your TeX files in the right place that you want
It is advisable to put \include in a \begin{figure} -- \end{figure} block and you should not include the extension .tex

```
\begin{figure}[h!]
\centering
\include{pathtoplot\myPlot}
\caption{}
\end{figure}
```
One problem solved by this is the page break normally created in Latex when not inlucding it in a figure.

### R data frames or R tables into Latex code
```
library(xtable)

# Example 1
dfWithInt <- data.frame(Version, Interaction)
dfTable <- table(dfWithInt)
ftable(dfWithInt) 
xtable(dfTable, caption = "XYZ")

#Summary of this table
xtable(summary(dfTable),caption = "XYZ")

#Write the Latex Table code to a file
print(xtable(dfTable, caption = "XYZ XYZ"), type="latex", file="Table.tex")

###problem with the above is the caption above the table //You have to change and tweak inside Latex ####

# Example 2
summary(dfWithInt)
xtable(summary(dfWithInt),caption = "Summary Statistics of XYZ in LaTeX yey!")

# to spit LaTeX code into a file
print(summary(dfWithInt),caption = "Summary Statistics of XYZ in LaTeX yey!"), type="latex", file="Table.tex")
```

## For loading Excel/CSV files
### XLConnect R package method
Do not forget to install the R XLConnect package. 

#### Reading data from CSV/Excel files
The following code shows you how to load an Excel file via XLConnect R Package
```
library(XLConnect)
library(plotrix)
theData <- readWorksheet(loadWorkbook(file.choose()),sheet=1, header = TRUE)
attach(theData)
```

### sqldf R package method
Do not forget to install the R sqldf package.

#### Reading CSV/Excel (usually filtered by SQL queries)
The following code reads from a CSV containing your data and then storing a selected information (via a SQL query) into a SQLite database - How cool?
```
library(sqldf)

read.csv.sql("myData.csv", sql = c("attach 'data.sqlite' as new", "create table new.MyData as select * from file"))
MyData <- sqldf("select * from dfNoInt where ModelVersionName LIKE '%Achavanich%'")
```
Now you can harness the power of SQL to create any complex queries that suits your need...

#### Writing CSV/Excel
```
library(sqldf)
MyData <- sqldf("select * from dfNoInt where ModelVersionName LIKE '%Achavanich%'")

# Write data as csv in working dir
write.csv(MyData, file = "MyData.csv", row.names=FALSE, na="")  
```

### xlsx R package method
Do not forget to install the R xlsx package by using install.packages("xlsx").

#### Reading CSV/Excel
```
library(xlsx)
myfile <- system.file("data", "myData.xlsx", package = "xlsx")
# Read from 1st worksheet (there is header)
myData <- read.xlsx(myfile, 1, header=TRUE) 
```
#### Writing CSV/Excel
```
##Change working directory and save as xlsx
library(xlsx)
write.xlsx(myRData, "RData.xlsx")
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
