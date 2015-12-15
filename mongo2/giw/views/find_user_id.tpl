
% include('header.tpl', data = data)

%if len(data["users"]) > 0:
<ul>
	<li><strong>Id:</strong> {{data["users"][0]["_id"]}}</li>
	<li><strong>Address:</strong></li>
	<ul>
		<li><strong>Country:</strong> {{data["users"][0]["address"]["country"]}}</li>
		<li><strong>Zip:</strong> {{data["users"][0]["address"]["zip"]}}</li>
	</ul>
	<li><strong>Email:</strong> {{data["users"][0]["email"]}}</li>
	<li><strong>Gender:</strong> {{data["users"][0]["gender"]}}</li>
	<li><strong>Likes:</strong></li>
	<ul>
		%if len(data["users"][0]["likes"]) > 0:
			%for like in data["users"][0]["likes"]:
			<li>{{like}}</li>
			%end
		%else:
			<li>This user has no likes</li>
		%end
	</ul>
	<li><strong>Password:</strong> {{data["users"][0]["password"]}}</li>
	<li><strong>Year:</strong> {{data["users"][0]["year"]}}</li>
</ul>
%else:
<div class="alert alert-danger" role="alert">
	Usuario no encontrado en la base de datos.
</div> 	
%end

% include('footer.tpl')
