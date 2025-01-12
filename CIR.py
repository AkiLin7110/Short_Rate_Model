# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 22:42:55 2020

@author: Aki

please save the file as CIR.py
"""
import numpy as np

class CIR(object):
    def __init__(self, alpha, mu, sigma, r0):
         self.alpha = alpha # mean-reverted speed
         self.mu = mu # mean-reverted level
         self.sigma = sigma # vol of interest rate
         self.r0 = r0 # initial interest rate
        
    def Euler(self,t_init,t_end,dt): #不同種隨機過程的模擬方式 #Euler
        np.random.seed(5)
        ts = np.arange(t_init, t_end, dt)
        dW = np.random.normal(loc=0.0, scale=np.sqrt(dt),size = ts.size)
        r = []
        r.append(self.r0)
        for i in range(1, ts.size):
            r.append(r[i-1] + self.alpha*(self.mu-r[i-1])*dt 
                     + self.sigma*np.sqrt(r[i-1])*dW[i-1])
        return r
    
    def Milstein(self,t_init,t_end,dt): #Milstein
        np.random.seed(5)
        ts = np.arange(t_init, t_end, dt)
        dW = np.random.normal(loc=0.0, scale=np.sqrt(dt),size = ts.size)
        r = []
        r.append(self.r0)
        for i in range(1, ts.size):
            dw = dW[i-1]
            r.append(r[i-1] + self.alpha*(self.mu-r[i-1])*dt 
                     + self.sigma*np.sqrt(r[i-1])*dw + 
                     (self.sigma**2/2)*(dw**2 - dt))
        return r
