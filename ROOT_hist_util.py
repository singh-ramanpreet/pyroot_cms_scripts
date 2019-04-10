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
                 normScale=1, drawOptions="", legend_markers="", suppressYtitle=False):
    
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
            norm_ = h_.DrawNormalized(h_.GetOption() + " same", normScale)
            ytitle = norm_.GetYaxis().GetTitle()
            if "Normalized" not in ytitle:
                norm_.GetYaxis().SetTitle("[Normalized] " + ytitle)
            if suppressYtitle:
                norm_.GetYaxis().SetTitle("")
        else:
            if suppressYtitle:
                h_.GetYaxis().SetTitle("")
            h_.Draw(h_.GetOption() + " same")
    canvas.SetLogy(int(logY))
    return latex, legend

def draw_graph_1D(canvas, graphs, colors, legend_entries, legX1=0.75, legY1=0.75, legX2=0.9, legY2=0.85,
                  textX=0.5, textY=0.8, text="", textSize=0.03, logY=False, drawOptions="",
                  legend_markers="", suppressYtitle=False):

    if isinstance(legend_markers, str):
        if len(legend_markers) > 0:
            legend_markers = [legend_markers]*len(graphs)
        else:
            legend_markers = ["l"]*len(graphs)

    if isinstance(drawOptions, str):
        if len(drawOptions) > 0:
            drawOptions = [drawOptions]*len(graphs)
        else:
            drawOptions = ["C"]*len(graphs)

    latex = ROOT.TLatex(textX, textY, text)
    latex.SetNDC()
    latex.SetTextFont(42)
    latex.SetTextSize(textSize)

    legend = ROOT.TLegend(legX1, legY1, legX2, legY2)
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)
    legend.SetTextFont(42)

    for i in range(len(graphs)):
        graph = graphs[i]
        color = colors[i]
        legend_entry = legend_entries[i]
        graph.SetLineColor(color)
        graph.SetLineWidth(2)
        legend.AddEntry(graph, legend_entry, legend_markers[i])

        if suppressYtitle:
            graph.GetYaxis().SetTitle("")
        if i == 0:
            graph.Draw("A" + drawOptions[i])
        else:
            graph.Draw(drawOptions[i])
    canvas.SetLogy(int(logY))
    return latex, legend

def draw_efficiency_1D(canvas, Tefficiency_objects, colors, legend_entries,
                       YaxisMax=1.1, YaxisMin=0.01,
                       markerstyle="", fillstyle="", linewidth="",
                       legX1=0.2, legY1=0.8, legX2=0.35, legY2=0.9,
                       textX=0.5, textY=0.85, text="", textSize=0.05,
                       drawOptions="", legend_markers="",
                       canvasTitle="", titleX="Title X", titleY="Title Y"):

    legend = ROOT.TLegend(legX1, legY1, legX2, legY2)
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)
    legend.SetTextFont(42)

    latex = ROOT.TLatex(textX, textY, text)
    latex.SetNDC()
    latex.SetTextFont(42)
    latex.SetTextSize(textSize)

    if isinstance(drawOptions, str):
        if drawOptions == "":
            drawOptions = ["P"]*len(Tefficiency_objects)
        else:
            drawOptions = [drawOptions]*len(Tefficiency_objects)

    if isinstance(legend_markers, str):
        if legend_markers == "":
            legend_markers = ["L"]*len(Tefficiency_objects)
        else:
            legend_markers = [legend_markers]*len(Tefficiency_objects)

    title = canvasTitle + ";" + titleX + ";" + titleY

    for i, effPlot in enumerate(Tefficiency_objects):
        effPlot.SetLineColor(colors[i])
        if markerstyle != "": effPlot.SetMarkerStyle(markerstyle)
        if fillstyle   != "": effPlot.SetFillStyle(fillstyle)
        if linewidth   != "": effPlot.SetLineWidth(linewidth)
        legend.AddEntry(effPlot, legend_entries[i], legend_markers[i])

        effPlot.SetTitle(title)
        if i == 0:
            graph = effPlot.CreateGraph("AP")
            graph.Draw("A" + drawOptions[i])
            graph.GetHistogram().SetMaximum(YaxisMax)
            graph.GetHistogram().SetMinimum(YaxisMin)
        else:
            effPlot.Draw("same " + drawOptions[i])

    return legend, latex
