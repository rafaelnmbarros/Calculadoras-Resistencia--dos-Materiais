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
b = 20 #cm (largura da base)
h = 20 #cm (altura)
Mz = 0.001 #kNm (momento em z: +compressão no topo, -comp na base)
My = 0 #kNm (momento em y: +comp à direita, -comp à esquerda)
N = -20 #kN (esforço normal: +tração, -compressão)

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
Mz = 80 #kNm (momento em z: +compressão no topo, -comp na base)
My = 120 #kNm (momento em y: +comp à direita, -comp à esquerda)
N = -300 #kN (esforço normal: +tração, -compressão)

TensFlexI(d, bf, tf, tw, Mz, My, N)
#%%
#==============================================================================
#SEÇÃO EM C
#==============================================================================
from FuncoesFlexao import TensFlexC

d = 20.3 #cm (altura total)
bf = 5.94 #cm (largura da mesa)
tw = 0.77 #cm (espessura da alma)
tf = 0.991 #cm (espessura da mesa)
Mz = 1.128 #kNm (momento em z: +compressão no topo, -comp na base)
My = 0.41 #kNm (momento em y: +comp à direita, -comp à esquerda)
N = 0 #kN (esforço normal: +tração, -compressão)

TensFlexC(d, bf, tw, tf, Mz, My, N)
#%%
#==============================================================================
#SEÇÃO EM L
#==============================================================================

from FuncoesFlexao import TensFlexL

d = 30 #cm (altura total)
bf = 30 #cm (largura da mesa)
tw = 3 #cm (espessura da alma)
tf = 3 #cm (espessura da mesa)
Mz = 4 #kNm (momento em z: +compressão no topo, -comp na base)
My = 1 #kNm (momento em y: +comp à direita, -comp à esquerda)
N = -10 #kN (esforço normal: +tração, -compressão)

TensFlexL(d, bf, tw, tf, Mz, My, N)