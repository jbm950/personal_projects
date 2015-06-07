"""
%% Script file: prob7.m
%
% Purpose: This program will answer the seventh problem of the second
% homework assignment for system dynamics and control.
%
%
% Record of revisions:
%    Date        Programmer             Description of change
%   ======      ============        ======================================
%  2/7/2014     James Milam             Original code
%
% Definition of variables:
%  Il = current of the inductor
%  mf = magnetic flux linkage for a non-linear inductor
%  L = inductance of the inductor
%

%% initialize the magnetic flux for the given range and find the inductor
% current given the magnetic flux.

mf = -0.4:0.01:0.4;
Il = 97.3*mf.^3+4.2*mf;

%% Part a.) Plot the current, Il, as a function of the flux.

figure(1)
plot(mf,Il)
xlabel('Magnetic Flux (Wb)')
ylabel('Current (A)')
title('Part a.) Inductor Current vs Magenetic Flux Linkage')

%% Part b.) Plot the flux linkage as a function of the inductor current.

figure(2)
plot(Il,mf)
ylabel('Magnetic Flux (Wb)')
xlabel('Current (A)')
title('Part b.) Magenetic Flux Linkage vs Inductor Current')

%% Part c.) calculate the inductance fo the inductor as a funtion of the
% flux linkage and create a plot of this function.

% Initialize L

L = zeros(1,length(mf)-1);

% Calculate L for the varying magnetic flux

for ii = 1:length(mf)-1
    L(ii) = (mf(ii+1)-mf(ii))/(Il(ii+1)-Il(ii));
end

% Plot the inductance as a function of the magnetic flux

figure(3)
plot(mf(1:length(mf)-1),L)
xlabel('Magnetic Flux (Wb)')
ylabel('Inductance (H)')
title('Part c.) Inductance vs Magnetic Flux Linkage')
"""

import numpy as np
import matplotlib.pyplot as plt

mf = np.array(np.arange(-.4,.4,.01))
Il = 97.3*mf**3+4.2*mf
plt.figure(0)

plt.plot(mf,Il)
plt.xlabel('Magnetic Flux (Wb)')
plt.ylabel('Current (A)')
plt.title('Part a.) Inductor Current vs Magenetic Flux Linkage')
plt.show()

plt.figure(1)
plt.plot(Il,mf)
plt.ylabel('Magnetic Flux (Wb)')
plt.xlabel('Current (A)')
plt.title('Part b.) Magenetic Flux Linkage vs Inductor Current')
plt.show()


