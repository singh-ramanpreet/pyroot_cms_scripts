import ROOT

CMS_style = ROOT.TStyle("CMS_style", "CMS Style for Plots")


# For the canvas
CMS_style.SetCanvasBorderMode(0)
CMS_style.SetCanvasColor(ROOT.kWhite)
CMS_style.SetCanvasDefH(600)
CMS_style.SetCanvasDefW(600)
CMS_style.SetCanvasDefX(0)
CMS_style.SetCanvasDefY(0)


# For the Pad
CMS_style.SetPadBorderMode(0)
CMS_style.SetPadColor(ROOT.kWhite)
CMS_style.SetPadGridX(False)
CMS_style.SetPadGridY(False)
CMS_style.SetGridColor(0)
CMS_style.SetGridStyle(3)
CMS_style.SetGridWidth(1)


# For the frame
CMS_style.SetFrameBorderMode(0)
CMS_style.SetFrameBorderSize(1)
CMS_style.SetFrameFillColor(0)
CMS_style.SetFrameFillStyle(0)
CMS_style.SetFrameLineColor(1)
CMS_style.SetFrameLineStyle(1)
CMS_style.SetFrameLineWidth(1)


# For the histo
CMS_style.SetHistLineColor(1)
CMS_style.SetHistLineStyle(0)
CMS_style.SetHistLineWidth(1)
CMS_style.SetEndErrorSize(2)
CMS_style.SetMarkerStyle(20)


# For the fit/function
CMS_style.SetOptFit(1)
CMS_style.SetFitFormat("5.4g")
CMS_style.SetFuncColor(2)
CMS_style.SetFuncStyle(1)
CMS_style.SetFuncWidth(1)


# For the date
CMS_style.SetOptDate(0)


# For the statistics box:
CMS_style.SetOptFile(0)
CMS_style.SetOptStat(0)
CMS_style.SetStatColor(ROOT.kWhite)
CMS_style.SetStatFont(42)
CMS_style.SetStatFontSize(0.025)
CMS_style.SetStatTextColor(1)
CMS_style.SetStatFormat("6.4g")
CMS_style.SetStatBorderSize(1)
CMS_style.SetStatH(0.1)
CMS_style.SetStatW(0.15)


# Margins
CMS_style.SetPadTopMargin(0.06)
CMS_style.SetPadBottomMargin(0.13)
CMS_style.SetPadLeftMargin(0.15)
CMS_style.SetPadRightMargin(0.04)


# For the Global title
CMS_style.SetOptTitle(0)
CMS_style.SetTitleFont(42)
CMS_style.SetTitleColor(1)
CMS_style.SetTitleTextColor(1)
CMS_style.SetTitleFillColor(10)
CMS_style.SetTitleFontSize(0.05)
CMS_style.SetTitleBorderSize(0)
CMS_style.SetTitleAlign(23)


# For the axis titles
CMS_style.SetTitleColor(1, "XYZ")
CMS_style.SetTitleFont(42, "XYZ")
CMS_style.SetTitleSize(0.06, "XYZ")
CMS_style.SetTitleXOffset(0.9)
CMS_style.SetTitleYOffset(1.25)


# For the axis labels
CMS_style.SetLabelColor(1, "XYZ")
CMS_style.SetLabelFont(42, "XYZ")
CMS_style.SetLabelOffset(0.007, "XYZ")
CMS_style.SetLabelSize(0.05, "XYZ")


# For the axis
CMS_style.SetAxisColor(1, "XYZ")
CMS_style.SetStripDecimals(ROOT.kTRUE)
CMS_style.SetTickLength(0.03, "XYZ")
CMS_style.SetNdivisions(510, "XYZ")
CMS_style.SetPadTickX(1)
CMS_style.SetPadTickY(1)


# Change for log plots
CMS_style.SetOptLogx(0)
CMS_style.SetOptLogy(0)
CMS_style.SetOptLogz(0)


# Postscript options
CMS_style.SetPaperSize(20.0 , 20.0)
# SetLineScalePS(Float_t scale = 3)
# SetLineStyleString(Int_t i, const char* text)
# SetHeaderPS(const char* header)
# SetTitlePS(const char* pstitle)

# SetBarOffset(Float_t baroff = 0.5)
# SetBarWidth(Float_t barwidth = 0.5)
# SetPaintTextFormat(const char* format = "g")
# SetPalette(Int_t ncolors = 0, Int_t* colors = 0)
# SetTimeOffset(Double_t toffset)
# SetHistMinimumZero(kTRUE)


CMS_style.SetHatchesLineWidth(5)
CMS_style.SetHatchesSpacing(0.05)
