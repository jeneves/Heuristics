% Generates surface and contour plots of bump function

numVals = 200;

X = linspace(-1, 11, numVals);
Y = linspace(-1, 11, numVals);

Z = zeros(numVals, numVals);
for i = 1:numVals
    for j = 1:numVals
        Z(i, j) = bump([X(i), Y(j)]);
    end
end

surf(X, Y, Z);
title('Surface graph of bump function');
xlabel('x1');
ylabel('x2');
zlabel('bump([x1, x2]');

figure
contour(X, Y, Z);
title('Surface graph of bump function');
xlabel('x1');
ylabel('x2');
zlabel('bump([x1, x2]');