function t = twoSampleTTest(X, Y, stdX, stdY, meanX, meanY)
% Performs the two-sample t test on two distributions

delta = 0;

m = length(X);
n = length(Y);

t = (meanX - meanY - delta) / sqrt(stdX^2/m + stdY^2/n);

end