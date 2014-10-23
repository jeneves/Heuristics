% Performs the statistical tests outlined in hw8
close all

SA = [0.580999775369 0.61406917796 0.513959304762 0.576823075147 ...
    0.606251445252 0.572961278261 0.626570370482 0.676633419162 ...
    0.592011658649 0.635321274343 0.607614020084 0.550302988528 ...
    0.519601288684 0.563091176325 0.560594868237 0.575744390307 ...
    0.55577200774 0.642951063542 0.624440936503 0.651069622181];

DDS = [0.741578200251 0.736273820534 0.702723523831 ...
    0.722696382616 0.736480452522 0.713701132392 0.744926573315 ...
    0.68653092157 0.712017571045 0.745911766569 0.773685821187 ...
    0.731640165959 0.750083631257 0.737184173382 0.740265775321 ...
    0.747315749576 0.743579648798 0.712843234704 0.755423977946 ...
    0.721779671141];

GA = [0.778915933699 0.750647633293 0.754253469359 0.766536726605 ...
    0.764022663632 0.779748852044 0.753347159918 0.71506311097 ...
    0.745588797768 0.754451816541 0.751255325534 0.743005388518 ...
    0.7235881248 0.756937155796 0.770611511523 0.746880650405 ...
    0.755596797328 0.747587338455 0.717772317175 0.753978934171];

allHeur = [SA' DDS' GA'];
means = [0.592339 0.732832 0.751489];
stdDevs = [0.042123 0.019712 0.0174096];
labels = {'SA', 'DDS', 'GA'};


% Box Plots:
hold on
boxplot(allHeur, 'labels', labels);
ylabel('Objective Function Value');
title('Box Plots of SA, DDS and GA Results');
hold off



% CDF
figure
hold all

n = 20;
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
title('Empirical CDF of SA, DDS and GA');
xlabel('Objective Function Value');
ylabel('Cumulative Probability');
hold off



% Two Sample T-Test
t_SA_DDS = twoSampleTTest(SA, DDS, stdDevs(1), stdDevs(2), means(1), means(2));
t_SA_GA = twoSampleTTest(SA, GA, stdDevs(1), stdDevs(3), means(1), means(3));
t_DDS_GA = twoSampleTTest(DDS, GA, stdDevs(2), stdDevs(3), means(2), means(3));

tVals = [t_SA_DDS, t_SA_GA, t_DDS_GA];

v_SA_DDS = getTwoSampleV(SA, DDS, stdDevs(1), stdDevs(2));
v_SA_GA = getTwoSampleV(SA, GA, stdDevs(1), stdDevs(3));
v_DDS_GA = getTwoSampleV(DDS, GA, stdDevs(2), stdDevs(3));

vVals = [v_SA_DDS, v_SA_GA, v_DDS_GA];

pairedLabels = {'SA/DDS', 'SA/GA', 'DDS/GA'};
alpha = 0.05;

for i = 1 : 3
    pTwoSide = 2 * tcdf(-abs(tVals(i)), vVals(i));
    pOneSide = pTwoSide / 2;
    
    tTwoSide = tinv(1 - alpha/2, vVals(i));
    tOneSide = tinv(1 - alpha, vVals(i));
    
    fprintf(['%s Statistics: T Statistic: %f\n\n Comparison Values:\n\n' ...
            'T Two Sided, alpha = 0.05/2: %f\nT One Sided, alpha = 0.05: %f\n' ...
            'P Two Sided: %f\nP One Sided: %f\n\n\n'], pairedLabels{i}, ...
            tVals(i), tTwoSide, tOneSide, pTwoSide, pOneSide);
end

