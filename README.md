# lambda-quickstart-python

AWS Lambda 本身是一个云服务，用于在无服务器环境中运行代码。虽然 Lambda 需要在 AWS 的云平台上运行，但你可以在本地开发和测试 Lambda 函数。AWS 提供了几种工具，如 AWS SAM (Serverless Application Model) 和 Docker，来帮助你在本地模拟 Lambda 环境。

下面是一个简单的例子，演示如何在本地开发一个使用 Python 编写的 Lambda 函数，该函数提供一个 Web API 接口，当用户访问时返回 "Hello World"。这个例子使用 AWS SAM。

### 步骤 1: 安装 AWS SAM CLI

首先，你需要在你的机器上安装 AWS SAM CLI。这个工具允许你本地构建、测试和调试 AWS Lambda 函数。你可以从 AWS 官方文档中找到安装指南：[AWS SAM CLI 安装指南](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)。

### 步骤 2: 初始化一个新的 SAM 应用

打开终端并运行以下命令以初始化一个新的 SAM 应用：

```bash
sam init
```

选择 "Quick Start Templates"，语言选择 "python3.8"，模板选择 "Hello World Example"。

### 步骤 3: 修改应用以创建一个 Web API

在生成的项目文件夹中，编辑 `app.py` 文件（位于 `hello_world` 文件夹中），修改 Lambda 函数以创建一个简单的 Web API。

```python
import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps('Hello World')
    }
```

### 步骤 4: 在本地运行 API

使用 SAM CLI 在本地启动 API。在项目的根目录下运行：

```bash
sam build
sam local start-api
```

这将启动一个本地服务器，通常是在 `http://127.0.0.1:3000/` 地址。

### 步骤 5: 访问你的 API

在浏览器或使用工具如 curl 访问 `http://127.0.0.1:3000/hello` 来看到返回的 "Hello World"。

### 步骤 6: 部署到 AWS Lambda

一旦你完成了本地测试，你可以使用以下命令将你的应用部署到 AWS Lambda：

```bash
sam deploy --guided
```

这将引导你通过配置并最终部署应用到 AWS Lambda。

以上步骤提供了一个基本的流程，你可以按照这个流程开发、测试和部署 Lambda 函数。对于更复杂的应用，你可能需要进一步探索 AWS SAM 的功能和选项。
