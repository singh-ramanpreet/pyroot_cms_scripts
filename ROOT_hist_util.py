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
