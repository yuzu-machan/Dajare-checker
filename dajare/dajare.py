import pykakasi
def judgment(text="",length=0):
    kks= pykakasi.kakasi()
    rule={'。':None,'、':None,',':None,'.':None,'!':None,'！':None,'「':None,'」':None,'『':None,'』':None,' ':None,'　':None,'っ':None,'ゃ':'や','ゅ':'ゆ','ょ':'よ','ぁ':'あ','ぃ':'い','ぅ':'う','ぇ':'え','ぉ':'お','ー':None,}
    textlist=[]
    for i in kks.convert(text):
        textlist.append(i['hira'])
    text=''.join(textlist)
    text=text.translate(str.maketrans(rule))
    target=[]
    for i in range(len(text)-length+1):
        target.append(text[i:i+length])
    a=len(target)
    b=len(list(set(target)))
    if a==b:
        return {"result":0}
    else:
        return {"result":1}