# -*- coding: utf-8 -*-
"""
Created on Fri May 26 10:16:12 2023

@author: Rafael Nascimento
"""

def TensCisRet(b, h, V):
    
    import numpy as np
    from scipy import integrate
    import matplotlib.pyplot as plt
    
    #--------------------------------------------------------------------------
    #Momento de inércia da seção
    #--------------------------------------------------------------------------
    
    I=(b*h**3)/12
    
    
    
    #--------------------------------------------------------------------------
    #Criação da malha
    #--------------------------------------------------------------------------
    npz = 100
    npy = 100
    z = np.linspace(-b/2,b/2,npz)
    y = np.linspace(-h/2,h/2,npy)
    Z, Y = np.meshgrid(z, y)

    #--------------------------------------------------------------------------
    #Cálculo das tensões
    #--------------------------------------------------------------------------
    tau = 10*(V/(2*I))*(0.25*h**2-Y**2)
    tau_max = np.max(tau)
    tau_min = np.min(tau)
    faixa = np.linspace(tau_min, tau_max, 10)
    
    
    #----------------------------------------------------
    #Vizualização dos resultados
    #----------------------------------------------------

    #Criação do gráfico
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect('equal')
    cores = 'gist_rainbow'

    # Plotagem do contorno de valores
    contour = ax.contourf(-Z, Y, tau, levels = faixa, cmap = cores,)

    # Adição da barra de cores
    cbar = fig.colorbar(contour)
    cbar.set_label('$\\tau $ (MPa)', fontdict={'fontsize': 12})
    
    #Adição de título ao gráfico
    ax.set_title('Distribuição de tensões de cisalhamento na seção \n \n',
                 fontdict={'fontsize': 14, 'fontweight': 'bold'})

    # Definição dos limites do gráfico
    lim_min = -max(b, h)/2
    lim_max = max(b, h)/2
    ax.set_xlim(lim_min, lim_max)
    ax.set_ylim(lim_min, lim_max)
    ax.set_xlabel('z (cm)', fontdict={'fontsize': 14})
    ax.set_ylabel('y (cm)', fontdict={'fontsize': 14})


    #Centroide da seção
    CG = ax.plot(0,0,
        'ko', label='Centroide'
    )

    #Legenda
    ax.legend()
    
    # Apresentação dos dados
    print('')
    print('')
    print('=================================================================')
    print('                    RESISTÊNCIA DOS MATERIAIS')
    print('                     Professor Rafael Barros')
    print('=================================================================')
    print('')
    print(' DISTRIBUIÇÃO DE TENSÕES DE CISALHAMETNO EM UMA VIGA RETANGULAR')
    print('-----------------------------------------------------------------')
    print('Força cortante:                     V         = %.2f kN' % V)
    print('Tensão de cisalhamento máxima:      tau_max   = %.2f MPa' % tau_max)
    print('-----------------------------------------------------------------')
    print('')


    plt.show()

###############################################################################
###############################################################################
b=20    #cm
h=40    #cm
V = 1000  #kN

TensCisRet(b, h, V)