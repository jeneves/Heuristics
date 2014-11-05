% Performs the statistical tests outlined in hw8
close all

SA = [107.0 109.0 103.0 104.0 111.0 110.0 109.0 109.0 105.0 108.0 109.0 ...
      107.0 111.0 112.0 112.0 108.0 107.0 108.0 108.0 116.0 112.0 114.0 ...
      105.0 112.0 105.0 108.0 105.0 110.0 113.0 113.0 ];

RS = [167.0 163.0 167.0 162.0 163.0 164.0 164.0 162.0 163.0 163.0 164.0 ...
      165.0 164.0 161.0 165.0 163.0 160.0 165.0 165.0 163.0 165.0 165.0 ...
      163.0 162.0 164.0 162.0 163.0 165.0 163.0 163.0 ];

GA = [162. 164. 165. 160. 163. 162. 162. 163. 165. 165. 164. 163. 161. ...
      167. 165. 165. 169. 161. 164. 162. 161. 167. 162. 164. 161. 164. ...
      165. 164. 164. 164. ];
  
DDS = [167.0 165.0 161.0 163.0 164.0 160.0 166.0 167.0 164.0 164.0 160.0 ...
       165.0 166.0 163.0 167.0 155.0 161.0 162.0 161.0 162.0 163.0 163.0 ...
       165.0 165.0 165.0 165.0 160.0 164.0 164.0 164.0 ];
  
TS = ones(1, length(DDS));

allHeur = [SA' RS' GA' DDS' TS'];
means = [mean(SA) mean(RS) mean(GA) mean(DDS) mean(TS)]
stdDevs = [std(SA) std(RS) std(GA) std(DDS) std(TS)]
labels = {'SA' 'RS' 'GA' 'DDS' 'TS'};


% Box Plots:
hold on
boxplot(allHeur, 'labels', labels);
ylabel('Objective Function Value');
title('Box Plots of SA, RS, GA, DDS and TS Results');
hold off



% CDF
figure
hold all

n = 30;
yVals = zeros(1,n);
for i = 1 : n
    yVals(i) = i / (n + 1);
end
% Sorting in the other direction because it's a minimization
for heur = 1:5
    sorted = sort(allHeur(:, heur), 'ascend');
    plot(sorted, yVals, '-x');
end
legend(labels, 'Location', 'SouthEast');
title('Empirical CDF of SA, RS, GA, DDS and TS');
xlabel('Objective Function Value');
ylabel('Cumulative Probability');
hold off



% Two Sample T-Test

pairs = [1,2;1,3;1,4;1,5;2,3;2,4;2,5;3,4;3,5;4,5];
labels = {'SA', 'RS', 'GA', 'DDS', 'TS'};

alpha = 0.05;

for i = 1 : 10
    curPair = pairs(i, :);
    t = twoSampleTTest(allHeur(:, curPair(1))', allHeur(:, curPair(2))',...
        stdDevs(curPair(1)), stdDevs(curPair(2)), means(curPair(1)), ...
        means(curPair(2)));
    v = getTwoSampleV(allHeur(:, curPair(1))', allHeur(:, curPair(2))',...
        stdDevs(curPair(1)), stdDevs(curPair(2)));
    
    pTwoSide = 2 * tcdf(-abs(t), v);
    pOneSide = pTwoSide / 2;
    
    tTwoSide = tinv(1 - alpha/2, v);
    tOneSide = tinv(1 - alpha, v);
    
    label = [ labels{curPair(1)} '/' labels{curPair(2)} ];
    
    fprintf(['%s Statistics: T Statistic: %f\n\n Comparison Values:\n\n' ...
            'T Two Sided, alpha = 0.05/2: %f\nT One Sided, alpha = 0.05: %f\n' ...
            'P Two Sided: %f\nP One Sided: %f\n\n\n'], label, ...
            t, tTwoSide, tOneSide, pTwoSide, pOneSide);
end

