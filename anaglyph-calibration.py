#!/usr/bin/env python2
from psychopy import visual, event, core, logging

""" DESCRIPTION:
This script allow to calibrate colors to use in an anaglyph presentation with
respect to a specific monitor and specific color filters.
Please see http://www.github.com/thomastweets/anaglyph-calibration for more
information.

Author: Thomas Emmerling (Maastricht University)
"""

myWin = visual.Window((800,800), monitor='testMonitor', useFBO=True,
    color=[-0.9,-0.9,-0.9], colorSpace='rgb')
stims = []
step = 0.01 #define the step size of the color adjustment

cycle = 0
colorCycle = [
    'rWr', 'rWg', 'rWb',
    'bWr', 'bWg', 'bWb',
    'rBr', 'rBg', 'rBb',
    'bBr', 'bBg', 'bBb',
    'BGr', 'BGg', 'BGb'
]
colors = {
    'rWr': {'t': 'red White\n red', 'c': 1.0},
    'rWg': {'t': 'red White\n green', 'c': -0.0199},
    'rWb': {'t': 'red White\n blue', 'c': -0.009999999999999997},
    'bWr': {'t': 'blue White\n red', 'c': -0.03},
    'bWg': {'t': 'blue White\n green', 'c': 1.0},
    'bWb': {'t': 'blue White\n blue', 'c': 1.0},
    'rBr': {'t': 'red Black\n red', 'c': -1.0},
    'rBg': {'t': 'red Black\n green', 'c': 1.0},
    'rBb': {'t': 'red Black\n blue', 'c': 1.0},
    'bBr': {'t': 'blue Black\n red', 'c': 1.0},
    'bBg': {'t': 'blue Black\n green', 'c': -1.0},
    'bBb': {'t': 'blue Black\n blue', 'c': -1.0},
    'BGr': {'t': 'BG\n red', 'c': -0.7},
    'BGg': {'t': 'BG\n green', 'c': -1.0},
    'BGb': {'t': 'BG\n blue', 'c': -0.7}
}

rW = [0.0, 0.0, 0.0]
bW = [0.0, 0.0, 0.0]
rB = [0.0, 0.0, 0.0]
bB = [0.0, 0.0, 0.0]
BG = [0.0, 0.0, 0.0]

def compCol():
    global rW, bW, rB, bB, BG
    rW = tuple([colors['rWr']['c'],colors['rWg']['c'],colors['rWb']['c']])
    bW = tuple([colors['bWr']['c'],colors['bWg']['c'],colors['bWb']['c']])
    rB = tuple([colors['rBr']['c'],colors['rBg']['c'],colors['rBb']['c']])
    bB = tuple([colors['bBr']['c'],colors['bBg']['c'],colors['bBb']['c']])
    BG = tuple([colors['BGr']['c'],colors['BGg']['c'],colors['BGb']['c']])
compCol()

op=1.0
#rgb colors
colText = visual.TextStim(myWin, color='white', text=colors[colorCycle[cycle]]['t'], alignHoriz = 'center', pos=[0.0, 0.9])
rWStim = visual.GratingStim(myWin, mask='None',color=rW, opacity=op, colorSpace='rgb', pos=[-0.2,-0.5],sf=0)
bWStim = visual.GratingStim(myWin, mask='None',color=bW, opacity=op, colorSpace='rgb', pos=[0.2,-0.5],sf=0)
rBStim = visual.GratingStim(myWin, mask='None',color=rB, opacity=op, colorSpace='rgb', pos=[-0.2,0.5],sf=0)
bBStim = visual.GratingStim(myWin, mask='None',color=bB, opacity=op, colorSpace='rgb', pos=[0.2,0.5],sf=0)

WStim = visual.GratingStim(myWin, mask='None',color=(-1.0,-1.0,-1.0), opacity=op, colorSpace='rgb', pos=[-0.2,0.0],sf=0)
BStim = visual.GratingStim(myWin, mask='None',color=(1.0,1.0,1.0), opacity=op, colorSpace='rgb', pos=[0.2,0.0],sf=0)

rWDots = visual.DotStim(myWin, nDots=200, dir=0.0, dotLife=-1, contrast=1.0, noiseDots='direction',
    speed=0.001, signalDots='same', coherence= 0.0, dotSize=9, color=rW, opacity=op, colorSpace='rgb', fieldPos=[-0.2,-0.5])
bWDots = visual.DotStim(myWin, nDots=200, dir=0.0, dotLife=-1, contrast=1.0, noiseDots='direction',
    speed=0.001, signalDots='same', coherence= 0.0, dotSize=9, color=bW, opacity=op, colorSpace='rgb', fieldPos=[0.2,-0.5])
rBDots = visual.DotStim(myWin, nDots=200, dir=0.0, dotLife=-1, contrast=1.0, noiseDots='direction',
    speed=0.001, signalDots='same', coherence= 0.0, dotSize=9, color=rB, opacity=op, colorSpace='rgb', fieldPos=[-0.2,0.5])
bBDots = visual.DotStim(myWin, nDots=200, dir=0.0, dotLife=-1, contrast=1.0, noiseDots='direction',
    speed=0.001, signalDots='same', coherence= 0.0, dotSize=9, color=bB, opacity=op, colorSpace='rgb', fieldPos=[0.2,0.5])

WDots = visual.DotStim(myWin, nDots=200, dir=0.0, dotLife=-1, contrast=1.0, noiseDots='direction',
    speed=0.001, signalDots='same', coherence= 0.0, dotSize=9, color=(1.0,1.0,1.0), opacity=op, colorSpace='rgb', fieldPos=[-0.2,0.0])
BDots = visual.DotStim(myWin, nDots=200, dir=0.0, dotLife=-1, contrast=1.0, noiseDots='direction',
    speed=0.001, signalDots='same', coherence= 0.0, dotSize=9, color=(-1.0,-1.0,-1.0), opacity=op, colorSpace='rgb', fieldPos=[0.2,0.0])

calibrating = True
while(calibrating):
    compCol()

    myWin.setColor(BG)

    rWStim.setColor(rW)
    bWStim.setColor(bW)
    rBStim.setColor(rB)
    bBStim.setColor(bB)

    rWDots.setColor(rW)
    bWDots.setColor(bW)
    rBDots.setColor(rB)
    bBDots.setColor(bB)

    rWStim.draw()
    bWStim.draw()
    rBStim.draw()
    bBStim.draw()
    WStim.draw()
    BStim.draw()

    rWDots.draw()
    bWDots.draw()
    rBDots.draw()
    bBDots.draw()
    WDots.draw()
    BDots.draw()

    colText.setText(''.join([colors[colorCycle[cycle]]['t'], '  ', str(colors[colorCycle[cycle]]['c'])]))
    colText.draw()
    myWin.flip()
    keys = event.getKeys()
    for k in keys:
        if k == "1": # go to the next color
            if cycle > 0:
                cycle -= 1
        if k == "2": # go to the previous color
            if cycle < len(colorCycle)-1:
                cycle += 1
        if k == "4": # increase the value
            if colors[colorCycle[cycle]]['c'] < 1.0:
                colors[colorCycle[cycle]]['c'] += step
        if k == "3": # decrease the value
            if colors[colorCycle[cycle]]['c'] > -1.0:
                colors[colorCycle[cycle]]['c'] -= step
        if k == "6": # increase the value fast (10x)
            if colors[colorCycle[cycle]]['c'] < 1.0:
                colors[colorCycle[cycle]]['c'] += 10*step
        if k == "5": # decrease the value fast (10x)
            if colors[colorCycle[cycle]]['c'] > -1.0:
                colors[colorCycle[cycle]]['c'] -= 10*step

        if k == "q": # quit
            calibrating = False
        print('rW: ', rW)
        print('bW: ', bW)
        print('rB: ', rB)
        print('bB: ', bB)
        print('BG: ', BG)

myWin.close()
