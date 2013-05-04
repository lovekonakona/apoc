{% extends "layout.tpl" %}

{% block content %}

<div class="container">
    <form action="" method="post">
        <fieldset>
            <legend>Sign In</legend>

            <label for="nickname">Nickname</label>
            <input type="text" id="nickname" name="nickname">

            <label for="email">Email</label>
            <input type="text" id="email" name="email">

            <label for="password">password</label>
            <input type="password" id="password" name="password">

            <label for="confirm-password">Confirm Password</label>
            <input type="password" id="confirm-password" name="confirmPassword">

            <div class="clear-fix"></div>

            <button type="submit" class="btn">Submit</button>
        </fieldset>
    </form>
</div>

{% end %}
