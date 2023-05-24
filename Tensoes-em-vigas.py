"""
###############################################################################
#                          RESISTÊNCIA DOS MATERIAIS                  _y|__   #
#                           Professor Rafael Barros                  |  |  |  #
#                                                                  z_|__|  |  #
#              TENSÕES EM SEÇÕES SOB MOMENTO FLETOR E FORÇA AXIAL    |     |  #
#                                                                    |_____|  #
#                                                                             #
###############################################################################
"""


#%%
#==============================================================================
#SEÇÃO RETANGULAR
#==============================================================================
#Funções utilizadas
from FuncoesFlexao import TensFlexRet

#Dados de entrada
b = 15 #cm (largura da base)
h = 35 #cm (altura)
Mz = 11 #kNm (momento em z: +compressão no topo, -comp na base)
My = 0 #kNm (momento em y: +comp à direita, -comp à esquerda)
N = -110 #kN (esforço normal: +tração, -compressão)

#Cálculos
TensFlexRet(b, h, Mz, My, N)
# %%
#==============================================================================
#SEÇÃO EM I
#==============================================================================

from FuncoesFlexao import TensFlexI

d = 30 #cm (altura total)
bf = 20 #cm (largura da mesa)
tw = 1.5 #cm (espessura da alma)
tf = 1.5 #cm (espessura da mesa)
Mz = 60 #kNm (momento em z: +compressão no topo, -comp na base)
My = 70 #kNm (momento em y: +comp à direita, -comp à esquerda)
N = -25 #kN (esforço normal: +tração, -compressão)

TensFlexI(d, bf, tf, tw, Mz, My, N)
#%%
##=============================================================================
#SEÇÃO EM C
#==============================================================================
from FuncoesFlexao import TensFlexC

d = 20.3 #cm (altura total)
bf = 5.94 #cm (largura da mesa)
tw = 0.77 #cm (espessura da alma)
tf = 0.991 #cm (espessura da mesa)
Mz = 0.71 #kNm (momento em z: +compressão no topo, -comp na base)
My = 0.26 #kNm (momento em y: +comp à direita, -comp à esquerda)
N = 0 #kN (esforço normal: +tração, -compressão)

TensFlexC(d, bf, tw, tf, Mz, My, N)
#%%#===========================================================================
#SEÇÃO EM L
#==============================================================================

from FuncoesFlexao import TensFlexL

d = 40 #cm (altura total)
bf = 20 #cm (largura da mesa)
tw = 2 #cm (espessura da alma)
tf = 5 #cm (espessura da mesa)
Mz = 0.71 #kNm (momento em z: +compressão no topo, -comp na base)
My = 0.26 #kNm (momento em y: +comp à direita, -comp à esquerda)
N = -5 #kN (esforço normal: +tração, -compressão)

TensFlexL(d, bf, tw, tf, Mz, My, N)