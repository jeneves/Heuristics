function v = getTwoSampleV(X, Y, stdX, stdY)
% Gets the appropriate v value for a two sample t test

m = length(X);
n = length(Y);

v = ((stdX^2/m + stdY^2/n)^2) / ...
    ((stdX^2 / m)^2 / (m-1) + (stdY^2 / n)^2 / (n-1));


end