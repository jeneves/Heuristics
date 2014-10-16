% Performs the statistical tests outlined in hw7
close all

SA = [91.94 77.13 10.93 18.6 28.63 86.52 64.58 22.23 59.75 134.11];
GA = [147.9 97.88 39.76 204.48 488.83 113.0 141.97 53.76 408.2 226.95];
GS = [47.660 150.53 97.04 82.62 99.89 76.52 87.84 51.73 147.51 115.98];
allHeur = [SA' GA' GS'];
means = [59.44 192.27 95.73];
stdDevs = [39.52 148.35 34.90];
labels = {'SA', 'GA', 'GS'};


% Part i
hold on
boxplot(allHeur, 'labels', labels);
ylabel('Objective Function Value');
title('Box Plots of SA, GA and GS Results');
hold off



% Part ii
figure
hold all

n = 10;
yVals = zeros(1,n);
for i = 1 : n
    yVals(i) = i / (n + 1);
end
% Sorting in the other direction because it's a minimization
for heur = 1:3
    sorted = sort(allHeur(:, heur), 'ascend');
    plot(sorted, yVals, '-x');
end
legend(labels, 'Location', 'SouthEast');
title('Empirical CDF of SA, GA and GS');
xlabel('Objective Function Value');
ylabel('Cumulative Probability');
hold off



% Part iii
%Each pair
t_SA_GA = twoSampleTTest(SA, GA, stdDevs(1), stdDevs(2), means(1), means(2));
t_SA_GS = twoSampleTTest(SA, GS, stdDevs(1), stdDevs(3), means(1), means(3));
t_GA_GS = twoSampleTTest(GA, GS, stdDevs(2), stdDevs(3), means(2), means(3));

tVals = [t_SA_GA, t_SA_GS, t_GA_GS];

v_SA_GA = getTwoSampleV(SA, GA, stdDevs(1), stdDevs(2));
v_SA_GS = getTwoSampleV(SA, GS, stdDevs(1), stdDevs(3));
v_GA_GS = getTwoSampleV(GA, GS, stdDevs(2), stdDevs(3));

vVals = [v_SA_GA, v_SA_GS, v_GA_GS];

pairedLabels = {'SA/GA', 'SA/GS', 'GA/GS'};
alpha = 0.05;

fprintf('iii)\n');

for i = 1 : 3
    pTwoSide = 2 * tcdf(tVals(i), vVals(i));
    pOneSide = pTwoSide / 2;
    
    tTwoSide = tinv(1 - alpha/2, vVals(i));
    tOneSide = tinv(1 - alpha, vVals(i));
    
    fprintf(['%s Statistics: T Statistic: %f\n\n Comparison Values:\n\n' ...
            'T Two Sided, alpha = 0.05/2: %f\nT One Sided, alpha = 0.05: %f\n' ...
            'P Two Sided: %f\nP One Sided: %f\n\n\n'], pairedLabels{i}, ...
            tVals(i), tTwoSide, tOneSide, pTwoSide, pOneSide);
end



% Part iv
% Using the paired t-test
tPaired = pairedTTest(SA, GS);
v = length(SA) - 1;

pTwoSide = 2 * tcdf(tPaired, v);
pOneSide = pTwoSide / 2;

tTwoSide = tinv(1 - alpha/2, v);
tOneSide = tinv(1 - alpha, v);

fprintf(['iv) Paired T Statistics: T Statistic: %f\n\n Comparison Values:\n\n' ...
            'T Two Sided, alpha = 0.05/2: %f\nT One Sided, alpha = 0.05: %f\n' ...
            'P Two Sided: %f\nP One Sided: %f\n\n\n'], ...
            tPaired, tTwoSide, tOneSide, pTwoSide, pOneSide);

        

% Part v
% Rank sum test
[w_SA_GA, z_SA_GA] = rankSumTest(SA, GA);
[w_SA_GS, z_SA_GS] = rankSumTest(SA, GS);
[w_GA_GS, z_GA_GS] = rankSumTest(GA, GS);

wVals = [w_SA_GA, w_SA_GS, w_GA_GS];
zVals = [z_SA_GA, z_SA_GS, z_GA_GS];

pairedLabels = {'SA/GA', 'SA/GS', 'GA/GS'};
alpha = 0.05;

fprintf('v)\n');

for i = 1 : 3
    
    z_alpha = norminv(1-alpha);
    z_alpha_2 = norminv(1 - alpha/2);
    
    p_alpha = 2 * (1 - normcdf(abs(zVals(i))));
    p_alpha_2 = p_alpha/2;
    
    fprintf(['%s Statistics: Z Statistic: %f\n\n Comparison Values:\n\n' ...
            'Z Two Sided, alpha = 0.05/2: %f\nZ One Sided, alpha = 0.05: %f\n' ...
            'P Two Sided: %f\nP One Sided: %f\n\n\n'], pairedLabels{i}, ...
            zVals(i), z_alpha_2, z_alpha, p_alpha_2, p_alpha);
end










