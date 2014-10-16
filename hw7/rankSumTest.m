function [w, Z] = rankSumTest(X, Y)

m = length(X);
n = length(Y);

delta = 0;
X = X - delta;

[~, indices] = sort([X Y]);

w = 0;
for i = 1 : m + n
    if indices(i) <= m
        w = w + i;
    end
end

Z = (w - m*(m + n + 1)/2) / sqrt(m*n*(m + n + 1)/12);

end