
% include('header.tpl', **data)

<table class="table table-hover">
    <thead>
        <tr>
            % for key in data["reqData"][0]:
                <th>{{key.capitalize()}}</th>
            % end
        </tr>
    </thead>
    % for row in data["reqData"]:
        <tr>
            % for key in row:
            <td>{{row[key]}}</td>
            % end
        </tr> 
    % end
</table>
<p><a href="/buscar">Volver a buscar</a></p>
% include('footer.tpl')
