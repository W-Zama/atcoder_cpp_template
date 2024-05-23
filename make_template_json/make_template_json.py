import json

with open('./input.cpp', 'r') as file:
    with open('output.json', 'w') as output:
        for line in file:
            # 改行文字を削除
            clean_line = line.rstrip()
            # もし，jsonにおける特殊文字が含まれていたらエスケープする
            json_line = json.dumps(clean_line)
            # 引用符で囲み、行の最後にカンマを付ける
            formatted_line = f'{json_line},\n'
            # 処理した行を出力ファイルに書き込む
            output.write(formatted_line)

print('Done!')
