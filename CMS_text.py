import ROOT

def CMS_text(pad):
    """Insert text outside frame, in upper-left
    pad: pad or canvas"""
    H = pad.GetWh()
    W = pad.GetWw()
    l = pad.GetLeftMargin()
    t = pad.GetTopMargin()
    r = pad.GetRightMargin()
    b = pad.GetBottomMargin()
    
    pad.cd()
    
    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextAngle(0)
    latex.SetTextColor(ROOT.kBlack)

    cms_text = "CMS"
    cms_text_font = 61
    cms_text_size = 0.04
    cms_text_offset = 0.1
    
    write_extra_text = True
    extra_text   = "Preliminary"
    extra_text_font = 52
    extra_text_size = 0.03

    posx = 1.7*l
    posy = 1 - 0.9*t
    
    latex.SetTextAlign(31)
    latex.SetTextFont(cms_text_font)
    latex.SetTextSize(cms_text_size)
    latex.DrawLatex(posx, posy, cms_text)
    
    latex.SetTextAlign(11)
    latex.SetTextFont(extra_text_font)
    latex.SetTextSize(extra_text_size)
    latex.DrawLatex(posx + 0.05*l, posy, extra_text)
