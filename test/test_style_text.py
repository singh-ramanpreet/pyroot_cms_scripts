#!/usr/bin/env python3

import ROOT

from pyroot_cms_scripts import CMS_style

from pyroot_cms_scripts import CMS_text

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

CMS_style("1D")
canvas = ROOT.TCanvas()
stack.Draw("pfc")
h4.Draw("x0 e1 same")
CMS_text(canvas, cms_text_location="outside left", draw_extra_text=True, extra_text_location="outside left right", draw_lumi_text=True)
canvas.Print("1.png")


CMS_style("1D")
canvas = ROOT.TCanvas()
stack.Draw("pfc")
h4.Draw("x0 e1 same")
CMS_text(canvas, cms_text_location="inside left", draw_extra_text=True, extra_text_location="inside left below")
canvas.Print("2.png")


CMS_style("1D")
canvas = ROOT.TCanvas()
stack.Draw("pfc")
h4.Draw("x0 e1 same")
CMS_text(canvas, cms_text_location="inside left", draw_extra_text=True, extra_text_location="inside left right")
canvas.Print("3.png")

CMS_style("1D")
canvas = ROOT.TCanvas()
stack.Draw("pfc")
h4.Draw("x0 e1 same")
CMS_text(canvas, cms_text_location="inside center", draw_extra_text=True, extra_text_location="inside center below")
canvas.Print("4.png")


CMS_style("1D")
canvas = ROOT.TCanvas()
stack.Draw("pfc")
h4.Draw("x0 e1 same")
CMS_text(canvas, cms_text_location="inside right", draw_extra_text=True, extra_text_location="inside right below", draw_lumi_text=True)
canvas.Print("5.png")


CMS_style("1D")
canvas = ROOT.TCanvas()
stack.Draw("pfc")
h4.Draw("x0 e1 same")
CMS_text(canvas, cms_text_location="inside left", draw_extra_text=True, extra_text_location="inside left right")
CMS_text(canvas, draw_cms=False, draw_extra_text=True, extra_text_location="outside center", extra_text="#font[42]{arxiv:YYMM.NNNNN}")
canvas.Print("6.png")

CMS_style("1D")
canvas = ROOT.TCanvas()
stack.Draw("pfc")
h4.Draw("x0 e1 same")
CMS_text(canvas, cms_text_location="inside left", draw_extra_text=True, extra_text_location="inside left right")
CMS_text(canvas, draw_cms=False, draw_extra_text=True, extra_text_location="inside left below", extra_text="#font[42]{arxiv:YYMM.NNNNN}")
canvas.Print("7.png")

input("Press any key to exit ... ")
