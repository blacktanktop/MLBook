# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pylab as plt

#-------------------
# 1. �f�[�^�̓ǂݍ���
data = pd.read_csv('../data/house-prices-advanced-regression-techniques/train.csv')
#-------------------

#-------------------
# 2. �v���b�g 

# figure�̏�����
fig = plt.figure()

# GrLivArea��SalePrice�̎U�z�}
ax=fig.add_subplot(1,2,1)   #�O���t�̈ʒu�w��i1�s2���1��ځj
ax.plot(data['GrLivArea'],data['SalePrice'],'.')
ax.set_xlabel('GrLivArea')  #x���̃��x��
ax.set_ylabel('SalePrice')  #y���̃��x��

# MSSubClass��SalePrice�̎U�z�}
ax=fig.add_subplot(1,2,2)   #�O���t�̈ʒu�w��i1�s2���2��ځj
ax.plot(data['MSSubClass'],data['SalePrice'],'.')
ax.set_xlabel('MSSubClass') #x���̃��x��
ax.set_ylabel('SalePrice')  #y���̃��x��

fig.tight_layout()  # �O���t�ԂɌ��Ԃ�������
plt.show()  # �O���t�̕\��
#-------------------