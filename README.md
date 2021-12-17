# memorandum
ためになったけど、今後使うかわからないコードとかをまとめておく
## RemoveDuplicates.py  
listの要素がdict型のデータで構成されてるときに、setを使って全く同じ要素を取り除く方法。  
例 list1=[{"id":1,"price":200},{"id":2,"price":400}],list2=[{"id":1,"price":200},{"id":2,"price":300}]  
   print(RemoveDuplicates(list1,list2))  
   実行結果　[{"id":1,"price":400}]
