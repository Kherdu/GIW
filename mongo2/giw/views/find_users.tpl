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
        <th>Password hash</th>
        <th>Gender</th>
        <th>Country</th>
		<th>ZIP</th>
		<th>Year</th>
		<th>Likes</th>
    </tr>
</thead>
% for user in data["users"]:
   
    <tr>
        <td><strong>{{user["_id"]}}</strong></td>
        <td>{{user["email"]}}</td>
        <td>{{user["password"]}}</td>
		<td>{{user["gender"]}}</td>
		<td>{{user["address"]["country"]}}</td>
		<td>{{user["address"]["zip"]}}</td>
		<td>{{user["year"]}}</td>
		<td>
		%for like in user["likes"]:
			{{like}} <br>
		%end
		</td>
    </tr> 

% end
% end

%include('footer.tpl')