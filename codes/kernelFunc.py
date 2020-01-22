# -*- coding: utf-8 -*-
import numpy as np

class kernelFunc():
  #-------------------
  # kernelType: ���`���f��(0), �K�E�X�J�[�l��(1)�A�������J�[�l��(2)
  # kernelParam: �J�[�l���̍쐬�ɗp����p�����[�^�i�X�J���[�j  
  def __init__(self, kernelType=0, kernelParam=1):
    # �J�[�l���֐��̐ݒ�  
    kernelFuncs = [self.linear, self.gauss, self.poly]
    self.createMatrix = kernelFuncs[kernelType]
    self.kernelParam = kernelParam
  #-------------------

  #-------------------
  # ���`���f��
  def linear(self,X1,X2):
    return np.matmul(X1,X2.T)
  #-------------------
    
  #-------------------
  # �K�E�X�J�[�l��
  # X1�F���̓f�[�^�i�f�[�^���~��������numpy.array�j
  # X2�F���̓f�[�^�i�f�[�^���~��������numpy.array�j
  def gauss(self,X1,X2):
    X1Num = len(X1)
    X2Num = len(X2)
    
    # X1��X2�̑S�y�A�Ԃ̋����̌v�Z
    X1 = np.tile(np.expand_dims(X1.T,axis=2),[1,1,X2Num])
    X2 = np.tile(np.expand_dims(X2.T,axis=1),[1,X1Num,1])
    dist = np.sum(np.square(X1 - X2),axis=0)
    
    # �O�����s��iX1�̃f�[�^���~X2�̃f�[�^���j
    K = np.exp(-dist / (2 * (self.kernelParam ** 2)))
    
    return K
  #-------------------
  
  #-------------------  
  # �������J�[�l��
  # X1�F���̓f�[�^�i�f�[�^���~��������numpy.array�j
  # X2�F���̓f�[�^�i�f�[�^���~��������numpy.array�j
  def poly(self,X1,X2):

    # �O�����s��iX1�̃f�[�^���~X2�̃f�[�^���j
    K = (np.matmul(X1,X2.T) + 1)**self.kernelParam

    return K
  #-------------------
