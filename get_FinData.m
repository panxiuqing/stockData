% ��Sina��ȡ���й�˾�ֺ�����

% ��ȡ�㽭��ʢ�ķֺ����ݾ���
fin_url = 'http://vip.stock.finance.sina.com.cn/corp/go.php/vISSUE_ShareBonus/stockid/600352.phtml'

str = urlread(fin_url);
tb_str = regexp(str, '<tbody>.+?</tbody>', 'match');
Data = regexp(tb_str{1}, '(?<=<td>).+?(?=</td>)', 'match');
D = reshape(Data, 9, length(Data)/9)';