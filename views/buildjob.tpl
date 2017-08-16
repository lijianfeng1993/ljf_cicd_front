<html>
    <head>
    <title>任务创建</title>
    </head>
    <body>
        <p><h2>任务创建</h2><input type="button" value="返回主页" onclick="location.href='http://10.132.47.15:4502/home'"></p>
        <p>
            <h4>当前的所有任务
        </p>
        <p>
            <h6>
            %for jobname in talljobnames:
                {{jobname}}<br />
            %end
        </p>
        <form action="/do_buildjob" method="post">
            Jobname: <input name="jobname" type="text" />
            <input value="构建任务" type="submit" />
        </form>
    </body>
</html>