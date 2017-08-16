<html>
    <head>
    <title>任务创建</title>
    </head>
    <body>
        <p><h2>任务创建</h2><input type="button" value="返回主页" onclick="location.href='http://10.132.47.15:4502/home'"></p>
        <form action="/do_createjob" method="post">
            Jobname: <input name="jobname" type="text" />
            Language: <input name="language" type="text" />
            Url: <input name="url" type="text" />
            <input value="创建任务" type="submit" />
        </form>
    </body>
</html>