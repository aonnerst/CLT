import numpy as np
import ROOT

import sys
sys.path.append("JPyPlotRatio");
#https://github.com/jaelpark/JPyPlotRatio

import JPyPlotRatio


f = ROOT.TFile("outfile.root","read");
# define panel/xaxis limits/titles
# add here the histogram names for each pad

#histnames = ["CenntralLimit"]; # histogram names in ROOT file
# add labels for each pad
plables = ["Central Limit Theorem"];
# model names : for histonames in ROOT file

# Following two must be added
toptitle = "Central Limit Theorem"; # need to add on the top
dataDetail = ["more"];


plot = JPyPlotRatio.JPyPlotRatio(panels=(1,1),
	disableRatio=[],    #to get rid of the 0th ratio panel
	axisLabelSize=9,
	tickLabelSize=7,
	#rowBounds=ylimits,  # for nrow
	#colBounds=xlimits,  # for ncol
	panelLabel=plables,  # nrowxncol
	#ratioBounds=rlimits,# for nrow
#	ratioSystPlot=True,

	panelLabelLoc=(0.55,0.57),panelLabelSize=5,panelLabelAlign="left",
	legendPanel=0,
	legendLoc=(0.73,0.80),legendSize=5,xlabel="sample mean",ylabel="# averages");


#plot.EnableLatex(True); # for publication need fonts via texlive

#load histogram from f
gr = f.Get("CentralLimit")
fit = f.Get("gaus")

#add histogram
p1 = plot.Add(0, gr, color="orchid", linestyle="dotted", label="sampled");
p2 = plot.Add(0, fit, color="red",label="fit");
plot.Ratio(p1,p2)

#compare to "model", gaussian in this case, if needed(?)
#model = f.Get("fgaus");
#plot.Ratio(model,data );

f.Close();

plot.Plot();

plot.Save("figs/xx.pdf");
plot.Show();
