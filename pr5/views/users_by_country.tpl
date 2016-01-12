%include('header.tpl', **data)

<div class="alert alert-info" role="alert">
	<strong>Data found:</strong> {{len(data["data"])}}
</div>

<table class="table table-striped">
<thead>
    <tr>
        <th>Country</th>
        <th>Num</th>
    </tr>
</thead>
% for country in data["data"]:
   
    <tr>
        <td><strong>{{country["country"]}}</strong></td>
        <td>{{country["count"]}}</td>
    </tr> 

% end

%include('footer.tpl')