clear;clc;
%% 单节点修复
%主要参数
n = 14; k = 10;
N = 1024*1024*k;
modulus = [257 263 269 271 277 281 283 293 307 311 313 317 331 337];
modulus_1 = [257 263 269 271 277 281 283 293 307 311];
modulus_2 = [293 307 311 313 317 331 337];

%数据导入
load rrns_data_b;
R = rrns_data_b(:,1:10);
%节点修复
X_e = zeros(1,N/80);

for i = 1:N/80
    X_e(1,i) = CRT(R(i,:),modulus_1);
end


%% 多节点修复
%主要参数
% n = 14; k = 10;
% N = 1024*1024*k;
% modulus = [257 263 269 271 277 281 283 293 307 311 313 317 331 337];
% 
% %数据导入
% load rrns_data_b;
% R = rrns_data_b;
% %节点修复
% X_e = zeros(1,N/80);
% for j=1:100
%     for i = 1:N/80
%         X_e(1,i) = CRT(R(i,:),modulus);
%     end
% end

