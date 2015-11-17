
%include('header.tpl', **data)

<table class="table table-hover">
<thead>
    <tr>
        <th>Id</th>
        <th>Juego</th>
        <th>Fecha inicio</th>
        <th>Fecha fin</th>
        <th>Prestado a</th>
        <th>DNI</th>
        <th>Devuelto</th>
        <th>Eliminar</th>
    </tr>
</thead>
% for prestamo in data["prestamos"]:
   
    <tr>
        <td><a href="/prestamo/{{prestamo["id"]}}"> {{prestamo["id"]}}</a></td>
        <td><a href="/juego/{{prestamo["juego_id"]}}">{{prestamo["juego_id"]}}</a></td>
        <td>{{prestamo["fecha_inicio"]}}</td>
        <td>{{prestamo["fecha_fin"]}}</td>
        <td>{{prestamo["usuario_prestado"]}}</td>
        <td>{{prestamo["dni_prestado"]}}</td>
        <td>{{prestamo["devuelto"]}}</td>
        <td><a href="/prestamo/{{prestamo["id"]}}/eliminar"><span class="text-danger">Eliminar</span></a></td>
    </tr> 

% end

</table>
<h3>Añadir prestamo</h3>
<form action="/prestamo" method="post" class="form-horizontal">
    <div class="form-group">
        <label class="col-sm-2">Selecciona el juego</label>
        <div class="col-sm-4">
            <select name="juegoPrest" class="form-control">
                % for juego in data["juegos"]:
                    <option value="{{juego["id"]}}">{{juego["nombre"]}}</option>
                % end
            </select>
        </div>
    </div>
    <div class="form-group">
        <label class="col-sm-2">Introduce el nombre del destinatario del prestamo</label>
        <div class="col-sm-4">
            <input type="text" name="personaPrest" class="form-control" placeholder="Nombre del destinatario del prestamo">
        </div>
    </div>
    <div class="form-group">
        <label class="col-sm-2">Introduce el dni del destinatario del prestamo</label>
        <div class="col-sm-4">
            <input type="text" name="dniPrest" class="form-control" placeholder="Nombre del destinatario del prestamo">
        </div>
    </div>
    <div class="form-group">
        <div class="col-sm-offset-2 col-sm-4">
          <button type="submit" class="btn btn-default">Añadir préstamo</button>
        </div>
    </div>
</form>

%include('footer.tpl')