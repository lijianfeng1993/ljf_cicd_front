 <html>
    <head>
    <title>获取任务构建日志</title>
    </head>
    <body>
        <p><h2>获取任务构建日志</h2><input type="button" value="返回主页" onclick="location.href='http://10.132.47.15:4502/home'"></p>
        <form action="/do_getconsole" method="post">
            Jobname: <input name="jobname" type="text" />
            <input value="获取构建日志" type="submit" />
        </form>
        <p>
            <h4>当前的所有任务
        </p>
        <p>
            <h6>
            %for jobname in talljobnames:
            	{{jobname}}<br />
            %end
        </p>
        
    </body>
</html>