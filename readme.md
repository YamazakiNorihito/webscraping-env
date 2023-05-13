

### 環境構築

 - ptenv install(win)
   - https://github.com/pyenv-win/pyenv-win#quick-start


- エラー出たときの対応
  - 現在のシステムで実行できないスクリプトが検出されたことを示しています。具体的には、C:\WINDOWS\system32\install-pyenv-win.ps1というファイルがデジタル署名されていないため、実行できないというエラー
    - （対処）以下で実行ポリシーが変更され、署名されていないスクリプトが実行できるようになるはずです。ただし、セキュリティ上の理由から、注意して署名されていないスクリプトを実行してください。必要な作業が完了したら、実行ポリシーを再び元の値に戻すことをお勧めします。
        1. PowerShellを管理者として実行します。
        2. 実行ポリシーを表示するために、次のコマンドを入力します。
           ```bash
                Get-ExecutionPolicy
           ``` 
        3. 出力された実行ポリシーの値をメモします。
        4. 実行ポリシーを変更するために、次のコマンドを入力します。
           ```bash
                Set-ExecutionPolicy RemoteSigned
           ``` 
        5. 「実行ポリシーの変更」という確認メッセージが表示された場合は、[Y]キーを押して確認します。

### Python 実行Version
    - 3.9.0

    ```bash
        pyenv install 3.9.0
        pyenv global  3.9.0
        pyenv version
    ``` 

### VSCode 拡張機能
    - [ms-python.python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
      - Microsoftが提供する公式のPython拡張機能です。コードのシンタックスハイライトや自動補完、デバッグのサポートなど、Python開発に必要な基本的な機能を提供します。
    - [ms-python.vscode-pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
      - Microsoftが開発した高性能なPython向け補完エンジンです。型ヒントのサポートやコードの自動補完、型の検査など、より高度な開発支援を提供します。
    - [ms-pyright.pyright](https://marketplace.visualstudio.com/items?itemName=ms-pyright.pyright)
      - Microsoftが提供する静的型チェッカーです。Pythonのコードを解析し、潜在的なエラーや型の不一致を検出してくれます。型ヒントを活用してコードの品質を向上させるのに役立ちます。
    - [njpwerner.autodocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)
      - コードのドキュメンテーションをサポートする拡張機能です。関数やクラスのドキュメンテーション文字列を自動生成してくれます。


### Python実行方法
    実行
    1. test.py
       ```python
            print("Hello, World!")
       ```
    2. Python: Run Python File in Terminal」を選択


    デバッグ実行
    1. test.py
       ```python
            print("Hello, World!")
       ```
    2. Ctrl + Shift + D
       1. launch.jsonのPythonを作成（Pythonを選択するだけで行けるはず
    3. ブレークポイントを設定
    4. デバッグを開始します。
       1. ショートカットキーF5
          - ステップイン（F11）
          - ステップオーバー（F10）
          - ステップアウト（Shift + F11）


### 仮想環境

プロジェクトごとに異なるPythonバージョンやパッケージのバージョンを管理
```powershell
# 使用したいPythonバージョンを指定して、新しい仮想環境を作成します。以下のコマンドを実行します:
python -m venv webscraping-env

# 仮想環境を有効化します。
.\webscraping-env\Scripts\Activate.ps1

# 仮想環境一覧
pyenv virtualenvs
```
VSCodeでデバッグ実行する場合は、右下でPythonの実行環境をwebscraping-envに選択する



### パッケージをインストール
パッケージのInstall方法

```bash
.\webscraping-env\Scripts\Activate.ps1
pip install <package_name>
```