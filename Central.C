/// My attempt of writing a macro for the central limit theorem
#include "TMath.h"
#include "TF1.h"
#include "TCanvas.h"
#include "TLegend.h"
#include "TRandom3.h"
#include "TH1.h"
/*
To compile:
.L Central.C++

To execute:
.x Central.C

*/


void Central()
{
	//Create a random number generator
	gRandom = new TRandom3();


	//Defining the Landau probability distribution function
	TF1 *pdf = new TF1("pdf","TMath::Landau(x,[0],[1],0)",0,20);
	//Setting the parameters for the Landau function (most prbable value, not well defined sigma)
	pdf->SetParameters(5.,1.0);


	Double_t N=1000000; //number of avarages
	Double_t n=20; // sample size


	//Creating the histogram
	TH1D *hist = new TH1D("CentralLimit", ";x;N", 200, 0.0, 20);


	for(Int_t i = 0; i < N; i++)
	{
		Double_t sum = 0; // The sum should always start on zero
		Double_t avg = 0; // the average over the summed samples

		for(Int_t i = 0; i < n; i++)
		{
			sum += pdf->GetRandom();
		}

		avg = sum / n;
		hist -> Fill(avg);
	}

	TCanvas *c1 = new TCanvas("c1", "Central Limit", 5,5,800,600);
	hist->Draw();
	hist->Fit("gaus");
	c1->SaveAs("/Users/absonner/work/FlowEx/CLT/figs/clt.pdf");

	TCanvas *c2 = new TCanvas("c2", "Landau Function", 5,5,800,600);
	pdf->Draw();
	c2->SaveAs("/Users/absonner/work/FlowEx/CLT/figs/landau.pdf");

}