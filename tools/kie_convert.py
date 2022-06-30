import json

if __name__ == '__main__':
    file = r'../cust-config/idcard/idcard_classes.txt'
    base_path = r'E:\opt\ocr-axatp\idcard-6-23\picture'
    label_file = fr'{base_path}\Label.txt'
    temp_file = rf'{base_path}\temp.txt'
    keys = {}
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            keys[line.split(' ')[1].rstrip('\n')] = line.split(' ')[0]
    with open(label_file, 'r', encoding='utf-8') as f:
        with open(temp_file, 'w', encoding='utf-8') as tmp:
            lines = f.readlines()
            for line in lines:
                line = line.rstrip('\n')
                file, labels = line.split('\t')[0], json.loads(line.split('\t')[1])
                for label in labels:
                    key_cls = label['key_cls']
                    label['label'] = int(keys[key_cls])
                    label.pop('key_cls')
                tmp.write(file + '\t' + json.dumps(labels, ensure_ascii=False) + '\n')
