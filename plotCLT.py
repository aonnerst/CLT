import numpy as np
import ROOT

import scipy
from scipy import interpolate

import sys
sys.path.append("JPyPlotRatio");
#https://github.com/jaelpark/JPyPlotRatio


import JPyPlotRatio


f = ROOT.TFile("outfile.root","read");
dataTypePlotParams = [
	{'plotType':'data','color':'k','fmt':'o','markersize':5.0},
	{'plotType':'theory','facecolor':'C0','edgecolor':'C0','alpha':0.5,'linestyle':'solid','linecolor':'C0'},
	{'plotType':'theory','facecolor':'C1','edgecolor':'C1','alpha':0.5,'linestyle':'dotted','linecolor':'C1'},
	{'plotType':'theory','facecolor':'C2','edgecolor':'C2','alpha':0.5,'linestyle':'dashed','linecolor':'C2'},
	{'plotType':'theory','facecolor':'C3','edgecolor':'C3','alpha':0.5,'linestyle':'dashdot','linecolor':'C3'},
];


# define panel/xaxis limits/titles
nrow = 1;
ncol = 1;
xlimits = [(0.0,20.0)];
ylimits = [(0.0,10.0)];
rlimits = [(0.,2.)];


# add here the histogram names for each pad
histnames =      ["CentralLimit"]; # histogram names in ROOT file
# add labels for each pad
plables = [ "Something" ];
# model names : for histonames in ROOT file
xtitle = ["x title"];
ytitle = ["y title"];

# Following two must be added
toptitle = "Central Limit Theorem"; # need to add on the top
dataDetail = ["more"];


plot = JPyPlotRatio.JPyPlotRatio(panels=(nrow,ncol),
	rowBounds=ylimits,  # for nrow
	colBounds=xlimits,  # for ncol
	panelLabel=plables,  # nrowxncol
	ratioBounds=rlimits,# for nrow
#	ratioSystPlot=True,
	panelLabelLoc=(0.07,0.51),panelLabelSize=8,panelLabelAlign="left",
	legendPanel=1,
	legendLoc=(0.47,0.77),legendSize=9,xlabel=xtitle[0],ylabel=ytitle[0]);


#plot.EnableLatex(True); # for publication need fonts via texlive

plotMatrix = np.empty((nrow,ncol),dtype=int);


for i in range(0,nrow):
	for j in range(0,ncol):
		index = i*ncol+j; # for each panel 
		gr = f.Get("{}".format(histnames[j]));
		model = f.Get("fgaus");
		data = plot.Add(index,gr,**dataTypePlotParams[0],label="sampled");
		plot.Ratio(model,data );

f.Close();

plot.Save("figs/xx.pdf");
plot.Save("figs/xx.png");
plot.Show();
