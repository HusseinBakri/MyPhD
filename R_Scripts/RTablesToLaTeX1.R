# Use the R package xtable  to transform any R data frame or R table into Latex code!!!

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

# to spit it as a file
print(summary(dfWithInt),caption = "Summary Statistics of XYZ in LaTeX yey!"), type="latex", file="Table.tex")


