# 网页公式提取器

## 页面展示

![1.png](https://s2.loli.net/2025/01/20/fDcZERBNCKAd7nO.png)



## 支持

支持从文件导入和从网页ctrl+v粘贴

# 1前端

## 1.1如何建立自己的前端页面



### 1.1.1创建Vite3项目

在你文件夹目录下使用下面的指令

```markdown
npm init vite
```

在project name 选项中输入自己的项目名字（这里假设项目名字是 vite-project ）

![image.png](https://cdn.nlark.com/yuque/0/2024/png/36042868/1735182833249-800e70a8-f836-4645-974e-a7045e1d6b17.png?x-oss-process=image%2Fformat%2Cwebp%2Fresize%2Cw_750%2Climit_0)

出现该图的时候选择vue,然后选择javascript。

### 1.1.2安装依赖

命令行中输入cd vite-project 进入项目

依赖安装

npm install 或者 cnpm i

npm：nodejs 默认的包管理工具，安装、卸载、管理依赖（国外下载，可能有网络问题）

cnmp：淘宝镜像

yarn：推出的包管理工具，取代npm,比npm块，是对于npm的新设计

![img](https://cdn.nlark.com/yuque/0/2024/png/36042868/1735183759630-6d41154a-df17-4e90-9193-84d34913a591.png)

### 1.1.3.运行vite项目

命令行输入npm run dev 或者 yarn dev

## 2.1替换

将我的文件换到你的初始化文件中。然后运行yarn dev就成功运行前端了

# 2.后端

## 2.1.配置接口

![image-20250120015154703.png](https://s2.loli.net/2025/01/20/Beao8GQsdNYDint.png)

#### 2.1.1获取 API（必需）



本软件调用了 `讯飞` 的 API（后续有望增加更多源，以提高准确率），目前的免费额度为 500次 / 天，可以满足个人用户的使用需求。

在进行识别前，**需要先自行申请 API 额度**，然后在软件的 **设置** 页面，填写获得的 API。

API 的获取方法如下：

1. 进入[讯飞开放平台注册页面](https://passport.xfyun.cn/register)，注册一个新的账号；

2. 进入[公式识别业务页面](https://www.xfyun.cn/service/formula-discern)，可以在首页顶栏的 “产品服务 - 文字识别 - 公式识别” 中找到；

   ![1_mainpage.png](https://camo.githubusercontent.com/dafd21af815f529e96f38a23592a94c522d88bba74b3bf55708f221d91d96efd/68747470733a2f2f73322e6c6f6c692e6e65742f323032312f31322f32312f64436851624535444c54724777496a2e706e67)

3. 点击 **“服务管理”**，会提示创建一个应用（如果之前没有账号的话），界面如下图所示。

   依次填写 “应用名称”、“应用分类” 与 “应用功能描述” 项，可以按自己喜好任意填写。

   ![2_CreateAPP.png](https://camo.githubusercontent.com/49ccb42f3c577edcc6b558cc8bea07f8ec9a376378429f4912e07f56c5756587/68747470733a2f2f73322e6c6f6c692e6e65742f323032312f31322f32312f49453567664753726f51566a4c6c612e706e67)

4. 点击 **“提交”** ，即可进入服务管理页面，如下图所示。

   右侧的 **APPID** 、 **APISecret** 、 **APIKey** 三项，即是我们需要的 API 值。

   ![3_APIInfo_B.png](https://camo.githubusercontent.com/88fe741f8fb0a9acadb39eea364cca8a8742cad5d9fa93aaa2c0a8d6800f5940/68747470733a2f2f73322e6c6f6c692e6e65742f323032312f31322f32322f5663366a4c39644851724f454b67582e706e67)

#### 2.1.2 将获取的 API 填入软件



- 进入软件，点击 `设置` 页面，可以看到如下图所示的界面。
- 将获取到的 **APPID** 、 **APISecret** 、 **APIKey** 三项，分别填入对应的位置，然后点击 `确定` 。

至此，软件已经配置成功！可以选择需要的公式，进行识别了！

## 2.2运行

![image-20250120015539414.png](https://s2.loli.net/2025/01/20/BCNnzUTh97AV4aJ.png)

pycharm 打开之后终端输入python app.py就能用

# 3.注意事项

## 3.1 端口占用问题

如何显示没有返回的话，注意检测是不是key-id Api上限到了或者端口的问题，flask5000端口已经被使用了。

## 3.2识别失败

公式没有提取到的话可以多加点白边进去，即是公式内容在图片正中，周围一圈白。

## 3.3 服务器部署问题

后端有一句：rewrite: (path) => path.replace(/^\/api/, ''), // 可选：去掉 /api 前缀。

但是实际上如果前端部署在服务器上，它还是访问的/api/upload_image。

```
# @app.route('/upload_image/', methods=['POST'])
@app.route('/api/upload_image/', methods=['POST'])
```

前端部署在宝塔服务器上将路由设置设置为/api/upload_image/。

但是如果前端还是在本地，就设置为/upload_image/

# 4.借鉴

[QingchenWait/QC-Formula: 轻量级公式 OCR 小工具：一键识别各类公式图片，并转换为 LaTeX 格式。](https://github.com/QingchenWait/QC-Formula)

# 5.参与贡献

这个软件的界面和功能还非常原始，随时欢迎大家对它进行后续的开发。

1. Fork 本仓库
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request

目前的问题在于这个api不是特别准确，又更好的api或者一些视觉算法都可以和我交流，作者本人可以加上去。

也欢迎大家加我Q：3269327552与我交流。
