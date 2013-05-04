<!DOCTYPE HTML>
<html lang="en-US">
    <head>
        <meta charset="UTF-8">
        <title>Apoc</title>
        <link rel="shortcut icon" href="/static/favicon.ico" />
        <link rel="stylesheet" type="text/css" href="/static/bootstrap/css/bootstrap.min.css">
        <link rel="stylesheet" type="text/css" href="/static/main/css/main.css">
        <script src="/static/main/js/jquery-1.9.1.min.js"></script>
        <script src="/static/bootstrap/js/bootstrap.min.js"></script>
    </head>
    <body>
        <div class="navbar navbar-inverse">
            <div class="navbar-inner">
                <div class="container">
                    <a class="btn btn-navbar" data-toggle="collapse" data-target=".navbar-inverse-collapse">
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </a>
                    <a class="brand" href="/">Apoc</a>
                    <div class="nav-collapse collapse navbar-inverse-collapse">
                        <ul class="nav">
                            <li><a href="/task">Task</a></li>
                        </ul>
                        <ul class="nav pull-right">
                            {% if user %}
                            <li class="dropdown">
                                <a href="#" class="dropdown-toggle" data-toggle="dropdown">{{user.nickname}}<b class="caret"></b></a>
                                
                                <ul class="dropdown-menu">
                                    <li><a href="/logout">logout</a></li>
                                </ul>
                            </li>
                            {% else %}
                            
                            {% if False %}
                            <li>
                                <a href="/signup">SignUp</a>
                            </li>
                            {% end %}
                            <li>
                                <a href="/login">Login</a>
                            </li>
                            {% end %}
                            
                        </ul>
                    </div><!-- /.nav-collapse -->
                </div>
            </div>
        </div>
        {% block content %}
        {% end %}
    </body>
</html>
