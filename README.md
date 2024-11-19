# Stable-Diffusion-PromptXY-Plus

## 项目简介

Stable-Diffusion-PromptXY-Plus 是一个用于生成 excel 格式的的 XY 对比表格
## 功能特性

本项目可以读取两个 csv 文件中的提示词，并通过 stable diffusion webui 提供的 api 来生成 XY 对比表格

> 类似于 Stable Diffusion webui 自带的 XYZ 脚本，本项目可以视为 XYZ 脚本的 Plus 版


## 安装

请按照以下步骤安装本项目：

1. 克隆仓库：
    ```bash
    git clone https://github.com/yourusername/Stable-Diffusion-PromptXY-Plus.git
    ```
2. 进入项目目录：
    ```bash
    cd Stable-Diffusion-PromptXY-Plus
    ```
3. 安装依赖：
    ```bash
    pip install -r requirements.txt
    ```

## 使用方法

1. 修改 `config.py` 中的配置
3. 运行 `generate_images.py` 生成图片
4. 运行 `generate_excel.py` 生成 excel 文件

## 贡献

欢迎贡献代码！请提交 Pull Request 或报告问题。

## 许可证

本项目采用 MIT 许可证，详情请参阅 LICENSE 文件。
