from easyocr import Reader

reader = Reader(['en'], gpu=False)
result = reader.readtext(r"ingestion_service\data\tweet_images\tweet_0.png")
for res in result:
    coord = res[0]
    text = res[1]
    conf = res[2]
    # print(text)
    print(coord)
    # print(conf)