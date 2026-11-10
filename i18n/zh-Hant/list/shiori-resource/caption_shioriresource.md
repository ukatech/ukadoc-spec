# SHIORI Resource

SHIORI Resource源自舊版協定[SHIORI/2.5](http://usada.sakura.vg/contents/shiori.html#shiori25)中的定義：它是一種*用來取得簡單字串資訊的請求*，例如顯示 owner draw 選單或取得homeurl。<br />
透過此規格，可以依照 ghost 的狀態控制這些資訊。

SHIORI/3.0以後，經整理舊規格後，在實作上已不再與一般的SHIORI Event明確區分。

與一般SHIORI Event不同之處在於，回傳值不是Sakura Script，而是以單純的（短）文字（也包含類似bool值的內容）處理。此外，請求ID不以「On」開頭，英文字母以小寫表示。
