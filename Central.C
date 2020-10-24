/// My attempt of writing a macro for the central limit theorem
#include "TMath.h"
#include "TF1.h"
#include "TCanvas.h"
#include "TLegend.h"
#include "TRandom3.h"
#include "TH1.h"
#include "TFile.h"
#include "TRatioPlot.h"
/*
To compile:
.L Central.C++

To execute:
TryMultiPDFs();

*/
void CentralLimit (TF1 *fpdf, TString outname, int ican);

void TryMultiPDFs(){
	
	//Define functions here
	const int Nsets = 5;
	TF1 *fPDF[Nsets];
	fPDF[0] = new TF1("pdf","TMath::Landau(x,[0],[1],0)",0,10);
	fPDF[0]->SetParameters(5.,1.0);
    fPDF[1] = new TF1("pdf","sin(x)/x",0,10);
    fPDF[2] = new TF1("pdf","TMath::DiLog(x)",0,10);
    fPDF[3] = new TF1("pdf","[0]", 0,10); // Uniform
    fPDF[3]->SetParameter(0,1.);
    fPDF[4] = new TF1("pdf","[0]/sqrt(2.0*TMath::Pi())/[2]*exp(-(x-[1])*(x-[1])/2./[2]/[2])", 0,10);
    fPDF[4]->SetParameters(1.,5.0,2.0);
    // string for outfile names
    TString OutfileName[Nsets] = {
    	"Landau",
    	"Sin",
    	"DiLog",
    	"uniform",
    	"gaus"
    };
    // Loop over the pdfs
	for(int i=0;i<Nsets;i++) {
	    CentralLimit(fPDF[i],OutfileName[i],i);
	}
}

void CentralLimit (TF1 *fpdf, TString outfilename,int ican)
{
	//Create a random number generator
	gRandom = new TRandom3();

	Double_t Nevt=1000000; //number of avarages
	Double_t Npdf=20; // sample size


	//Creating the histogram
	TH1D *hist = new TH1D("CentralLimit", ";x;N", 200, 0.0, 10);


	for(Int_t i = 0; i < Nevt; i++)
	{
		Double_t sum = 0; // The sum should always start on zero
		Double_t avg = 0; // the average over the summed samples

		for(Int_t i = 0; i < Npdf; i++)
		{
			sum += fpdf->GetRandom();
		}

		avg = sum / Npdf;
		hist -> Fill(avg);
	}

	
	TCanvas *c1 = new TCanvas(Form("c%d",ican), "Central Limit", 5,5,500,600);
	c1->Divide(1,2);
	c1->cd(1);
	fpdf->Draw();
	c1->cd(2);
	hist->Draw();
	hist->Fit("gaus");
	TF1 *myfit = hist -> GetFunction("gaus");

	//Simple ration plot with RatioPlot in ROOT. https://root.cern.ch/doc/v608/classTRatioPlot.html
	auto rp = new TRatioPlot(hist);
    rp->Draw();
    rp->GetLowerRefYaxis()->SetTitle("ratio");
	

	// Save figs
	c1->SaveAs(Form("figs/clt_%s.pdf",outfilename.Data()));
	// Write them out to a rootfile
	TFile *fout= new TFile(Form("results/outfile_%s.root",outfilename.Data()), "recreate");
	fout -> cd();
	hist -> Write();
	fpdf -> Write();
	myfit-> Write();
	fout -> Close();

}