import numpy as np
import ROOT

import sys
sys.path.append("JPyPlotRatio");
#https://github.com/jaelpark/JPyPlotRatio

import JPyPlotRatio

pdfnames = [
        "Landau",
        "Sin",
        "DiLog",
        "uniform",
        "gaus"
];

# define manually option 1 in case ROOT files are not named according to pdfnames
InfilesTest = [
	"results/outfile_Landau.root",
	"results/outfile_Sin.root",
	"results/outfile_DiLog.root",
	"results/outfile_uniform.root",
	"results/outfile_gaus.root"
];
# make infile names according to pdfnames
Infiles = [];
for i in range(0,len(pdfnames)):	
	tmpstr = "results/outfile_{:s}.root".format(pdfnames[i]);
	print("{:s}".format(tmpstr));
	Infiles.append(tmpstr);


fin = [ROOT.TFile(elm) for elm in Infiles];
#fin = [ROOT.TFile(elm) for elm in InfilesTest];

i = 1;


fin[i].Print();
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

#load histogram from fin
gr = fin[i].Get("CentralLimit");
fit = fin[i].Get("gaus");


#add histogram
p1 = plot.Add(0, gr, color="orchid", linestyle="dotted", label="sampled");
p2 = plot.Add(0, fit, color="red",label="fit");
plot.Ratio(p1,p2)



fin[i].Close();

plot.Plot();

	
figures = "figs/plot_{:s}.pdf".format(pdfnames[i]);
print("{:s}".format(figures));
plot.Save(figures)


