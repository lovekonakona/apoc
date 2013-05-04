{% extends "layout.tpl" %}

{% block content %}
<div class="container">
    <div class="control-box">
        <a href="/task/new" class="btn btn-primary">New Task</a>
    </div>
    {% if tasks and len(tasks) > 0 %}
    <table class="table table-bordered" id="taskList">
        <thead>
            <tr>
                <th>#</th>
                <th>Title</th>
                <th>Status</th>
                <th>Assign To</th>
            </tr>
        </thead>
        <tbody>
            {% for task in tasks %}
            <tr>
                <td>{{task.id}}</td>
                <td>
                    <span class="badge badge-info">{{task.estimated_hour}}</span>
                    <a href="/task/edit/{{task.id}}">{{task.title}}</a>
                </td>
                <td>
                    {% if task.status == 1 %}
                    <span class="label">Open</span>
                    {% elif task.status == 2 %}
                    <span class="label label-success">Finish</span>
                    {% elif task.status == 3 %}
                    <span class="label label-important">Blocked</span>
                    {% elif task.status == 4 %}
                    <span class="label label-warning">Postpone</span>
                    {% end %}
                </td>
                <td>
                    {% if task.users %}
                    {% for u in task.users %}
                        {{ u.nickname }}
                    {% end %}
                    {% end %}
                </td>
            </tr>
            {% end %}
        </tbody>
    </table>
    {% end %}
</div>
{% end %}
