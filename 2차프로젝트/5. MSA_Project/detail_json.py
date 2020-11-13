# 카테고리, 모델명, 모델코드, 모델 이미지, 퀵 가이드, 매뉴얼

# 테이블에 있는 제품 코드를 가지고 온다
# 해당 제품 코드에 대한 product이 있는 테이블의 속성들을 가져온다
# 이걸 제이슨 파일 형태로? 아님 제이슨으로?

import boto3
import json
from boto3.dynamodb.conditions import Key, Attr


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('product_table')

response = table.query(
    KeyConditionExpression=Key('product_code').eq('CLP-415N')
)
items = response['Items']
# print(items)

print(json.dumps(items, ensure_ascii=False, indent="\t"))

