<html>
    <head>
    <title>sonar静态扫描任务创建</title>
    </head>
    <body>
        <p><h2>sonar静态扫描任务创建</h2><input type="button" value="返回主页" onclick="location.href='http://10.132.47.15:4502/home'"></p>
        <form action="/do_create_sonarjob" method="post">
            Jobname: <input name="jobname" type="text" /><br />
            Language: <input name="language" type="text" /><br />
            Url: <input name="url" type="text" /><br />
            <input value="创建任务" type="submit" /><br />
        </form>
    </body>
</html>