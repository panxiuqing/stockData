% 从Sina获取上市公司分红数据

% 获取浙江龙盛的分红数据举例
fin_url = 'http://vip.stock.finance.sina.com.cn/corp/go.php/vISSUE_ShareBonus/stockid/600352.phtml'

str = urlread(fin_url);
tb_str = regexp(str, '<tbody>.+?</tbody>', 'match');
Data = regexp(tb_str{1}, '(?<=<td>).+?(?=</td>)', 'match');
D = reshape(Data, 9, length(Data)/9)';