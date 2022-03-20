clear;clc;
%主要参数
n = 14; k = 10;
N = 1024*1024*k;
m = 4;
T=[1,2,4,8,3,6,12,11,5,10,7,14,15,13,9];
%数据生成与存储
% data = randi(2,m,1);
% data = data - 1;
% save data;
%数据导入
load data;
rs_data = data;
rs_data_word = reshape(rs_data,N/8,8);
original_data = zeros(1,N/8);
for i = 1:N/8
    word_str = num2str(rs_data_word(i,:));
    original_data(i) = bin2dec(word_str);
end
rs_data_a = reshape(original_data,N/k/8,k);
%rs编码

msg  = gf(rs_data_a,8);
RS_output = rsenc(msg,n,k);
rs_data_b = double(RS_output.x);
% save rs_data_b;


