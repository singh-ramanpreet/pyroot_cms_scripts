import ROOT

def CMS_text(
    pad, 
    draw_cms=True,
    cms_text="CMS",
    cms_text_location="inside left",
    cms_pos_x_scale=1.0,
    cms_pos_y_scale=1.0,
    draw_extra_text=False,
    extra_text="Preliminary",
    extra_text_location="inside left below",
    extra_text_pos_x_scale=1.0,
    extra_text_pos_y_scale=1.0,
    draw_lumi_text=False,
    lumi_text="#scale[0.95]{3000 fb^{-1} (14 TeV)}",
    lumi_text_pos_x_scale=1.0,
    lumi_text_pos_y_scale=1.0
):
    """Insert text outside frame, in upper-left
    
    Parameters
    ----------
    pad : instance of ROOT.TPad or ROOT.TCanvas
        pad or canvas to draw on
    draw_cms : bool, optional
        draws "CMS" text (default is True)
    cms_text : str, optional
        cms text (default is "CMS")
    cms_text_location : str, optional
        location of cms_text, (default is "inside left")
        options, "outside left"
                 "inside left"
                 "inside center"
                 "inside right"
    cms_pos_x_scale : float, optional
        for fine positioning of cms_text (default is 1.0)
    cms_pos_y_scale : float, optional
        for fine positioning of cms_text (default is 1.0)
    draw_extra_text : bool, optional
        draw extra text next cms_text (default is False)
    extra_text: str, optional
        extra text (default is "Preliminary")
    extra_text_location : str, optional
        location of extra_text, (default is "inside left below")
        options, "outside left right"
                 "inside left below"
                 "inside left right"
                 "inside center below"
                 "inside right below"
                 "outside center"
    extra_pos_x_scale : float, optional
        for fine positioning of extra_text (default is 1.0)
    extra_pos_y_scale : float, optional
        for fine positioning of extra_text (default is 1.0)
    
    draw_lumi_text : bool, optional
        draw lumi text on top right outside frame (default is False)
    lumi_text: str, optional
        extra text (default is "#scale[0.95]{3000 fb^{1} (14 TeV)}")
    lumi_pos_x_scale : float, optional
        for fine positioning of lumi_text (default is 1.0)
    lumi_pos_y_scale : float, optional
        for fine positioning of lumi_text (default is 1.0)
    
    Returns
    -------
    instance of ROOT.TLatex used to draw.
    """


    pad_height = pad.GetWh()
    pad_width = pad.GetWw()
    pad_left_margin = pad.GetLeftMargin()
    pad_top_margin = pad.GetTopMargin()
    pad_right_margin = pad.GetRightMargin()
    pad_bottom_margin = pad.GetBottomMargin()

    pad.cd()

    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextAngle(0)
    latex.SetTextColor(ROOT.kBlack)


    cms_text_font = 61
    cms_text_size = 0.6 * pad_top_margin

    if cms_text_location == "outside left":

        cms_text_pos_x = cms_pos_x_scale * 1.1 * pad_left_margin
        cms_text_pos_y = 1 - cms_pos_y_scale * 0.53 * pad_top_margin
        cms_text_align = 13

    if cms_text_location == "inside left":

        cms_text_pos_x = cms_pos_x_scale * 1.25 * pad_left_margin
        cms_text_pos_y = 1 - cms_pos_y_scale * 1.40 * pad_top_margin
        cms_text_align = 13

    if cms_text_location == "inside center":

        cms_text_pos_x = cms_pos_x_scale * 4.05 * pad_left_margin
        cms_text_pos_y = 1 - cms_pos_y_scale * 1.40 * pad_top_margin
        cms_text_align = 23

    if cms_text_location == "inside right":

        cms_text_pos_x = cms_pos_x_scale * 6.85 * pad_left_margin
        cms_text_pos_y = 1 - cms_pos_y_scale * 1.40 * pad_top_margin
        cms_text_align = 33

    if draw_cms:
        latex.SetTextAlign(cms_text_align)
        latex.SetTextFont(cms_text_font)
        latex.SetTextSize(cms_text_size)
        latex.DrawLatex(cms_text_pos_x, cms_text_pos_y, cms_text)
    
    
    extra_text_font = 52
    extra_text_size = 0.4 * pad_top_margin

    if extra_text_location == "outside left right":

        extra_text_pos_x = extra_text_pos_x_scale * 1.85 * pad_left_margin
        extra_text_align = 13
        extra_text_pos_y = 1 - extra_text_pos_y_scale * 0.63 * pad_top_margin


    if "inside left" in extra_text_location:

        if "below" in extra_text_location:

            extra_text_pos_x = extra_text_pos_x_scale * 1.25 * pad_left_margin
            extra_text_align = 13
            extra_text_pos_y = 1 - extra_text_pos_y_scale * 1.90 * pad_top_margin

        if "right" in extra_text_location:

            extra_text_pos_x = extra_text_pos_x_scale * 2.00 * pad_left_margin
            extra_text_align = 13
            extra_text_pos_y = 1 - extra_text_pos_y_scale * 1.5 * pad_top_margin


    if extra_text_location == "inside center below":

        extra_text_pos_x = extra_text_pos_x_scale * 4.05 * pad_left_margin
        extra_text_align = 23
        extra_text_pos_y = 1 - extra_text_pos_y_scale * 1.90 * pad_top_margin


    if extra_text_location == "inside right below":

        extra_text_pos_x = extra_text_pos_x_scale * 6.85 * pad_left_margin
        extra_text_align = 33
        extra_text_pos_y = 1 - extra_text_pos_y_scale * 1.90 * pad_top_margin


    if extra_text_location == "outside center":

        extra_text_pos_x = extra_text_pos_x_scale * 4.05 * pad_left_margin
        extra_text_align = 23
        extra_text_pos_y = 1 - extra_text_pos_y_scale * 0.53 * pad_top_margin       

    if draw_extra_text:
        latex.SetTextAlign(extra_text_align)
        latex.SetTextFont(extra_text_font)
        latex.SetTextSize(extra_text_size)
        latex.DrawLatex(extra_text_pos_x, extra_text_pos_y, extra_text)
        
    lumi_text_font = 42
    lumi_text_size = 0.55 * pad_top_margin
    lumi_text_align = 31

    lumi_text_pos_x = lumi_text_pos_x_scale * 7.1 * pad_left_margin
    lumi_text_pos_y = 1 - lumi_text_pos_y_scale * 0.88 * pad_top_margin
    
    if draw_lumi_text:
        latex.SetTextAlign(lumi_text_align)
        latex.SetTextFont(lumi_text_font)
        latex.SetTextSize(lumi_text_size)
        latex.DrawLatex(lumi_text_pos_x, lumi_text_pos_y, lumi_text)
    
    return latex
