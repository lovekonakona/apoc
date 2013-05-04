{% extends "layout.tpl" %}

{% block content %}
<div class="container">
    <form action="" method="post">
        <fieldset>
            <legend>Edit Task</legend>

            <label for="title">Title</label>
            <input type="text" id="title" name="title" class="input-xxlarge" value="{{ task.title }}">
            
            <label for="description">Description</label>
            <textarea name="description" id="description" cols="" rows="6" class="input-xxlarge">{{ task.description }}</textarea>

            <label for="">Estimated hour</label>
            <div class="inline-wrapper">
                <label class="radio inline">
                    <input type="radio" id="" name="estimated_hour" value="0"{% if task.estimated_hour == 0 %} checked="checked"{% end %}> 0
                </label>

                <label class="radio inline">
                    <input type="radio" id="" name="estimated_hour" value="0.5"{% if task.estimated_hour == 0.5 %} checked="checked"{% end %}> 0.5
                </label>

                <label class="radio inline">
                    <input type="radio" id="" name="estimated_hour" value="1.0"{% if task.estimated_hour == 1.0 %} checked="checked"{% end %}> 1.0
                </label>

                <label class="radio inline">
                    <input type="radio" id="" name="estimated_hour" value="2.0"{% if task.estimated_hour == 2.0 %} checked="checked"{% end %}> 2.0
                </label>

                <label class="radio inline">
                    <input type="radio" id="" name="estimated_hour" value="4.0"{% if task.estimated_hour == 4.0 %} checked="checked"{% end %}> 4.0
                </label>

                <label class="radio inline">
                    <input type="radio" id="" name="estimated_hour" value="6.0"{% if task.estimated_hour == 6.0 %} checked="checked"{% end %}> 6.0
                </label>

                <label class="radio inline">
                    <input type="radio" id="" name="estimated_hour" value="8.0"{% if task.estimated_hour == 8.0 %} checked="checked"{% end %}> 8.0
                </label>
            </div>

            {% if users and len(users) > 0 %}
            <div class="clear-fix"></div>
            <label for="">Assign to</label>
            <div class="inline-wrapper">
                {% for u in users %}
                <label class="checkbox inline">
                    <input type="checkbox" id="" name="assign_to_{{u.id}}" value="{{u.id}}"{% if u.id in assign_ids %} checked="checked"{% end %}> {{u.nickname}}
                </label>
                {% end %}
            </div>
            {% end %}

            <label for="">Status</label>
            <div class="inline-wrapper">
                <label class="radio inline">
                    <input type="radio" id="" name="status" value="1"{% if task.status == 1 %} checked="checked"{% end %}>
                    open
                </label>
                <label class="radio inline">
                    <input type="radio" id="" name="status" value="2"{% if task.status == 2 %} checked="checked"{% end %}>
                    finish
                </label>
                <label class="radio inline">
                    <input type="radio" id="" name="status" value="3"{% if task.status == 3 %} checked="checked"{% end %}>
                    blocked
                </label>
                <label class="radio inline">
                    <input type="radio" id="" name="status" value="4"{% if task.status == 4 %} checked="checked"{% end %}>
                    postpone
                </label>
            </div>
            
            <div class="clear-fix"></div>
            
            <button type="submit" class="btn">Submit</button>
        
        </fieldset>
    </form>
    
</div>
{% end %}
