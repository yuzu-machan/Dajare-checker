# Dajare-checker
ダジャレの判定を行うだけのプログラムです。  
正確には文字の繰り返しを判定するプログラムです。  
実行にはpykakasi 2.0以降が必要です。  
APIもあるよ! 
## pythonでの使い方
dajare.pyのjudgment関数を呼び出すだけ。  
それ以外のファイルは必要なし。  
### judgement関数
第一引数に判定したいテキストを、第二引数に分割する文字数をとります。  
テキストはひらがなに自動的に変換されます。  
テキストは記号などを変換してから判定しています。
戻り値は辞書型で、`result`キーに0が入っていたらダジャレではなく、1が入っていたらダジャレという判定です。  
例1:  
`judgement("アルミ缶の上にあるミカン",5)`を呼び出す  
->あるみかんのうえにあるみかん  
->あるみかん,るみかんの,みかんのう,かんのうえ,んのうえに,のうえにあ,うえにある,えにあるみ,にあるみか,あるみかん  
->あるみかんが一致  
->`{"result":1}`を返す  
例2:  
`judgement("ふとんが吹っ飛んだ",4)`を呼び出す  
->ふとんがふとんだ  
->ふとんが,とんがふ,んがふと,がふとん,ふとんだ  
->一致なし  
->`{"result":0}`を返す  
となっています。  
この関数は将来的にresultに-1,errornoに数値が返される可能性があります。
この場合内部エラーですので、対策をお願いします。
## WebAPIでの使い方
`https://dajare-1-b7169515.deta.app/judge?text=[判定したい文字列]&length=[分割する文字数]`でGETしてください。  
JSONを返し、`result`キーに0が入っていたらダジャレではなく、1が入っていたらダジャレという判定です。   
__このAPIは[Deta](Deta.space)で活動させています。いくら使っても無料なので気にせず使ってください。__
