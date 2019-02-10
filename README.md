# phynance
Open source Data Science libraries in python

This repository contains a collection python code that helps investors to use data science when taking financial decisions.
It is written for our own research and open source with absolutely no warranty or support.

## Portfolio Optimizer
The code is dependent on PyPortfolioOpt, please check the following page for installation instructions.

https://github.com/robertmartin8/PyPortfolioOpt

In our Portfolio Optimizer, you can input a list of stocks and the code will calculate what is the allocation that maximize the Sharpe ratio of the portfolio.

To run it in Google Colab:
https://colab.research.google.com/github/cartasuzuki/phynance/blob/master/PortfolioOptimizer.ipynb


In the Nikkei jupyter notebook we do an analysis of the Nikkei 50 High Yield index and analyze if it is possible to create a portfolio with similar returns and Sharpe ratio by holding a smaller number of stocks (an avoid paying management fees)

To run it in Google Colab

https://colab.research.google.com/github/cartasuzuki/phynance/blob/master/NikkeiHighDiv50_analysis.ipynb

The result is a Portfolio where however one particular sector (Trading Companies) are over represented. In order to improve sector differentiation we therefore want to drop some stocks and redo the calculation.

https://colab.research.google.com/github/cartasuzuki/phynance/blob/master/NikkeiHighDiv50_analysis_drop_some.ipynb

Another type of assets that helps creating a recurring income is REIT. In the following study we try to selcect a REIT portfolio which maximize Sharpe ration.

https://colab.research.google.com/github/cartasuzuki/phynance/blob/master/JREIT_analysis.ipynb
