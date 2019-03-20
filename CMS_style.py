import ROOT

def CMS_style(type="1D", ps_scale=2, axis_maxdigits=3):
    """Set CMS Style
    type: "1D" or "2D", Default: "1D"
    ps_scale: line width in PS graphics, eps, pdf, svg, etc
                Default: 2
    axis_maxdigits: max number of digits,
                    before switching to exponents
                    Default: 3
    """

    CMS_style = ROOT.TStyle("CMS_style", "CMS Style for Plots")
    ROOT.TGaxis().SetMaxDigits(axis_maxdigits)

    # Line Scale for PS graphics,
    # eps, pdf, svg, etc.
    CMS_style.SetLineScalePS(ps_scale)

    CMS_style.SetCanvasBorderMode(0)
    CMS_style.SetCanvasColor(ROOT.kWhite)
    CMS_style.SetCanvasDefH(600)
    if type == "1D":
        CMS_style.SetCanvasDefW(600)
    if type == "2D":
        CMS_style.SetCanvasDefW(700)    
    else:
        CMS_style.SetCanvasDefW(600)

    CMS_style.SetPadBorderMode(0)
    CMS_style.SetPadColor(ROOT.kWhite)
    CMS_style.SetPadGridX(False)
    CMS_style.SetPadGridY(False)

    CMS_style.SetPadTopMargin(0.075)
    CMS_style.SetPadBottomMargin(0.13)
    CMS_style.SetPadLeftMargin(0.13)
    if type == "1D":
        CMS_style.SetPadRightMargin(0.075)
    if type == "2D":
        CMS_style.SetPadRightMargin(0.165)
    else:
        CMS_style.SetPadRightMargin(0.075)

    # Global title
    CMS_style.SetOptTitle(0)
    CMS_style.SetTitleFont(42)
    CMS_style.SetTitleColor(1)
    CMS_style.SetTitleTextColor(1)
    CMS_style.SetTitleFillColor(10)
    CMS_style.SetTitleFontSize(0.045)
    CMS_style.SetTitleFillColor(0)
    CMS_style.SetTitleBorderSize(0)
    CMS_style.SetTitleAlign(23)

    # For the axis labels:
    CMS_style.SetLabelColor(1, "XYZ")
    CMS_style.SetLabelFont(42, "XYZ")
    CMS_style.SetLabelOffset(0.007, "XYZ")
    CMS_style.SetLabelSize(0.033, "XYZ")

    # For the axis:
    CMS_style.SetAxisColor(1, "XYZ")
    CMS_style.SetStripDecimals(True)
    CMS_style.SetTickLength(0.03, "XYZ")
    CMS_style.SetNdivisions(510, "XYZ")
    CMS_style.SetPadTickX(1) 
    CMS_style.SetPadTickY(1)

    CMS_style.SetTitleColor(1, "XYZ")
    CMS_style.SetTitleFont(42, "XYZ")
    CMS_style.SetTitleSize(0.04, "XYZ")
    CMS_style.SetTitleX(0.485)
    CMS_style.SetTitleY(0.985)
    CMS_style.SetTitleOffset(1.2, "X")
    CMS_style.SetTitleOffset(1.5, "Y")
    CMS_style.SetTitleOffset(1.3, "Z")

    CMS_style.SetGridColor(0)
    CMS_style.SetGridStyle(3)
    CMS_style.SetGridWidth(1)

    CMS_style.SetFrameBorderMode(0)
    CMS_style.SetFrameBorderSize(1)
    CMS_style.SetFrameFillColor(0)
    CMS_style.SetFrameFillStyle(0)
    CMS_style.SetFrameLineColor(1)
    CMS_style.SetFrameLineStyle(1)
    CMS_style.SetFrameLineWidth(1)

    CMS_style.SetOptFile(0)
    CMS_style.SetStatColor(ROOT.kWhite)
    CMS_style.SetStatFont(42)
    CMS_style.SetStatFontSize(0.03)
    CMS_style.SetStatTextColor(1)
    CMS_style.SetStatFormat("6.4g")
    CMS_style.SetStatBorderSize(1)
    CMS_style.SetStatH(0.1)
    CMS_style.SetStatW(0.15)
    #CMS_style.SetStatX(0.96)
    #CMS_style.SetStatY(0.94)
    
    CMS_style.cd()
