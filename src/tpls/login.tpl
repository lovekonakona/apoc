{% extends "layout.tpl" %}

{% block content %}
<div class="container">
    <form action="" method="post">
        <fieldset>
            <legend>Login</legend>

            <label for="email">Email</label>
            <input type="text" id="email" name="email">

            <label for="password">password</label>
            <input type="password" id="password" name="password">

            <label class="checkbox">
                <input type="checkbox" name="rememberMe"> Remember me
            </label>

            <button type="submit" class="btn">Submit</button>
        </fieldset>
    </form>
</div>
{% end %}
