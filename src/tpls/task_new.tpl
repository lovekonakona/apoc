{% extends "layout.tpl" %}

{% block content %}
<div class="container">
    <form action="" method="post">
        <fieldset>
            <legend>New Task</legend>
            
            <label for="title">Title</label>
            <input type="text" id="title" name="title" class="input-xxlarge">

            <label for="description">Description</label>
            <textarea name="description" id="description" cols="" rows="6" class="input-xxlarge"></textarea>

            <label for="">Estimated hour</label>
            <div class="inline-wrapper">
                <label class="radio inline">
                    <input type="radio" id="" name="estimated_hour" value="0" checked="checked"> 0
                </label>

                <label class="radio inline">
                    <input type="radio" id="" name="estimated_hour" value="0.5"> 0.5
                </label>

                <label class="radio inline">
                    <input type="radio" id="" name="estimated_hour" value="1.0"> 1.0
                </label>

                <label class="radio inline">
                    <input type="radio" id="" name="estimated_hour" value="2.0"> 2.0
                </label>

                <label class="radio inline">
                    <input type="radio" id="" name="estimated_hour" value="4.0"> 4.0
                </label>

                <label class="radio inline">
                    <input type="radio" id="" name="estimated_hour" value="6.0"> 6.0
                </label>

                <label class="radio inline">
                    <input type="radio" id="" name="estimated_hour" value="8.0"> 8.0
                </label>
            </div>

            {% if users and len(users) > 0 %}
            <div class="clear-fix"></div>
            <label for="">Assign to</label>
            <div class="inline-wrapper">
                {% for u in users %}
                
                <label class="checkbox inline">
                    <input type="checkbox" id="" name="assign_to_{{u.id}}" value="{{u.id}}"> {{u.nickname}}
                </label>
                {% end %}
            </div>
            {% end %}
            
            <div class="clear-fix"></div>
            
            <button type="submit" class="btn">Submit</button>
        </fieldset>
    </form>
</div>
{% end %}
