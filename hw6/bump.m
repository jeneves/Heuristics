function cost = bump(x)
% Computes the cost of a vector x (will have some length n) using the bump
% function.

% First check two conditions to make sure we need to do the calculation
if min(x) < 0 || max(x) > 10
    cost = 0;
    return;
end

if prod(x) < 0.75
    cost = 0;
    return;
end

% Then do the calculation
numerator1 = sum(cos(x).^ 4);
numerator2 = 2*prod(cos(x).^2);

n = length(x);
denominator = 0;
for i = 1:n
    denominator = denominator + i * x(i)^2;
end
denominator = sqrt(denominator);

cost = abs((numerator1 + numerator2) / denominator);

end

