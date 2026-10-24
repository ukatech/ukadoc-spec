# SHIORI Resource

SHIORI Resourceは、旧プロトコル[SHIORI/2.5](http://usada.sakura.vg/contents/shiori.html#shiori25)において、オーナードローメニューの表示やhomeurlなどの*単純な文字列情報を取得するためのリクエスト*として定義されたものが元になっています。<br />
この仕様によって、そうした情報をゴースト側の状態に応じて制御することができます。

SHIORI/3.0以降では、旧仕様の整理の結果通常のSHIORI Eventと実装上明確には区別されていません。

通常のSHIORI Eventと異なる特徴として、戻り値はさくらスクリプトでなく単なる（短い）テキスト（bool値様の物含む）として扱われることが挙げられます。またリクエストIDは「On」から始まらず、英字は小文字で表記されます。
