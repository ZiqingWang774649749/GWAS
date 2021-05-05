library(ncvreg)
library(Matrix)
library(biglasso)
library(bigmemory)
library(readr)
setwd("d:/AtPolyDB")
X <- setupX(filename = "biglasso_input_with_FT10.raw", sep=' ')
X <- attach.big.matrix("biglasso_input_with_FT10.desc")
y <- X[,1]
X <- X[,-1]
X.bm <- as.big.matrix(X)
str(X.bm)
dim(X.bm)
X.bm[1:10, 1:10]
table(y)
fit <- biglasso(X.bm, y, ncores = 4)
fit <- biglasso(X.bm, y, family = "binomial", ncores = 4)
coefs <- as.matrix(coef(fit, lambda = 0.06))
coefs[coefs != 0, ]
predict(fit, lambda = 0.06, type = "nvars")