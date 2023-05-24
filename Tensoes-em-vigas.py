#%%
#===============================================================================
#SEÇÃO RETANGULAR
#===============================================================================
#Funções utilizadas
from FuncoesFlexao import TensFlexRet

#Dados de entrada
b = 15 #cm (largura da base)
h = 35 #cm (altura)
Mz = 11 #kNm (momento em torno de z: +compressão no topo, -compressão na base)
My = 0 #kNm (momento em torno de y: +compressão à direita, -compressão à esquerda)
N = -110 #kN (Esforço normal na seção: +tração, -compressão)

#Cálculos
TensFlexRet(b, h, Mz, My, N)
# %%
#===============================================================================
#SEÇÃO EM I
#===============================================================================

from FuncoesFlexao import TensFlexI

d = 30 #cm
bf = 20 #cm
tw = 1.5
tf = 1.5
P=120 #kN
Mz = 2*P*0.25 #kNm (momento em torno de z: +compressão no topo, -compressão na base)
My = P*((75+7.5)/1000) #kNm (momento em torno de y: +compressão à direita, -compressão à esquerda)
N = -25 #kN

TensFlexI(d, bf, tf, tw, Mz, My, N)
#%%
##==============================================================================
#SEÇÃO EM C
#===============================================================================
from FuncoesFlexao import TensFlexC

d = 20.3
bf = 5.94
tw = 0.77
tf = 0.991
Mz = 0.71 #kNm (momento em torno de z: +compressão no topo, -compressão na base)
My = 0.26 #kNm (momento em torno de y: +compressão à direita, -compressão à esquerda)
N = 0 #kN

TensFlexC(d, bf, tw, tf, Mz, My, N)
#%%#===============================================================================
#SEÇÃO EM L
#===============================================================================