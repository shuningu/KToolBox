<p style="text-decoration:none">
  <img src="https://cdn.jsdelivr.net/gh/Ljzd-PRO/KToolBox@latest/static/repository-open-graph-2.svg" alt="logo">
</p>

<h1 style="text-align: center">
  KToolBox
</h1>

<p style="text-align: center">
  KToolBox 是一个用于下载
  <a href="https://kemono.su/">Kemono.party / Kemono.su</a>
  中作品内容的实用命令行工具
</p>

<p style="text-align: center">
  <a href="https://pypi.org/project/ktoolbox" target="_blank">
    <img src="https://img.shields.io/github/v/release/Ljzd-PRO/KToolBox?logo=python" alt="Version">
  </a>

  <a href="./LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-blue" alt="MIT"/>
  </a>

  <a href="https://github.com/Ljzd-PRO/KToolBox/activity">
    <img src="https://img.shields.io/github/last-commit/Ljzd-PRO/KToolBox/devel" alt="Last Commit"/>
  </a>

  <a href="https://codecov.io/gh/Ljzd-PRO/KToolBox" target="_blank">
      <img src="https://codecov.io/gh/Ljzd-PRO/KToolBox/branch/master/graph/badge.svg?token=5XK9CYQHQN" alt="codecov"/>
  </a>

  <a href='https://ktoolbox.readthedocs.io/'>
    <img src='https://readthedocs.org/projects/ktoolbox/badge/?version=latest' alt='Documentation Status' />
  </a>

  <a style="text-decoration:none">
    <img src="https://img.shields.io/badge/Platform-Windows%20|%20Linux%20|%20macOS-blue" alt="Platform Win | Linux | macOS"/>
  </a>
</p>

<img src="https://cdn.jsdelivr.net/gh/Ljzd-PRO/KToolBox@latest/static/preview-1.png" alt="Preview">

## 功能

- 你可以下载 Kemono 上的作品的所有文件
- 或者下载某个作者 / 画师的所有作品
- **同步** 已下载完成的作者 / 画师目录至最新, 只有近期更新和新发布的作品会被下载
- 搜索作者和作品，并导出结果
- 并发下载
- 支持全平台

## 使用方法

### 安装

=== "一般情况"
    ```bash
    pip3 install ktoolbox
    ```

=== "对于 iOS a-Shell"
    ```bash
    pip3 install ktoolbox-pure-py
    ```
    !!! info "关于 a-Shell"
        [a-Shell](https://github.com/holzschu/a-shell) 是一个 iOS 终端 App，它只能运行纯 Python 脚本

### 命令

使用帮助命令或前往 [命令](./commands.md) 页面查看更多帮助。
  
#### ❓ 获取帮助总览
```bash
ktoolbox -h
```
  
#### ❓ 获取某个命令的帮助信息
```bash
ktoolbox download-post -h
```

#### ⬇️🖼️ 下载指定的作品
```bash
ktoolbox download-post https://kemono.su/fanbox/user/49494721/post/6608808
```
??? info "如果部分文件下载失败"
    如果部分文件下载失败，你可以尝试重新运行命令，已下载完成的文件会被 **跳过**。
  
#### ⬇️🖌️ 下载作者的所有作品
```bash
ktoolbox sync-creator https://kemono.su/fanbox/user/9016
```
??? info "输出"
    默认情况下你会在作者目录下得到一个 `creator-indices.ktoolbox` 文件，你可以用它来更新目录。
  

#### 🔄️ 更新一个作者目录
```bash
ktoolbox sync-creator https://kemono.su/fanbox/user/641955 --update-with=./xxx/creator-indices.ktoolbox
```
??? info "关于 `creator-indices.ktoolbox` 文件"
    `creator-indices.ktoolbox` 包含目录下的所有作品的信息和路径。