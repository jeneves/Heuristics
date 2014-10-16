function t = pairedTTest(X, Y)
% Gets the t value for a paired t test between X and Y

D = X - Y;
meanD = mean(D);
delta = 0;
stdD = std(D);
n = length(X);

t = (meanD - delta) / (stdD / sqrt(n));