%��Ϣ�ڵ��޸�

clear;clc;
%��Ҫ����
n = 14; k = 10;
N = 1024*1024*n;
m = 8;
T=[1,2,4,8,3,6,12,11,5,10,7,14,15,13,9];

%���ݵ���
load rs_data_b;
rs_data = rs_data_b;



msg  = gf(rs_data,8) ; 
code = rsdec(msg,n,k);