# yieldcurve-apm466a1-repo
MAT1856/APM466: Mathematical Finance Assignment #1 on yield curves. Scraping bond price data to calculate yield curve, spot curve, forward curve, and other things

MAT1856/APM466: Mathematical Finance Winter 2023
Assignment #1: Yield Curves
Professor: Luis Seco
Note: Please bring any questions about this assignment to your TA’s weekly office hour.
1.1 Introduction
Due: Monday, February 6th, 2023 at 11AM ET to be submitted online via Crowdmark.
For each weekday from Jan 16th, 2023, to January 30, 2022 (inclusive, 2 weeks worth, 10 days), collect all
historical close prices for all Canadian Government Bonds which have a maturity less than 10 years from
January 16, 2023 on the “Frankfurt” Exchange; I.e., all bonds listed via the following two links:
1. https://markets.businessinsider.com/bonds/finder?borrower=71&maturity=shortterm&yield=
&bondtype=2%2c3%2c4%2c16&coupon=&currency=184&rating=&country=19
2. https://markets.businessinsider.com/bonds/finder?borrower=71&maturity=midterm&yield=
&bondtype=2%2c3%2c4%2c16&coupon=&currency=184&rating=&country=19
The data surrounding the bonds found on the above two links will be used for calculating the yield curve
(ytm curve), spot curve, and forward curve. Please familiarize yourself with these definitions, as
per the links, as those will be the definitions used for this assignment.
For each bond, you will also need to collect the following information: coupon, ISIN, issue date, maturity
date. All this data is available on the “Snapshot” page before clicking through to the “Historical” page.
This assignment is split into 2 parts, the first asks questions about some fundamentals of fixed income and
mathematical finance. The second will be an empirical exercise in generating yield curves, and in particular
the 1, 2, 3, 4 and 5 year rates, and analyzing these rates through PCA.
1.2 Expectations
1. You may use R, Python, or any programming language (no Excel without approval from TA beforehand)
of your choice to answer the “empirical questions”.
2. Please have your final report typeset using LATEXand the following template: template. The website:
www.overleaf.com is particularly useful.
3. Important/New: Your report must be no longer than 3 pages long in total (excluding references).
4. Each of the “fundamental questions” must be answered in clear and coherent full sentences.
5. At the end of your report you must cite all references and include a link to a GitHub repository with
all your code used for the project.
6. You may, and are encouraged, to discuss how to do these questions with your peers. However, your
write-up must be done individually, and the sharing of your write-up or code before the deadline is
prohibited.
7. A 5% penalty per day past the deadline up until 1 week (35%) will apply for late submissions.
Additional Notes: Marks will be awarded for each question as either full-, half-, or zero-marks according to if
the question was answered with a few small mistakes, substantial mistakes but fundamental idea still correct, or
fundamental idea wrong / no answer respectively. -10 marks (each) if expectations 2, 3, or 4 not adhered to.
1
Assignment 1: Yield Curves, Luis Seco 2
2 Questions
2.1 Fundamental Questions - 25 points
1. (5 points total) (One sentence each.)
(a) (1 point) Why do governments issue bonds and not simply print more money?
(b) (2 points) Give a hypothetical example of why the long-term part of a yield curve might flatten.
(c) (2 points) Explain what quantitative easing is and how the (US) Fed has employed this since
the beginning of the COVID-19 pandemic.
2. (10 points) We asked you to pull data for all bonds, but if you’d like to construct a yield a “0-5 year”
yield & spot curves, as the government of Canada issues all of its bonds with a semi-annual coupon,
when bootstrapping you’ll only need 10 or 11 bonds to perform this task. Ideally, the bonds in any
yield curve should be consistent in some way with one another so that yields are easier to compare.
Select (list) 10 bonds that you will use to construct the aforementioned curves with an explanation
of why you selected those 10 bonds based on the characteristics we asked you to collect for each bond
(coupon, issue date, maturity date, etc.).
􀀀
Note: 1) There is a unique ideal answer, 2) To easily refer to a bond, please use the following
convention: “CAN 2.5 Jun 24” refers to the Canadian Government bond with a maturity in June 24
and a coupon of 2.5
 
.
3. (10 points) In a few plain English sentences, in general, if we have several stochastic processes for
which each process represents a unique point along a stochastic curve (assume points/processes are
evenly distributed along the curve), what do the eigenvalues and eigenvectors associated with the
covariance matrix of those stochastic processes tell us?
(Hint: This is called Principal Component Analysis)
2.2 Empirical Questions - 75 points
4. (40 points total)
(a) (10 points) First, calculate each of your 10 selected bonds’ yield (ytm). Then provide a welllabeled
plot with a 5-year yield curve (ytm curve) corresponding to each day of data superimposed
on-top of each other. You may use any interpolation technique you deem appropriate
provided you include a reasonable explanation for the technique used.
(b) (15 points) Write a pseudo-code (explanation of an algorithm) for how you would derive the
spot curve with terms ranging from 1-5 years from your chosen bonds in part 2. (Please recall
the day convention simplifications provided in part 2 as well.) Then provide a well-labeled plot
with a 5-year spot curve corresponding to each day of data superimposed on-top of each other.
(c) (15 points) Write a pseudo-code for how you would derive the 1-year forward curve with terms
ranging from 2-5 years from your chosen bonds in part 2 (I.e., a curve with the first point being
the 1yr-1yr forward rate and the last point being the 1yr-4yr rate). Then provide a well-labeled
plot with a forward curve corresponding to each day of data superimposed on-top of each other.
5. (20 points) Calculate two covariance matrices for the time series of daily log-returns of yield, and
forward rates (no spot rates). In other words, first calculate the covariance matrix of the random
variables Xi, for i = 1, . . . , 5, where each random variable Xi has a time series Xi,j given by:
Xi,j = log(ri,j+1/ri,j), j = 1, . . . , 9
then do the same for the following forward rates - the 1yr-1yr, 1yr-2yr, 1yr-3yr, 1yr-4yr.
6. (15 points) Calculate the eigenvalues and eigenvectors of both covariance matrices, and in one sentence,
explain what the first (in terms of size) eigenvalue and its associated eigenvector imply.
