# HttpRunner3
An automatic framework of API Test（接口自动化测试框架）.采用yaml格式文件编写测试用例，执行make模块转换为pytest测试.py模块文件，
执行pytest后生成Allure报告结果文件，最后采用Allure展示报告并跟踪质量。

基于Pytest、requests、HttpRunner3_Maker、Yaml、Allure、Jenkins(CI)、Toml等第三方组件及中间件打造，具有高效、简单易用、高质量等特点。 

## 套件说明
由两部分组成：自动测试框架 和 应用案例。

### 自动测试框架
框架解决案例数据转换及其自动持续集成等实现，详见知识库： [httprunner3-framework](https://www.github.com/ruudzhao/httprunner3-framework "Framework")

### 应用案例
包括基本的例子，也包括互联网、金融等行业的综合案例，案例持续更新中，详见知识库：[httprunner3-cases](https://www.github.com/ruudzhao/httprunner3-cases "Cases")

## Slogan
一天的工作一小时搞定

An hour Done a day's work.
