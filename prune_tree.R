rm(list=ls()) # clear environment
graphics.off() # clear plots; comment out if you want to keep displayed plots every run

## Install package using install.packages("ape") command
install.packages("ape")
require(ape)

args = commandArgs(trailingOnly=TRUE)
print(args)
if (length(args)<2) {
  stop("At least one argument must be supplied (input file).n", call.=FALSE)
} else if (length(args)==2) {
  # default output file
  args[3] = "out.txt"
}

work.dir <- setwd('.') # change to your work dir
tr.f <- file.path(work.dir, args[0]) # tree file 
tr <- read.tree(file=tr.f) # read tree

## file containing sample IDs to keep. 
#  "to_keep.txt" is new line separated but feel free to format in anyway you want.
#  ?read.delim will show man file for how to read/import the file. 
keep.f <- file.path(work.dir, args[1]) 
to.keep <- read.delim(file=keep.f, header=FALSE, sep='\n', as.is=TRUE)[,1] 

pruned.tr <- drop.tip(tr, setdiff(tr$tip.label, to.keep))

## Plotting output for visual inspection
cat(paste("keeping samples"), to.keep)
par(mfrow=c(1,2), mar=c(1,1,1,1))
# before prune
plot.phylo(ladderize(tr), use.edge.length=TRUE, show.tip.label=TRUE,
           main='original tree')
# after prune
plot.phylo(ladderize(pruned.tr), use.edge.length=TRUE, show.tip.label=TRUE,
           main='pruned tree')