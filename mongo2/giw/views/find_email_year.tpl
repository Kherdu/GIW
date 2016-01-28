%include('header.tpl', **data)

% if data["err"] != '':
    <div class="alert alert-danger" role="alert">
        Ha indtroducido campos no válidos: {{data["err"]}}
    </div>
% else:
<div class="alert alert-info" role="alert">
	<strong>Users found:</strong> {{len(data["users"])}}
</div>

<table class="table table-striped">
<thead>
    <tr>
        <th>Id</th>
        <th>e-mail</th>
    </tr>
</thead>
% for user in data["users"]:
   <tr>
        <td><strong>{{user["_id"]}}</strong></td>
        <td>{{user["email"]}}</td>
    </tr> 

% end
% end

%include('footer.tpl')