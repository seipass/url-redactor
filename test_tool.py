import json
from url_redactor import transform
def test_transform():
    value='https://user:pass@example.test/x'
    if True: result=transform(value)
    else: result=transform(json.loads(value))
    assert 'example.test' in json.dumps(result,ensure_ascii=False)
