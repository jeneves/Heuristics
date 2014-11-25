function [v,b]=demo
%DEMO    Demonstration function of the GPLAB toolbox.
%   DEMO runs a symbolic regression problem (the quartic
%   polynomial) with 100 individuals for 25 generations,
%   with automatic adaptation of operator probabilities,
%   drawing several plots in runtime, and finishing with
%   two additional post-run plots.
%
%   VARS=DEMO returns all the variables of the algorithm
%   needed to plot charts, continue runs, draw trees, etc.
%
%   [VARS,BEST]=DEMO also returns the best individual found
%   during the run (the same as 'vars.state.bestsofar').
%
%   See also DEMOPARITY,DEMOANT,DEMOPLEXER
%
%   Copyright (C) 2003-2007 Sara Silva (sara@dei.uc.pt)
%   This file is part of the GPLAB Toolbox


fprintf('Running symbolic regression demo...');
p=resetparams;

p=setoperators(p,'crossover',2,2);
p.operatorprobstype='variable';
p.initalfixedprobs=[0.9];
p.reproduction = 0.1;

p = setfunctions(p,'plus',2,'minus',2,'times',2,'mydivide',2);
% Terminals by default just x



p.datafilex='x.txt';
p.datafiley='y.txt';

p.usetestdata=0;

p.calcdiversity={'uniquegen'};
p.calccomplexity=1;
p.graphics={'plotfitness','plotdiversity','plotcomplexity','plotoperators'};
p.depthnodes='2';

M = 1000;
G = 151;
[v,b]=gplab(G,M,p);

desired_obtained(v,[],1,0,[]);
accuracy_complexity(v,[],0,[]);

figure
plotpareto(v);

drawtree(b.tree);