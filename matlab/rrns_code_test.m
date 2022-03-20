clear;clc;
%主要参数
n = 14; k = 10;
N = 1024*1024*k;
modulus = [3 5 7 11 13 17 19 23 29 31 37 41 43 47];
%数据导入
load data;
rrns_data = data';
%数据转化
rrns_data_word = reshape(rrns_data,N/8,8);
original_data = zeros(1,N/8);
for i = 1:N/8
    word_str = num2str(rrns_data_word(i,:));
    original_data(i) = bin2dec(word_str);
end
%取模
rrns_data_b =  zeros(N/8,n);
for i = 1:N/8
    for j = 1:n
        rrns_data_b(i,j) = mod(original_data(i),modulus(j));
    end
end


