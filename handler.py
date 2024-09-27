import json


def hello(event, context):
    body = {
        "message": "Go Serverless v4.0! Your function executed successfully!",
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def tree(event, context):
    floors = 20
    if floors <= 2:
        return {"statusCode": 400, "body": json.dumps({"message": "Error: Number of floors must be greater than 2"})}
    
    if floors > 100:
        return {"statusCode": 400, "body": json.dumps({"message": "Error: Number of floors must be less than 100"})}
    
    tree = []
    width = floors * 2 - 1

    star = ' ' * (floors - 1) + '✯' + ' ' * (floors - 1)
    tree.append(star)

    for i in range(floors):
        level = ' ' * (floors - i - 1) + '*' * (2 * i + 1) + ' ' * (floors - i - 1)
        tree.append(level)
        
    base_width = 1 if floors <= 3 else 3 if floors <= 10 else 5 if floors <= 50 else 11
    base = ' ' * (floors - base_width // 2 - 1) + '*' * base_width + ' ' * (floors - base_width // 2 - 1)
    for _ in range(base_width):
        tree.append(base)

    tree_str = "\n".join(tree)
    print(tree_str)  
    return {"statusCode": 200, "body": json.dumps({"message": "Tree printed"})}