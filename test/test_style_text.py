#!/usr/bin/env python3

import ROOT

from pyroot_cms_scripts import CMS_style

from pyroot_cms_scripts import CMS_text

CMS_style.cd()

f1 = ROOT.TF1("f1", "gaus", -5, 5)
f1.SetParameters(5, 0, 1.5)

h1 = ROOT.TH1F("h1", "h1", 50, -5, 5)
h1.FillRandom("f1", 2000)

h2 = ROOT.TH1F("h2", "h2", 50, -5, 5)
h2.FillRandom("f1", 2000)

h3 = ROOT.TH1F("h3", "h3", 50, -5, 5)
h3.FillRandom("f1", 2000)

h4 = ROOT.TH1F("h4", "h4", 50, -5, 5)
h4.FillRandom("f1", 6000)

stack = ROOT.THStack("stack", ";Varaible; Events")
stack.Add(h1)
stack.Add(h2)
stack.Add(h3)

h4.SetMarkerColor(ROOT.kBlack)
h4.SetLineColor(ROOT.kBlack)
h4.SetMarkerStyle(8)

maxY = max(stack.GetMaximum(), h4.GetMaximum())
stack.SetMaximum(maxY * 1.2)

canvas = ROOT.TCanvas()
stack.Draw("pfc")
h4.Draw("x0 e1 same")
CMS_text(canvas, cms_text_location="outside left", draw_extra_text=True, extra_text_location="outside left right", draw_lumi_text=True)
canvas.Print("1.png")

canvas = ROOT.TCanvas()
stack.Draw("pfc")
h4.Draw("x0 e1 same")
CMS_text(canvas, cms_text_location="inside left", draw_extra_text=True, extra_text_location="inside left below")
canvas.Print("2.png")


canvas = ROOT.TCanvas()
stack.Draw("pfc")
h4.Draw("x0 e1 same")
CMS_text(canvas, cms_text_location="inside left", draw_extra_text=True, extra_text_location="inside left right")
canvas.Print("3.png")


canvas = ROOT.TCanvas()
stack.Draw("pfc")
h4.Draw("x0 e1 same")
CMS_text(canvas, cms_text_location="inside center", draw_extra_text=True, extra_text_location="inside center below")
canvas.Print("4.png")


canvas = ROOT.TCanvas()
stack.Draw("pfc")
h4.Draw("x0 e1 same")
CMS_text(canvas, cms_text_location="inside right", draw_extra_text=True, extra_text_location="inside right below", draw_lumi_text=True)
canvas.Print("5.png")


canvas = ROOT.TCanvas()
stack.Draw("pfc")
h4.Draw("x0 e1 same")
CMS_text(canvas, cms_text_location="inside left", draw_extra_text=True, extra_text_location="inside left right")
CMS_text(canvas, draw_cms=False, draw_extra_text=True, extra_text_location="outside center", extra_text="#font[42]{arxiv:YYMM.NNNNN}")
canvas.Print("6.png")


canvas = ROOT.TCanvas()
stack.Draw("pfc")
h4.Draw("x0 e1 same")
CMS_text(canvas, cms_text_location="inside left", draw_extra_text=True, extra_text_location="inside left right")
CMS_text(canvas, draw_cms=False, draw_extra_text=True, extra_text_location="inside left below", extra_text="#font[42]{arxiv:YYMM.NNNNN}")
canvas.Print("7.png")

canvas = ROOT.TCanvas()

h5 = stack.GetStack().Last()

h4.SetTitle(stack.GetTitle())
h4.SetMaximum(maxY * 1.2)

ratio = ROOT.TRatioPlot(h4, h5)

ratio.SetH1DrawOpt("axis")
ratio.SetH2DrawOpt("axis")
ratio.SetGraphDrawOpt("p")

ratio.SetSeparationMargin(0)
ratio.SetLeftMargin(canvas.GetLeftMargin())
ratio.SetRightMargin(canvas.GetRightMargin())
ratio.SetUpTopMargin(0.075)
ratio.SetLowBottomMargin(0.40)

ratio.Draw("grid hideup")

ratio.GetLowYaxis().SetNdivisions(205)
ratio.GetLowerRefYaxis().SetTitle("Ratio")
ratio.GetLowerRefGraph().SetMinimum(-0.9)
ratio.GetLowerRefGraph().SetMaximum(2.9)
ratio.GetLowerRefGraph().SetMarkerStyle(6)

upper_pad = ratio.GetUpperPad()
upper_pad.cd()
stack.Draw("pfc same")
h4.Draw("x0 e1 same")

CMS_text(upper_pad, cms_text_scale=1.2, cms_text_location="inside left", draw_extra_text=True, extra_text_location="inside left right", extra_text="#scale[1.1]{Preliminary}", extra_text_pos_x_scale=1.02, draw_lumi_text=True, lumi_text="#scale[1.1]{3000 fb^{-1} (14 TeV)}")
CMS_text(upper_pad, draw_cms=False, draw_extra_text=True, extra_text_location="inside left below", extra_text="#scale[1.1]{#font[42]{arxiv:YYMM.NNNNN}}", extra_text_pos_y_scale=1.05)
canvas.Print("8.png")

input("Press any key to exit ... ")
