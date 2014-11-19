function f = evaluate_objective(x, M, V)

%% function f = evaluate_objective(x, M, V)
% Function to evaluate the objective functions for the given input vector
% x. x is an array of decision variables and f(1), f(2), etc are the
% objective functions. The algorithm always minimizes the objective
% function hence if you would like to maximize the function then multiply
% the function by negative one. M is the number of objective functions and
% V is the number of decision variables. 
%
% This functions is basically written by the user who defines his/her own
% objective function. Make sure that the M and V matches your initial user
% input. Make sure that the 
%
% An example objective function is given below. It has two six decision
% variables are two objective functions.

% f = [];
% %% Objective function one
% % Decision variables are used to form the objective function.
% f(1) = 1 - exp(-4*x(1))*(sin(6*pi*x(1)))^6;
% sum = 0;
% for i = 2 : 6
%     sum = sum + x(i)/4;
% end
% %% Intermediate function
% g_x = 1 + 9*(sum)^(0.25);
% 
% %% Objective function two
% f(2) = g_x*(1 - ((f(1))/(g_x))^2);

%% Kursawe proposed by Frank Kursawe.
% Take a look at the following reference
% A variant of evolution strategies for vector optimization.
% In H. P. Schwefel and R. Männer, editors, Parallel Problem Solving from
% Nature. 1st Workshop, PPSN I, volume 496 of Lecture Notes in Computer 
% Science, pages 193-197, Berlin, Germany, oct 1991. Springer-Verlag. 
%
% Number of objective is two, while it can have arbirtarly many decision
% variables within the range -5 and 5. Common number of variables is 3.
f = [];

rho = 7.8*10^-6;
P = 10^6;
E = 2.07*10^8;
S_y = 3*10^5;
S_max = 5;

d = x(1);
l = x(2);

% Objective function one
f(1) = rho * pi() * d^2 * l / 4;

% Objective function two
f(2) = 64 * P * l^3 / (3 * E * pi() * d^4);

% Constraints as penalties
if 32 * P * l / (pi() * d^3) > S_y
    f(1) = f(1) + 10*(32 * P * l / (pi() * d^3) - S_y);
    f(2) = f(2) + 10*(32 * P * l / (pi() * d^3) - S_y);
end

if f(2) > S_max
    f(1) = f(1) + 10*(f(2) - S_max);
    f(2) = f(2) + 10*(f(2) - S_max);
end

%% Check for error
if length(f) ~= M
    error('The number of decision variables does not match you previous input. Kindly check your objective function');
end