AutoXiaomi
==========

APIs for buying Xiaomi-Tw Product


How to use ?
------------

1)

  edit the buy.config
  
  write your info in it
  
  other info :
  
        3387-台北市
        3388-基隆市
        3389-宜蘭縣
        3390-桃園縣
        3391-新北市
        3392-新竹市
        3393-新竹縣
        3394-苗栗縣
        3395-台中市
        3396-彰化縣
        3397-南投縣
        3398-嘉義市
        3399-嘉義縣
        3400-雲林縣
        3401-台南市
        3402-高雄市
        3405-屏東縣
        3406-台東縣
        3407-花蓮縣
        3775-台中縣
        3776-台南縣
        3777-高雄縣  
  
2)
  Python Code :
  
  
      import module_xiaomi
      
      xiaomi = module_xiaomi.Xiaomi()
      xiaomi.login( account , password )
      
      
      xiaomi.buy_method1( itemid )
      
    
      
      

P.S
-------
  
  buy_method1 function can only apply on the order without captcha.
  
  itemid can be found at Xiaomi's website.
      
      
