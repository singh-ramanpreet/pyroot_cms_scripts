import ROOT

def dphi(phi1, phi2):
    dphi = abs(phi1 - phi2)
    Pi = ROOT.TMath.Pi()
    if dphi > Pi:
        dphi = 2*Pi - dphi
    return dphi

def book_hist_1D(xbins, xlow, xup, titleX, units=""):
    variable = ROOT.TH1F("", "", xbins, xlow, xup)
    bw = variable.GetBinWidth(1)
    titleY = "Enteries/%s" % bw
    if units != "":
        titleX = titleX + " [" + units + "]"
        titleY = titleY + " " + units
    variable.SetTitle(";%s;%s" % (titleX, titleY))
    return variable

def book_hist_2D(xbins=1, xlow=0, xup=1, ybins=1, ylow=0, yup=1, titleX="", titleY="", titleZ="", 
                 unitsX="", unitsY="", unitsZ="", canExtend=False):
    variable = ROOT.TH2F("","", xbins, xlow, xup, ybins, ylow, yup)
    if canExtend:
        variable.SetCanExtend(ROOT.TH2.kAllAxes)
    if unitsX != "":
        titleX = titleX + " [" + unitsX + "]"
    if unitsY != "":
        titleY = titleY + " [" + unitsY + "]"
    if unitsZ != "":
        titleZ = titleZ + " [" + unitsZ + "]"
    variable.SetTitle(";" + titleX + ";" + titleY + ";" + titleZ)
    return variable
    
def clone_hist(h_hist_, keys):
    hist_dict = {"base": h_hist_}
    for key_ in keys:
        hist_dict[key_] = h_hist_.Clone()
    return hist_dict

def draw_hist_1D(canvas, hists, colors, legend_entries, legX1=0.75, legY1=0.75, legX2=0.9, legY2=0.85, 
                 textX=0.5, textY=0.8, text="", textSize=0.03, showStats=False, logY=False, normalize=False, 
                 drawOptions="", legend_markers=""):
    
    if isinstance(legend_markers, str): 
        if len(legend_markers) > 0:
            legend_markers = [legend_markers]*len(hists)
        else:
            legend_markers = ["f"]*len(hists)

    if isinstance(drawOptions, str):
        if len(drawOptions) > 0:
            drawOptions = [drawOptions]*len(hists)
        else:
            drawOptions = ["h"]*len(hists)

    latex = ROOT.TLatex(textX, textY, text)
    latex.SetNDC()
    latex.SetTextFont(42)
    latex.SetTextSize(textSize)
    
    legend = ROOT.TLegend(legX1, legY1, legX2, legY2)
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)
    legend.SetTextFont(42)
    
    for i in range(len(hists)):
        hist = hists[i]
        color = colors[i]
        legend_entry = legend_entries[i]
        hist.SetStats(int(showStats))
        hist.SetLineColor(color)
        hist.SetLineWidth(2)
        legend.AddEntry(hist, legend_entry, legend_markers[i])
        hist.SetOption(drawOptions[i])
        
    if normalize:
        hists.sort(key = lambda x: x.GetMaximum()/x.GetSumOfWeights(), reverse=True)
    else:
        hists.sort(key = lambda x: x.GetMaximum(), reverse=True)

    for h_ in hists:
        if normalize:
            norm_ = h_.DrawNormalized(h_.GetOption() + " same")
            ytitle = norm_.GetYaxis().GetTitle()
            if "Normalized" not in ytitle:
                norm_.GetYaxis().SetTitle("[Normalized] " + ytitle)
        else:
            h_.Draw(h_.GetOption() + " same")
    canvas.SetLogy(int(logY))
    return latex, legend
