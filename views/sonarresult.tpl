<html>
    <head>
    <title>sonar扫描结果</title>
    </head>
    <body>
        <p><h2>sonar扫描结果</h2><input type="button" value="返回主页" onclick="location.href='http://10.132.47.15:4502/home'"></p>
        <p>
            {{tjobname}}项目sonar扫描结果：{{tresult}}
        </p>
        <p>
            <input type="button" value="查询详细信息" onclick="location.href='{{tresulturl}}'">
        </p>
    </body>
</html>