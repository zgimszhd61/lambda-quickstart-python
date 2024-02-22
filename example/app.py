import requests

def lambda_handler(event, context):
    # 获取API Gateway传递的查询参数
    query_parameters = event.get('queryStringParameters', {})
    name = query_parameters.get('name', 'World')  # 获取用户输入的名称（如果提供）

    url = "https://linchat.xyz/"
    try:
        response = requests.get(url)  # 尝试请求URL
    except:
        return {
            'statusCode': 200,
            'body': f'Hello, ERROR!'  # 如果请求失败，返回错误信息
        }

    return {
        'statusCode': 200,
        'body': f'Hello, {name}!'  # 如果请求成功，返回问候语
    }
