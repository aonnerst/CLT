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

for i in range(0,len(pdfnames)):
	fin[i].Print();