# Django with React 取り扱い書

## 起動方法
少々複雑だが、慣れてしまえば問題ない。
最終的に Python manage.py runserver を行う

React 部分を編集した場合、root で build
```bash
npm run build
```

build 後、withReact フォルダに移動して Django を起動する
```bash
python manage.py runserver
```

### 参考文献
* [環境構築](https://qiita.com/sand/items/15da91117c680a618c2b)
* [写真を撮って保存](https://blog.usize-tech.com/take-photo-by-react-app/)
