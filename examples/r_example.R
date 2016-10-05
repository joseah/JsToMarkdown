#' ---
#' title: Get and plot a random distribution
#' author: José Alquicira Hernández
#' ---
#'
#' # Get distribution
#'
#' Create a vector from **1** to **100**
#'


d <- seq(1,100)  

#' Sample 400 values with replacement

d.sample <- sample(d, size = 400, replace = TRUE)


#' # Plot data
#' Plot data and save graph

library(Cairo)
CairoPNG(filename = "sample_dist.png", width = 600, height = 600)
hist(d.sample, breaks = 50, col = "steelblue", 
          main = "Sample distribution", xlab = "Values")
dev.off()

#' ![](sample_dist.png)